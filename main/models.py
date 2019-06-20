from django.db import models


class Picture(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img")


