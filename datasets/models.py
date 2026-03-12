from django.db import models
class Patient(models.Model):
    name = models.CharField(max_length=200, blank=True)
    dob = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return self.name or f'Patient #{self.pk}'

class FundusImage(models.Model):
    patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='fundus/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f'Image {self.pk} - {self.uploaded_at:%Y-%m-%d %H:%M}'
