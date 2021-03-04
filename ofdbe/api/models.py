from django.db import models

# Create your models here.


class OFDStatus(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    size = models.CharField(max_length=256)
