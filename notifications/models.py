from django.contrib.auth.models import User
from django.db import models

from notifications.constants import ColorChoices


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Flower(models.Model):  # noqa: E302
    """
    Doc String
    Describes a flower
    Color, type etc.
    """

    color = models.IntegerField(choices=ColorChoices)
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @property
    def type(self):
        return 'flower'


class Mail(TimeStampedModel):
    """
    Holds data about email messages send by our service
    """
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=5000)
