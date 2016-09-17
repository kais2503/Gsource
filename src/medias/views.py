from rest_framework.generics import (
        ListAPIView,
        RetrieveAPIView,
        RetrieveUpdateAPIView,
        RetrieveDestroyAPIView,
        ListCreateAPIView)

from .models import Media
from .serializers import (
        MediaListSerializer,
        MediaCreateUpdateSerialzer)
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser)


class MediaList(ListAPIView):
    queryset=Media.objects.all()
    serializer_class=MediaListSerializer
    permission_classes=[AllowAny]

class MediaDetail(RetrieveAPIView):
    queryset=Media.objects.all()
    serializer_class=MediaCreateUpdateSerialzer
    permission_classes=[AllowAny]
class MediaUpdate(RetrieveUpdateAPIView):
    queryset=Media.objects.all()
    serializer_class=MediaCreateUpdateSerialzer
    permission_classes=[IsAdminUser]
class MediaDelete(RetrieveDestroyAPIView):
    queryset=Media.objects.all()
    serializer_class=MediaCreateUpdateSerialzer
    permission_classes=[IsAdminUser]
class MediaCreate(ListCreateAPIView):
    queryset=Media.objects.all()
    serializer_class=MediaCreateUpdateSerialzer
    permission_classes=[IsAuthenticated]
