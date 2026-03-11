from django.contrib import admin
from .models import Patient, FundusImage
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','name','dob')

@admin.register(FundusImage)
class FundusImageAdmin(admin.ModelAdmin):
    list_display = ('id','patient','uploaded_at','label')
