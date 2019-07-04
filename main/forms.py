import django.forms as forms
from .models import Picture


class PictureForm(forms.ModelForm):

    extensions = (
        ("JPEG", "jpg"),
        ("png", "png"),
        ("gif", "gif"),
        ("svg", "svg")
    )

    ext = forms.ChoiceField(choices=extensions)

    class Meta:
        model = Picture
        fields = ['name', 'image']

