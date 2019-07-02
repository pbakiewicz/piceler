from celery import shared_task
from PIL import Image
from .models import Picture


@shared_task
def modify_picture(id_picture, *args, **kwargs):
    try:
        pic = Picture.objects.get(pk=id_picture)
        image = Image.open(pic.image)
        ext = pic.image.name.split(".")[-1]
        image.thumbnail((20, 20))

        image.save("img/" + pic.name + "_mini." + ext)
    except Exception as e:
        raise e

