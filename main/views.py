from .models import Picture
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import PictureForm


class PictureListView(ListView):

    model = Picture


class PictureCreate(CreateView):
    model = Picture
    success_url = reverse_lazy("new-pic")
    form_class = PictureForm

