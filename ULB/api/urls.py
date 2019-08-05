from django.conf.urls import url
from ULB.api.views import FileUploadView, FileDetail, ApiRoot, ULBLabelList, ULBLabelDetail, ULBLabelListFraud
from rest_framework.response import Response
from rest_framework.reverse import reverse

urlpatterns = [

    url(r'^labeled-list/$',
    ULBLabelList.as_view(),
    name=ULBLabelList.name),

    url(r'^labeled-list/fraud/$',
    ULBLabelListFraud.as_view(),
    name=ULBLabelListFraud.name),

    url(r'^labeled-detail/(?P<pk>[0-9]+)$',
    ULBLabelDetail.as_view(),
    name=ULBLabelDetail.name),

    url(r'^file-upload/$', 
    FileUploadView.as_view(),
    name=FileUploadView.name),

    url(r'^file-upload/(?P<pk>[0-9]+)$', 
    FileDetail.as_view(),
    name=FileDetail.name),

    url(r'^$',
        ApiRoot.as_view(),
        name=ApiRoot.name),
]   
