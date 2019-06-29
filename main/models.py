from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from main.generic import upload_to

class Picture(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_to("img"))
    modified_img = models.ImageField(upload_to="img", blank=True, editable=False)

    def save(self, *args, **kwargs):
        try:
            self.make_thumbnail()
        except Exception as e:
            print("Couldn't create a thumbnail ", e)

        super().save(*args, **kwargs)

    def make_thumbnail(self):
        try:
            image = Image.open(self.image)
            image.thumbnail((20,20))

            with BytesIO() as temp_bytes:
                image.save(temp_bytes, format='PNG')
                temp_bytes.seek(0)
                self.modified_img.save(self.name + "_mini", ContentFile(temp_bytes.read()), save=False)

        except Exception as e:
            raise e


