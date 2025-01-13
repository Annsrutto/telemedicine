import requests
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import Appointment, Department, Doctor, Contact, UploadedImage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from telemed_app.credentials import LipanaMpesaPpassword, MpesaAccessToken


# Create your views here.
def home(request):
    """This is the landing page"""
    return render(request, 'pages/index.html')

def about(request):
    """This is the about page"""
    return render(request, 'pages/about.html')

def services(request):
    """This is the services page"""
    return render(request, 'pages/services.html')

def specialist(request):
    """This is the specialists page"""
    return render(request, 'pages/specialists.html')

def doctor(request):
    """This is the doctor's page"""
    return render(request, 'pages/doctor.html')

def departments(request):
    """This is departments page"""
    return render(request, 'pages/departments.html')

def department(request):
    """This is single department page"""
    return render(request, 'pages/department.html')

def contact(request):
    """This is the contacts page"""
    if request.method == 'POST':
        contacts = Contact (
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            phone = request.POST['phone'],
            message = request.POST['message'],
        )
        contacts.save()
        return redirect('telemed_app:home')
    else:
        return render(request, 'pages/contact.html')

@login_required(login_url='user_auth:login')
def appointments(request):
    """Contains form for booking appointments"""
    # Check if its a POST method
    if request.method == 'POST':
        # Create a variable to pick appointments table inputs
        appointments = Appointment (
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            doctor = request.POST['doctor'],
            department = request.POST['department'],
            message = request.POST['message'],
            user = request.user,
        )
        # Save the variable
        appointments.save()
        # Redirect
        return redirect('telemed_app:all_appointments')
        
    else:
        departments = Department.objects.all()
        doctors = Doctor.objects.all()
        context = {
            'departments': departments, 
            'doctors': doctors
            }
        return render(request, 'pages/appointment.html', context)

# Retrieve all appointments
@login_required(login_url='user_auth:login')
def display_appointments(request):
    """Displays all appointments"""
    # Create variable for storing appointments
    appointments = Appointment.objects.filter(user=request.user)
    context = {'appointments': appointments}
    return render(request, 'pages/display_appointments.html', context)

def delete_appointment(request, id):
    """Deletes appointment by id"""
    appointment = Appointment.objects.get(id=id)

    appointment.delete()
    return redirect('telemed_app:all_appointments')

def update_appointments(request, appointment_id):
    """Updates appointments by id"""
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        try:
            appointment.name = request.POST.get('name')
            appointment.email = request.POST.get('email')
            appointment.phone = request.POST.get('phone')
            appointment.date = request.POST.get('date')
            appointment.doctor = request.POST.get('doctor')
            appointment.department = request.POST.get('department')
            # appointment.appointment_type = request.POST.get('appointment_type')
            # appointment.booking = request.POST.get('booking')
            appointment.message = request.POST.get('message')
            user = request.user

            appointment.save()
            messages.success(request, "Appointment updated successfully")
            return redirect('telemed_app:all_appointments')
        except:
            messages.error(request, "Failed! Try again")
    departments = Department.objects.all()
    doctors = Doctor.objects.all()
    context = {
            'departments': departments, 
            'doctors': doctors,
            'appointment': appointment
            }
    # context = {'appointment': appointment}
    return render(request, 'pages/update_appointment.html', context)

# @login_required 
def upload_images(request):
    """Uploads images"""
    if request.method == 'POST':
        # Retrieve data from the form
        title = request.POST['title']
        uploaded_file = request.FILES['image']

        # Save the file using FileSystemStorage
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)

        # Save file information to the database
        image = UploadedImage.objects.create(title=title, image=filename)
        image.save()
        
        context = {'file_url': file_url}
        return render(request, 'pages/upload_success.html', context)

    return render(request, "pages/upload_image.html")


# MPESA credentials views

#Display the payment form
def pay(request):
   """ Renders the form to pay """
   return render(request, 'pages/pay.html')

# Generate the ID of the transaction
def token(request):
    """ Generates the ID of the transaction """
    consumer_key = 'I60IAP6GlrauJabfvo0uTL7UuBkQ9OYfGb9x5rxsb8K6QxVv'
    consumer_secret = 'xtlpht7FAXDUMGIygd9Jc9WMsbbT9u9rjbiYQz1XGEShfSeIirWl6R2bGu5JWph5'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'pages/token.html', {"token":validated_mpesa_access_token})

# Send the stk push
def stk(request):
    """ Sends the stk push prompt """
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "InsightiaTech",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        # return HttpResponse("Payment successful")

        return redirect('telemed_app:appointments')
