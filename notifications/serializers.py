from rest_framework import serializers


class SendMailSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=5000)
    recipient = serializers.EmailField()
