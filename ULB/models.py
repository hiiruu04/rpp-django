from django.db import models
from postgres_copy import CopyManager

# Create your models here.
class ULBdata(models.Model):
    CHOICES = [(i,i) for i in range(2)]
    Time = models.FloatField()
    V1 = models.FloatField()
    V2 = models.FloatField()
    V3 = models.FloatField()
    V4 = models.FloatField()
    V5 = models.FloatField()
    V6 = models.FloatField()
    V7 = models.FloatField()
    V8 = models.FloatField()
    V9 = models.FloatField()
    V10 = models.FloatField()
    V11 = models.FloatField()
    V12 = models.FloatField()
    V13 = models.FloatField()
    V14 = models.FloatField()
    V15 = models.FloatField()
    V16 = models.FloatField()
    V17 = models.FloatField()
    V18 = models.FloatField()
    V19 = models.FloatField()
    V20 = models.FloatField()
    V21 = models.FloatField()
    V22 = models.FloatField()
    V23 = models.FloatField()
    V24 = models.FloatField()
    V25 = models.FloatField()
    V26 = models.FloatField()
    V27 = models.FloatField()
    V28 = models.FloatField()
    Amount = models.FloatField()
    Class = models.IntegerField(choices=CHOICES)
    objects = CopyManager()

class ULBdataLabelled(models.Model):
    CHOICES = [(i,i) for i in range(2)]
    Timestamps = models.DateTimeField(auto_now_add=True)
    Time = models.FloatField()
    V1 = models.FloatField()
    V2 = models.FloatField()
    V3 = models.FloatField()
    V4 = models.FloatField()
    V5 = models.FloatField()
    V6 = models.FloatField()
    V7 = models.FloatField()
    V8 = models.FloatField()
    V9 = models.FloatField()
    V10 = models.FloatField()
    V11 = models.FloatField()
    V12 = models.FloatField()
    V13 = models.FloatField()
    V14 = models.FloatField()
    V15 = models.FloatField()
    V16 = models.FloatField()
    V17 = models.FloatField()
    V18 = models.FloatField()
    V19 = models.FloatField()
    V20 = models.FloatField()
    V21 = models.FloatField()
    V22 = models.FloatField()
    V23 = models.FloatField()
    V24 = models.FloatField()
    V25 = models.FloatField()
    V26 = models.FloatField()
    V27 = models.FloatField()
    V28 = models.FloatField()
    Amount = models.FloatField()
    Detect = models.IntegerField(choices=CHOICES)
    class Meta:
        ordering = ('Timestamps', )

class Dataset(models.Model):
    File = models.FileField(blank=False, null=False, upload_to='dataset/ulb/')
    finished = models.BooleanField(default=False)
    def __str__(self):
        return self.File.name

    def delete(self, *args, **kwargs):
        self.File.delete()
        super().delete(*args, **kwargs)
    
class Models(models.Model):
    is_supervised = models.BooleanField()