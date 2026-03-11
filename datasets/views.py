from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .models import FundusImage
from .forms import FundusUploadForm

def dataset_list(request):
    imgs = FundusImage.objects.order_by('-uploaded_at')[:100]
    return render(request,'datasets/list.html', {'images': imgs})

def upload_image(request):
    if request.method == 'POST':
        form = FundusUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('datasets:list')
    else:
        form = FundusUploadForm()
    return render(request, 'datasets/upload.html', {'form': form})

def export_csv(request):
    qs = FundusImage.objects.all().order_by('-uploaded_at')[:1000]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fundus_images.csv"'
    writer = csv.writer(response)
    writer.writerow(['id','patient','uploaded_at','label','notes','image_path'])
    for i in qs:
        writer.writerow([i.id, i.patient_id if i.patient else '', i.uploaded_at, i.label, i.notes, i.image.name if i.image else ''])
    return response
