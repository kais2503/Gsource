from django.conf.urls import url,include
from django.contrib import admin
from.views import UserListAPI,UserDetailAPI,UserCreateAPI,UserUpdateAPI,UserDeleteAPI



urlpatterns = [
        url(r'^$', UserListAPI.as_view(), name='User'),
        url(r'^(?P<pk>\d+)/$', UserDetailAPI.as_view(), name='detail'),
        url(r'^edit/(?P<pk>\d+)/$', UserUpdateAPI.as_view(), name='edit'),
        url(r'^delete/(?P<pk>\d+)/$', UserDeleteAPI.as_view(), name='delete'),
        url(r'^create/$', UserCreateAPI.as_view(), name='create'),

]
