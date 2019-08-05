"""rpp_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home-ss3'),
    path('admin/', admin.site.urls),
    path('ML/', include('random_forest.urls', namespace='rf')),
    url(r'^ulb/', include('ULB.urls')),
    path('ML/home/', views.index, name='home-rf'),
    path('IF/home/', views.indexIF, name='home-if'),
    url(r'^datatests/', views.DatasetListView.as_view(), name='datatest-view'),
    path('settings/', views.settings, name='settings'),
    path('import/<int:pk>/', views.importDb, name='importDb'),
    path('pickle/<str:choice>/', views.setpickle, name='set_pickle'),
    path('changeState/<int:pk>/', views.changeState, name='changeState')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
