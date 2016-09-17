from rest_framework.serializers import ModelSerializer
from .models import Poste


class PosteListSerializers(ModelSerializer):
    class Meta:
        model=Poste
        fields=[
                'id',
                'libelle',
                ]
class PosteCreateUpdateSerializer(ModelSerializer):
    class Meta:
        models=Poste
        fields=['libelle']
