from django.urls import path
from .views import PictureListView, add_picture

urlpatterns = [
    path("new_picture/", add_picture, name="new-pic"),
    path('all/', PictureListView.as_view(), name="all-pics"),

]