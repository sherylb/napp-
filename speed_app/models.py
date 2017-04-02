from datetime import *

from django.db import models


class Speed(models.Model):
    download_speed = models.DecimalField(max_digits=5,decimal_places=2)
    upload_speed = models.DecimalField(max_digits=5,decimal_places=2)
    score = models.IntegerField(max_length=20)
    name = models.TextField(max_length=50)
    mac = models.TextField(max_length=20)
    date = models.DateTimeField(default=timezone)
