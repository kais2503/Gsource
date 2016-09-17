from rest_framework.serializers import ModelSerializer
from .models import Media


class MediaListSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields=['id',
                'libelle',
                'adresse',
                'email',
                'responsable',
                'genre',
                ]
class MediaCreateUpdateSerialzer(ModelSerializer):
    class Meta:
        model=Media
        fields=['libelle',
                'adresse',
                'email',
                'responsable',
                'genre',
                ]
