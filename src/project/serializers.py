from rest_framework.serializers import ModelSerializer
from .models import Project




class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields =['id','titre','description','date',]
class ProjectCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model =Project
        fields=['titre','description','date']
