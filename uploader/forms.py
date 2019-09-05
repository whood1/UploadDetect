from django import forms
from . import models


class TestForm(forms.ModelForm):
    class Meta:
        model = models.TestModel
        fields = ['text']


class UploadForm(forms.ModelForm):
    class Meta:
        model = models.UserImage
        fields = ('image',)

# class UploadForm(forms.Form):
#    class Meta:
#        title = forms.CharField(max_length=10)
#        file = forms.FileField(label='Choose a file')
