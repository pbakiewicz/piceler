from .models import Picture
from django.views.generic import ListView
from django.shortcuts import render
from .forms import PictureForm
from .tasks import modify_picture


class PictureListView(ListView):

    model = Picture


def add_picture(request):
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()

            #starting celery task
            modify_picture.delay(obj.id, form.cleaned_data['ext'])

    else:
        form = PictureForm()

    return render(request, "main/picture_form.html", {"form": form})

