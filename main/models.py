from django.db import models
from main.generic import upload_to


class Picture(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_to("img"))
    modified_img = models.ImageField(upload_to="img", blank=True, editable=False)

    def __str__(self):
        return f"{self.id}. {self.name}"




