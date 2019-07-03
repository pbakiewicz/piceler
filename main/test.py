from django.test import RequestFactory, TestCase
from django.core.files import File
from django.conf import settings
import os

from .views import add_picture, PictureListView


class UploadFile(TestCase):

    def test_upload(self):
        self.factory = RequestFactory()
        request = self.factory.post("/pics/new_picture/", {"name": "super2"})

        img_path = os.path.join(settings.BASE_DIR, "main/test_image.jpg")
        with open(img_path, 'rb') as f:
            image = File(f)
            request.FILES['image'] = image
            response = add_picture(request)
            print(response)




