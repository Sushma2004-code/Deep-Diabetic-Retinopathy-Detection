from django import forms
from datasets.models import FundusImage
class DiagnosisUploadForm(forms.ModelForm):
    class Meta:
        model = FundusImage
        fields = ['patient','image','notes']
