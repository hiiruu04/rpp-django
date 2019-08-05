from django.shortcuts import render
from ULB.api.serializers import DatasetSerializers
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
# Create your views here.

def file_upload(request):
    return render(request, "file_upload.html", {})

def predict(request):
    return render(request, 'predict.html', {})