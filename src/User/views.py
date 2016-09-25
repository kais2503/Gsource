from rest_framework.generics import (ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,CreateAPIView)
from .serializers import UserListSerializers,UserDetailSerializers,UserRegisterSerializers,UserUpdateSerializers
from django.contrib.auth import get_user_model
User=get_user_model()


class UserListAPI(ListAPIView):

    queryset=User.objects.all()
    serializer_class=UserListSerializers
class UserDetailAPI(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserDetailSerializers
class UserCreateAPI(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializers
class UserDeleteAPI(RetrieveDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserDetailSerializers
class UserUpdateAPI(RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserUpdateSerializers
