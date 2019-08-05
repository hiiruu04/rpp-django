from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .utils import get_pickle
from ULB.services import get_dataset, send_csv_to_db, pick_model
from django.views.generic import ListView, CreateView, UpdateView
from random_forest.models_randomForest import RandomForest
from ULB.models import Dataset
from ULB.api.serializers import DatasetSerializers
from django.core.management import call_command

def index(request):
    return render(request, "index.html", {})

def indexIF(request):
    return render(request, "indexIF.html", {})
    
def home(request):
    return render(request, "home.html")

def settings(request):
    pickles = get_pickle()
    return render(request, "rpp/settings.html", 
    {'pickles' : pickles})


def setpickle(request, **kwargs):
    pick_model(kwargs['choice'])
    return HttpResponseRedirect(reverse('settings'))

def importDb(request, *args, **kwargs):
    pk = kwargs['pk']
    send_csv_to_db(pk)
    return HttpResponseRedirect(reverse('settings'))

def changeState(request, *args, **kwargs):
    dataset = Dataset.objects.get(id=kwargs['pk'])
    if dataset.finished == 1:
        dataset.finished = 0
        call_command('importcommand', dataset.id)
    else:
        dataset.finished = 1
    dataset.save()
    return HttpResponseRedirect(reverse('datatest-view'))

class DatasetListView(ListView):
    model = Dataset
    template_name = 'datatest/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["datatests"] = Dataset.objects.all() 
        return context

    def post(self, request, *args, **kwargs):
        return changeState(self.id)

    
    