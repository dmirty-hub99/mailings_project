from rest_framework import generics

from .models import Client, Mailing, Message
from .serializers import ClientSerializer, MailingSerializer, MessageSerializer


class AddClient(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class AllClients(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class AddMailing(generics.CreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class AllMailings(generics.ListAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class AllMessages(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
