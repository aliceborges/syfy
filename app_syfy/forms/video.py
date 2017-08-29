from django.forms import *

from app_syfy.models.video import Video


class VideoForm(ModelForm):
    class Meta:
        model = Video