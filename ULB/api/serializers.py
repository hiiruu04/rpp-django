from rest_framework import serializers
from ULB.models import ULBdataLabelled, Dataset, ULBdata
from django import forms

class ULBSerializers(serializers.ModelSerializer):
    class Meta:
        model = ULBdata
        fields = (
            'Time',
            'V1',
            'V2',
            'V3',
            'V4',
            'V5',
            'V6',
            'V7',
            'V8',
            'V9',
            'V10',
            'V11',
            'V12',
            'V13',
            'V14',
            'V15',
            'V16',
            'V17',
            'V18',
            'V19',
            'V20',
            'V21',
            'V22',
            'V23',
            'V24',
            'V25',
            'V26',
            'V27',
            'V28',
            'Class',
        )
        
class ULBLabelledSerializers(serializers.ModelSerializer):
    class Meta:
        model = ULBdataLabelled
        fields = (
            'Time',
            'V1',
            'V2',
            'V3',
            'V4',
            'V5',
            'V6',
            'V7',
            'V8',
            'V9',
            'V10',
            'V11',
            'V12',
            'V13',
            'V14',
            'V15',
            'V16',
            'V17',
            'V18',
            'V19',
            'V20',
            'V21',
            'V22',
            'V23',
            'V24',
            'V25',
            'V26',
            'V27',
            'V28',
            'Detect',
            'Timestamps',
        )

class DatasetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = "__all__"
