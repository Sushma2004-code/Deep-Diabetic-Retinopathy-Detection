from django.shortcuts import render, redirect, get_object_or_404
from .forms import DiagnosisUploadForm
from datasets.models import FundusImage
from .model import run_inference_on_image

def upload_for_diagnosis(request):
    if request.method == 'POST':
        form = DiagnosisUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            result = run_inference_on_image(instance.image.path)
            instance.label = result['prediction']
            instance.save()
            return redirect('diagnosis:result', pk=instance.pk)
    else:
        form = DiagnosisUploadForm()
    return render(request,'diagnosis/upload.html', {'form': form})

def result_view(request, pk):
    obj = get_object_or_404(FundusImage, pk=pk)
    probs = {'No DR':0.7,'Mild':0.15,'Moderate':0.1,'Severe':0.04,'Proliferative':0.01}
    return render(request,'diagnosis/result.html', {'image': obj, 'probs': probs})
