from rest_framework.generics import (
        ListAPIView,
        RetrieveAPIView,
        RetrieveUpdateAPIView,
        RetrieveDestroyAPIView,
        ListCreateAPIView,)
from .models import Contact
from .serializers import (
        ContactListSerializer,
        ContactCreateUpdateSerializer,)


class  ContactList(ListAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactListSerializer
class ContactDetail(RetrieveAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactCreateUpdateSerializer
class ContactUpdate(RetrieveUpdateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactCreateUpdateSerializer
class ContactDelete(RetrieveDestroyAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactCreateUpdateSerializer
class ContactCreate(ListCreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactCreateUpdateSerializer
