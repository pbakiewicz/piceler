from django.urls import path
from .views import PictureFormView

urlpatterns = [
    path("new_picture/", PictureFormView.as_view(), name="new-pic"),
]