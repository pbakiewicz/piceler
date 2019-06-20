from .models import Picture
from django.views.generic import ListView

class PictureListView(ListView):

    model = Picture