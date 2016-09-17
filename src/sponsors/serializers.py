from rest_framework import serializers
from .models import Sponsor

class SponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sponsor
        fields=['id','libelle','email','tel','adresse','domaine','pack','website','facebookpage','responsable',]
class SponsorUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sponsor
        fields=['libelle','email','tel','adresse','domaine','pack','website','facebookpage','responsable',]
