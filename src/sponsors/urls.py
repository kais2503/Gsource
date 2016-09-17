from django.conf.urls import url,include
from .views import (
    ListSponsors,
    SponsorDetail,
    SponsorUpdate,
    SponsorDelete,
    SponsorCreate,
)




urlpatterns = [
      url(r'^$',ListSponsors.as_view(),name='sposnors'),
      url(r'^(?P<pk>\d+)/$', SponsorDetail.as_view(), name='detail'),
      url(r'^edit/(?P<pk>\d+)/$', SponsorUpdate.as_view(), name='edit'),
      url(r'^delete/(?P<pk>\d+)/$', SponsorDelete.as_view(), name='delete'),
      url(r'^create$', SponsorCreate.as_view(), name='create'),
]
