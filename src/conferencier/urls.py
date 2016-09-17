from django.conf.urls import url,include
from django.contrib import admin
from .views import ConferencierList,ConferencierDetail,ConferencierUpdate,ConferencierCreate,ConferencierDelete



urlpatterns=[
        url(r'^$', ConferencierList.as_view(), name='Conferencier'),
        url(r'^(?P<pk>\d+)/$', ConferencierDetail.as_view(), name='detail'),
        url(r'^edit/(?P<pk>\d+)/$', ConferencierUpdate.as_view(), name='edit'),
        url(r'^delete/(?P<pk>\d+)/$', ConferencierDelete.as_view(), name='delete'),
        url(r'^create$', ConferencierCreate.as_view(), name='create'),




]
