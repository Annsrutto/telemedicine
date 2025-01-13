from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Appointment(models.Model):
    """Contains the appointments table"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateTimeField()
    doctor = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"Dear {self.name}, your appointment with {self.doctor} was successfully booked"

class Department(models.Model):
    """Contains the departments table"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    """Contains the doctors model"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    """Contains the contacts table"""
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} your message was sent successfully"

class UploadedImage(models.Model):
    """Contains the table for uploading images"""
    title = models.CharField(max_length=100) # image title
    image = models.ImageField(upload_to='uploaded_images/') # floder to save images

    def __str__(self):
        return f"{self.title} uploaded successfully"


 