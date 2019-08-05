# chat/routing.py
from django.urls import re_path
from django.conf.urls import url
from ULB.consumer import StreamingConsumer

websocket_urlpatterns = [
    url(r'^ulb/predict/$',StreamingConsumer),
]