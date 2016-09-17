from rest_framework.serializers import ModelSerializer
from .models import Contact


class ContactListSerializer(ModelSerializer):
    class Meta:
        model= Contact
        fields=['id',
                'libelle',
                'description',
                'email',
                'adresse',
                'siteweb',
                'facebookpage',]
class ContactCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields=['libelle',
                'description',
                'email',
                'adresse',
                'siteweb',
                'facebookpage',
                ]
