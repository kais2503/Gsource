from django.conf.urls import url,include
from django.contrib import admin
from .views import (
        MediaList,
        MediaDetail,
        MediaUpdate,
        MediaDelete,
        MediaCreate,)


urlpatterns=[
        url(r'^$', MediaList.as_view(), name='Media'),
        url(r'^(?P<pk>\d+)/$', MediaDetail.as_view(), name='detail'),
        url(r'^edit/(?P<pk>\d+)/$', MediaUpdate.as_view(), name='edit'),
        url(r'^delete/(?P<pk>\d+)/$', MediaDelete.as_view(), name='delete'),
        url(r'^create$', MediaCreate.as_view(), name='create'),


]
