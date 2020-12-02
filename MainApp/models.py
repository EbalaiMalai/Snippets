from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                        blank=True, null=True)