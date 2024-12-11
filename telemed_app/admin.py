from django.contrib import admin
from .models import Appointment, Department, Doctor, Contact, UploadedImage

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Contact)
admin.site.register(UploadedImage)
