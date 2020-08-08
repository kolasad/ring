from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SendMailView(APIView):
    def post(self, request):
        message = request.data.get('message')
        send_mail(
            'New email message title',
            message,
            from_email=settings.EMAIL_FROM,
            recipient_list=[request.data.get('recipient')]
        )
        return Response('OK', status=status.HTTP_200_OK)
