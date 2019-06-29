from django.urls import path
from .views import PictureListView, PictureCreate

urlpatterns = [
    path("new_picture/", PictureCreate.as_view(), name="new-pic"),
    path('all/', PictureListView.as_view(), name="all-pics"),

]