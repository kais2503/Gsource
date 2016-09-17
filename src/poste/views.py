from rest_framework.generics import (
        ListAPIView,
        RetrieveAPIView,
        RetrieveUpdateAPIView,
        RetrieveDestroyAPIView,
        ListCreateAPIView)
from .models import Poste
from .serializers import (
        PosteListSerializers,PosteCreateUpdateSerializer)
from rest_framework.permissions  import (
        AllowAny,
        IsAuthenticated,
        IsAdminUser,
        IsAuthenticatedOrReadOnly,

        )

class PosteList(ListAPIView):
    queryset=Poste.objects.all()
    serializer_class=PosteListSerializers
    permission_classes=[AllowAny]
class PosteDetail(RetrieveAPIView):
    queryset=Poste.objects.all()
    serializer_class=PosteCreateUpdateSerializer
class PosteUpdate(RetrieveUpdateAPIView):
    queryset=Poste.objects.all()
    serializer_class = PosteCreateUpdateSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]
class PosteDelete(RetrieveDestroyAPIView):
    queryset=Poste.objects.all()
    serializer_class=PosteCreateUpdateSerializer
    permission_classes=[IsAuthenticated ,IsAdminUser]

class PosteCreate(ListCreateAPIView):
    queryset=Poste.objects.all()
    serializer_class=PosteCreateUpdateSerializer
    permission_classes=[IsAdminUser]
