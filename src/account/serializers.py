from rest_framework import serializers
from .models import Account
from django.contrib.auth import get_user_model

from User.serializers import UserListSerializers

User=get_user_model()





class AccountListSerializer(serializers.ModelSerializer):

    username=serializers.CharField(source ='user.username')

    image=serializers.ImageField()
    class Meta:

        model= Account
        fields=['id','username','image',]
class AccountDetailSerializer(serializers.ModelSerializer):
    user=UserListSerializers()
    image=serializers.ImageField()

    class Meta:

        model= Account
        fields=['id','user','image',]
class AccountCreateSerializer(serializers.ModelSerializer):


    user=UserListSerializers()
    image=serializers.ImageField()

    class Meta:


        model= Account
        fields=['id','user','image']
    def create(self,validated_data):

          user_data = validated_data.pop('user')
          user = User.objects.create(**user_data)
          account = Account.objects.create(user=user, **validated_data)

          return account



class AccountUpdateSerializer(serializers.ModelSerializer):

    user=UserListSerializers(read_only=True)
    image=serializers.ImageField()
    class Meta:
        model=Account
        fields=['id','user','image',]
    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance
