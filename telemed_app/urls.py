from django.urls import path
from . import views

app_name = 'telemed_app'

urlpatterns = [
    path('', views.home, name='home'), # Home url
    path('appointments/', views.appointments, name='appointments'), # Appointment url
    path('about/', views.about, name='about'), # About url
    path('services/', views.services, name='services'), # Services url
    path('specialist/', views.specialist, name='specialist'), # Specialists url
    path('doctor/', views.doctor, name='doctor'), # Doctor's url
    path('departments/', views.departments, name='departments'), # Departments url
    path('department/', views.department, name='department'), # Single department url
    path('contact/', views.contact, name='contact'), # Contact url
    path('all_appointments/', views.display_appointments, name='all_appointments'), # Display appointments url
    path('delete/<int:id>', views.delete_appointment, name='delete_appointment'), # Delete appointments url
    path('edit/<int:appointment_id>', views.update_appointments, name='update_appointments'), # Update appointments url
    path('upload/', views.upload_images, name='upload_images'), # Upload images url
    path('pay/', views.pay, name='pay'), # view the payment form
    path('stk/', views.stk, name='stk'), # send the stk push prompt
    path('token/', views.token, name='token'), # generate the token for that particular transaction
    # path('qr/', views.generate_qr, name='generate_qr'), # QR code generation
    path('qr/download/', views.generate_qr_download, name='generate_qr_download'), #Downloadable QRCode
]
