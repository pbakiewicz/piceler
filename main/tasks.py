from celery import shared_task
from PIL import Image
from .models import Picture
from io import BytesIO
from django.core.files.base import ContentFile


@shared_task
def modify_picture(id_picture, *args, **kwargs):
    try:
        pic = Picture.objects.get(pk=id_picture)
        image = Image.open(pic.image)
        ext = pic.image.name.split(".")[-1]
        image.thumbnail((20, 20))
        with BytesIO() as temp_image:
            # image.save("media/img/" + pic.name + "_mini." + ext)
              image.save(temp_image, format="JPEG")
              temp_image.seek(0)
              pic.modified_img.save(pic.name + "_mini." + ext,
                                    ContentFile(temp_image.read()))
    except Exception as e:
        raise e

