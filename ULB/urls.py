from django.conf.urls import url, include
from ULB.api.views import FileUploadView, ApiRoot
from rest_framework.response import Response
from rest_framework.reverse import reverse
from ULB import views


urlpatterns = [
    url(r'^api/', include('ULB.api.urls')),
    url(r'^upload-data/$', views.file_upload, name='file-upload-ulb'),
    url(r'^predict/$', views.predict, name='predict'),
]
