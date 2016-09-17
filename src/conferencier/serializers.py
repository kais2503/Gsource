from rest_framework.serializers import ModelSerializer
from .models import Conferencier

class ConferencierListSerializer(ModelSerializer):
    class Meta:
        model= Conferencier
        fields=['id',
                'nom',
                'prenom',
                'domaine',
                ]
class ConferencierUpdateCreateSerializer(ModelSerializer):
    class Meta:
        model= Conferencier
        fields=[
                'nom',
                'prenom',
                'domaine',
                ]
