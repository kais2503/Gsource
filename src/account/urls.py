from django.conf.urls import url,include
from django.contrib import admin
from.views import (AccountList,AccountUpdate,AccountDelete,AccountDetail,
AccountCreate)



urlpatterns = [
        url(r'^$', AccountList.as_view(), name='account'),
        url(r'^(?P<pk>\d+)/$', AccountDetail.as_view(), name='detail'),
        url(r'^edit/(?P<pk>\d+)/$', AccountUpdate.as_view(), name='edit'),
        url(r'^delete/(?P<pk>\d+)/$', AccountDelete.as_view(), name='delete'),
        url(r'^create/$', AccountCreate.as_view(), name='create'),

]
