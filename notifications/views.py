from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from notifications.serializers import SendMailSerializer


class SendMailView(APIView):
    def post(self, request):
        serializer = SendMailSerializer(data=request.data)
        if serializer.is_valid():
            send_mail(
                'New email message title',
                serializer.validated_data['message'],
                from_email=settings.EMAIL_FROM,
                recipient_list=[serializer.validated_data['recipient']]
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
