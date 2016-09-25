from rest_framework import serializers
from .models import Account
from django.contrib.auth import get_user_model

from User.serializers import UserListSerializers

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','is_active','is_superuser']



class AccountListSerializer(serializers.ModelSerializer):

    username=serializers.CharField(source ='user.username')

    image=serializers.ImageField()
    class Meta:

        model= Account
        fields=['id','username','image',]
class AccountDetailSerializer(serializers.ModelSerializer):

    username=serializers.CharField(source ='my_user.username')
    class Meta:

        model= Account
        fields=['id','username','image',]
class AccountCreateSerializer(serializers.ModelSerializer):


    user=UserListSerializers()
    image=serializers.ImageField()

    class Meta:


        model= Account
        fields=['id','user','image']
    def create(self,validated_data):

        user_data=validated_data.pop('user')
        print(user_data)
        account=Account.objects.create(**validated_data)
        User.objects.create(account=account,**user_data)

        return account



class AccountUpdateSerializer(serializers.ModelSerializer):

    user=UserListSerializers(read_only=True)
    image=serializers.ImageField()
    class Meta:
        model=Account
        fields=['id','user','image',]
    def update(self, instance, validated_data):



        #instance.user=validated_data.get('user', instance.user)
        instance.image = validated_data.get('image', instance.image)
            #instance.my_user.username=validated_data.get('my_user.username' ,instance.my_user.username)

        instance.save()

        return instance
