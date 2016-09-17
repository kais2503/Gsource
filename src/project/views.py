from rest_framework.generics import (
        ListAPIView,
        RetrieveAPIView,
        RetrieveUpdateAPIView,
        RetrieveDestroyAPIView,
        ListCreateAPIView)
from .models import Project
from .serializers import (
        ProjectListSerializer,
        ProjectCreateUpdateSerializer)
from rest_framework.permissions  import (
        AllowAny,
        IsAuthenticated,
        IsAdminUser,
        IsAuthenticatedOrReadOnly,

        )

class ProjectList(ListAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectListSerializer
    permission_classes=[AllowAny]
class ProjectDetail(RetrieveAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectListSerializer
class ProjectUpdate(RetrieveUpdateAPIView):
    queryset=Project.objects.all()
    serializer_class = ProjectCreateUpdateSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]
class ProjectDelete(RetrieveDestroyAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectListSerializer
    permission_classes=[IsAuthenticated ,IsAdminUser]

class ProjectCreate(ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectCreateUpdateSerializer
    permission_classes=[IsAdminUser]
