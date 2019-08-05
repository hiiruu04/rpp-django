from django.contrib import admin
from .models import ULBdataLabelled, Dataset, Models
# Register your models here.
admin.site.register([ULBdataLabelled, Dataset, Models])