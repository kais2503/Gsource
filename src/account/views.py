from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,CreateAPIView
from .serializers import AccountListSerializer,AccountUpdateSerializer,AccountDetailSerializer,AccountCreateSerializer
from .models import Account

class AccountList(ListAPIView):
    queryset=Account.objects.all()
    serializer_class= AccountListSerializer
class AccountUpdate(RetrieveUpdateAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountUpdateSerializer
class AccountDelete(RetrieveDestroyAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountDetailSerializer
class AccountCreate(CreateAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountCreateSerializer
class AccountDetail(RetrieveAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountDetailSerializer
