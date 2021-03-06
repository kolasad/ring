from django.conf import settings
from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from notifications.models import Flower, Mail
from notifications.serializers import SendMailSerializer, FlowerSerializer, FlowerListSerializer, MailSerializer


class SendMailView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response('unauthorized', status=status.HTTP_401_UNAUTHORIZED)

        serializer = SendMailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            send_mail(
                subject,
                message,
                from_email=settings.EMAIL_FROM,
                recipient_list=[serializer.validated_data['recipient']]
            )
            Mail.objects.create(
                subject=subject,
                message=message
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlowerViewSet(ModelViewSet):
    """
    API endpoint for flowers view, edition
    """
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['color', 'name']
    search_fields = ['name']
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.action == 'list':
            return FlowerListSerializer
        return FlowerSerializer


class MailListView(ListAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
