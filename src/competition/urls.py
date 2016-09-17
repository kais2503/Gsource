from django.conf.urls import url,include
from django.contrib import admin
from .views import CompetitionList,CompetitionCreate,CompetitionDelete,CompetitionDetail,CompetitionUpdate



urlpatterns=[
        url(r'^$', CompetitionList.as_view(), name='Competition'),
        url(r'^(?P<pk>\d+)/$', CompetitionDetail.as_view(), name='detail'),
        url(r'^edit/(?P<pk>\d+)/$', CompetitionUpdate.as_view(), name='edit'),
        url(r'^delete/(?P<pk>\d+)/$', CompetitionDelete.as_view(), name='delete'),
        url(r'^create$', CompetitionCreate.as_view(), name='create'),




]
