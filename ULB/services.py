import requests
from django.conf.urls import url
from ULB.models import Dataset, ULBdata, Models
from random_forest.models_randomForest import RandomForest
import csv
import pandas as pd
from django.conf import settings
from django.core.management import call_command
from django.http import HttpRequest

root_url = 'https://rpp-backend.herokuapp.com/'
# root_url = 'http://127.0.0.1:8000/'

def get_ulb_labelled():
    url = root_url + 'ulb/api/labeled-list/' 
    r = requests.get(url)
    ulb_labelled = r.json()
    return ulb_labelled

def get_dataset():
    url = root_url + 'ulb/api/file-upload/' 
    r = requests.get(url)
    dataset = Dataset.objects.all()
    return dataset

def send_csv_to_db(pk):
    call_command('importcommand', pk)

def pick_model(choice):
    if Models.objects.all().exists():
        model = Models.objects.all()[0]
        if choice == 'Supervised':
            model.is_supervised = True
        else:
            model.is_supervised = False
        model.save()
    else:
        if choice == 'Unsupervised':
            model = Models(
                is_supervised = True
            )
        else:
            model = Models(
                is_supervised = False
            )
        model.save()

