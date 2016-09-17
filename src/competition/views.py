from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,ListCreateAPIView
from .serializers import CompetitionListSerializer,CompetitionUpdateCreateSerializer
from .models import Competition



class CompetitionList(ListAPIView):
    queryset=Competition.objects.all()
    serializer_class= CompetitionListSerializer
class CompetitionDetail(RetrieveAPIView):
    queryset=Competition.objects.all()
    serializer_class=CompetitionUpdateCreateSerializer
class CompetitionUpdate(RetrieveUpdateAPIView):
    queryset=Competition.objects.all()
    serializer_class=CompetitionUpdateCreateSerializer
class CompetitionDelete(RetrieveDestroyAPIView):
    queryset=Competition.objects.all()
    serializer_class=CompetitionUpdateCreateSerializer

class CompetitionCreate(ListCreateAPIView):
    queryset=Competition.objects.all()
    serializer_class=CompetitionUpdateCreateSerializer
