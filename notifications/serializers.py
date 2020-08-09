from rest_framework import serializers

from notifications.models import Flower, Mail


class SendMailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=5000)
    recipient = serializers.EmailField()


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['color', 'name', 'description', 'owner']


class FlowerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['color', 'name']


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = '__all__'
