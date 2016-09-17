from django.conf.urls import url,include
from django.contrib import admin
from .views import PosteList,PosteDetail,PosteUpdate,PosteDelete,PosteCreate




urlpatterns = [
        url(r'^$', PosteList.as_view(), name='Poste'),
        url(r'^(?P<pk>\d+)/$', PosteDetail.as_view(), name='detail'),
        url(r'^edit/(?P<pk>\d+)/$', PosteUpdate.as_view(), name='edit'),
        url(r'^(?P<pk>\d+)/$', PosteDelete.as_view(), name='delete'),
        url(r'^create/$', PosteCreate.as_view(), name='create'),

]
