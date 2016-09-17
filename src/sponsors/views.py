from rest_framework.generics import (
        ListAPIView,
        RetrieveAPIView,
        RetrieveUpdateAPIView,
        DestroyAPIView,
        CreateAPIView)
from.models import Sponsor
from .serializers import (
    SponsorListSerializer,
    SponsorUpdateCreateSerializer
)
from rest_framework.permissions import(AllowAny,is_authenticated,IsAdminUser)

class ListSponsors(ListAPIView):
    queryset=Sponsor.objects.all()
    serializer_class=SponsorListSerializer
    permission_classes=[AllowAny]
class SponsorDetail(RetrieveAPIView):
    queryset=Sponsor.objects.all()
    serializer_class=SponsorUpdateCreateSerializer
    permission_classes=[AllowAny]
class SponsorUpdate(RetrieveUpdateAPIView):
    queryset=Sponsor.objects.all()
    serializer_class=SponsorUpdateCreateSerializer
    permission_classes=[IsAdminUser]
class SponsorDelete(DestroyAPIView):
    queryset=Sponsor.objects.all()
    serializer_class=SponsorUpdateCreateSerializer
    permission_classes=[IsAdminUser]
class SponsorCreate(CreateAPIView):
    queryset=Sponsor.objects.all()
    serializer_class=SponsorUpdateCreateSerializer
    permission_classes=[IsAdminUser]
