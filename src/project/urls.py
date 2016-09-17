from django.conf.urls import url,include
from django.contrib import admin
from.views import ProjectList,ProjectDetail,ProjectUpdate,ProjectDelete,ProjectCreate



urlpatterns = [
  url(r'^$', ProjectList.as_view(), name='Project'),
  url(r'^(?P<pk>\d+)/$', ProjectDetail.as_view(), name='detail'),
  url(r'^edit/(?P<pk>\d+)/$', ProjectUpdate.as_view(), name='edit'),
  url(r'^delete/(?P<pk>\d+)/$', ProjectDelete.as_view(), name='delete'),
  url(r'^create$', ProjectCreate.as_view(), name='create'),
]
