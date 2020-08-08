from django.contrib.auth.models import User
from django.db import models

from notifications.constants import ColorChoices


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
