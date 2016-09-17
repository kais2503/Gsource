from django.conf.urls import url,include
from django.contrib import admin
from.views import (ContactList,
            ContactDetail,
            ContactUpdate,
            ContactDelete,
            ContactCreate,)



urlpatterns = [
        url(r'^$', ContactList.as_view(), name='Contact'),
        url(r'^(?P<pk>\d+)/$', ContactDetail.as_view(), name='detail'),
        url(r'^edit/(?P<pk>\d+)/$', ContactUpdate.as_view(), name='edit'),
        url(r'^(?P<pk>\d+)/$', ContactDelete.as_view(), name='delete'),
        url(r'^create/$', ContactCreate.as_view(), name='create'),

]
