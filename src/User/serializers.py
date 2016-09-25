from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.validators import ValidationError
from rest_framework import serializers
User=get_user_model()

class UserListSerializers(ModelSerializer):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','is_active','is_superuser',]

class UserDetailSerializers(ModelSerializer):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','is_active','is_superuser',]
class UserUpdateSerializers(ModelSerializer):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','is_active','is_superuser',]
class UserRegisterSerializers(ModelSerializer):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','is_active','is_superuser',]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
                username = username,
                email = email
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
    def validate_email(self,value):
        email=value
        user_qs=User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("this user is already registred.")
        return value
