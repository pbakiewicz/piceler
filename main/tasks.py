from celery import shared_task
from PIL import Image
from .models import Picture
from io import BytesIO
from django.core.files.base import ContentFile


@shared_task
def modify_picture(id_picture, ext):
    try:
        pic = Picture.objects.get(pk=id_picture)
        image = Image.open(pic.image)
        image.thumbnail((20, 20))
        with BytesIO() as temp_image:
            image.save(temp_image, format=ext)
            temp_image.seek(0)
            final_name = pic.name + "_mini." + ext
            pic.modified_img.save(final_name,
                                  ContentFile(temp_image.read()))
    except Exception as e:
        raise e

