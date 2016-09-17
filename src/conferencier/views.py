from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,ListCreateAPIView
from .serializers import ConferencierListSerializer,ConferencierUpdateCreateSerializer
from .models import Conferencier



class ConferencierList(ListAPIView):
    queryset=Conferencier.objects.all()
    serializer_class= ConferencierListSerializer
class ConferencierDetail(RetrieveAPIView):
    queryset=Conferencier.objects.all()
    serializer_class=ConferencierUpdateCreateSerializer
class ConferencierUpdate(RetrieveUpdateAPIView):
    queryset=Conferencier.objects.all()
    serializer_class=ConferencierUpdateCreateSerializer
class ConferencierDelete(RetrieveDestroyAPIView):
    queryset=Conferencier.objects.all()
    serializer_class=ConferencierUpdateCreateSerializer

class ConferencierCreate(ListCreateAPIView):
    queryset=Conferencier.objects.all()
    serializer_class=ConferencierUpdateCreateSerializer
