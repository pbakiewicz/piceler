from .models import Picture
from django.views.generic import ListView, FormView
from .forms import PictureForm

class PictureListView(ListView):

    model = Picture


class PictureFormView(FormView):

    template_name = "send_picture.html"
    form_class = PictureForm
