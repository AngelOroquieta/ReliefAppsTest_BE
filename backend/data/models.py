from django.db import models

class Data(models.Model):
    url = models.CharField(max_length=120, blank=False, default='')
