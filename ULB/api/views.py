from django.shortcuts import render
from rest_framework import generics, filters, permissions
from rest_framework.views import APIView
from ULB.models import ULBdataLabelled, Dataset, ULBdata
from ULB.api.serializers import ULBLabelledSerializers, DatasetSerializers, ULBSerializers
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import FileUploadParser
from rest_framework import status


# Create your views here.

class ULBList(generics.ListCreateAPIView):
    queryset = ULBdata.objects.all()
    serializer_class = ULBSerializers
    name = 'ulb-list'

class ULBDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ULBdata.objects.all()
    serializer_class = ULBSerializers
    name = 'ulb-detail'

class ULBLabelList(generics.ListCreateAPIView):
    queryset = ULBdataLabelled.objects.all()
    serializer_class = ULBLabelledSerializers
    name = 'ulb-labeled-list'

class ULBLabelListFraud(generics.ListCreateAPIView):
    pagination_class = None
    queryset = ULBdataLabelled.objects.filter(Detect=1)
    serializer_class = ULBLabelledSerializers
    name = 'ulb-labeled-list-fraud'

class ULBLabelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ULBdataLabelled.objects.all()
    serializer_class = ULBLabelledSerializers
    name = 'ulb-labeled-detail'

class FileUploadView(generics.ListCreateAPIView):
    name = 'file-api'
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializers

class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializers
    name = 'file-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-ulb-root'
    def get(self, request, *args, **kwargs):
        return Response({
            ULBList.name: reverse(ULBList.name, request=request),
            ULBLabelList.name: reverse(ULBLabelList.name, request=request),
            ULBLabelListFraud.name: reverse(ULBLabelListFraud.name, request=request),
            FileUploadView.name: reverse(FileUploadView.name, request=request),
        })