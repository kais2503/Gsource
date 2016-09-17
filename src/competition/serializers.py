from rest_framework.serializers import ModelSerializer
from .models import Competition

class CompetitionListSerializer(ModelSerializer):
    class Meta:
        model= Competition
        fields=[ 'id',
                 'libelle',
                 'description',
                 'date',
                 'lieu',

        ]
class CompetitionUpdateCreateSerializer(ModelSerializer):
    class Meta:
        model= Competition
        fields=[ 
                 'libelle',
                 'description',
                 'date',
                 'lieu',

        ]
