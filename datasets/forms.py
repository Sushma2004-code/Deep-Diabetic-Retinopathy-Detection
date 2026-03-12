from django import forms
from .models import FundusImage
class FundusUploadForm(forms.ModelForm):
    class Meta:
        model = FundusImage
        fields = ['patient','image','label','notes']
