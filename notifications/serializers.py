from rest_framework import serializers

from notifications.models import Flower


class SendMailSerializer(serializers.Serializer):
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
