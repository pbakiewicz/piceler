
from django.contrib import admin
from django.urls import path, include
from main.views import PictureListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pics/', include('main.urls')),
    path('all/', PictureListView.as_view(), name="all-pics")
]
