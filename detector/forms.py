from django import forms
from . import models


class ModifiedImageForm(forms.ModelForm):
    class Meta:
        model = models.ModifiedImage
        fields = ('modified_image',)

