from django.db import models

# Create your models here.
from django.utils import timezone


class TimeStamps(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    class Meta:
        abstract = True
