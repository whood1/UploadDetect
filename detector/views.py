from django.shortcuts import render
from django.http import HttpResponse
from . import models, forms
import cv2
from django.core.files.uploadedfile import UploadedFile, InMemoryUploadedFile
from django.core.files.images import ImageFile
from django.conf import settings


# Create your views here.

def index(request):
    return render(request, 'detector/index.html')


def detect(request):
    print("Detect Request", str(request.POST))
    print("NAME:   ", request.POST['name'])

    orig_name = request.POST['name']
    orig_url = request.POST['url']
    orig_src = request.POST['src']

    split = orig_url.split('UploadDetect/')
    print('SPLIT:  ', split)
    orig_src = split[1]

    orig = cv2.imread(orig_src)
    print('image', orig.shape)

    # swapped_color = orig.copy()

    swapped_color = cv2.cvtColor(orig, cv2.COLOR_RGB2BGR)
    mod_name = 'mod_' + str(orig_name)

    location = getattr(settings, "MEDIA_ROOT")[0:-1] + '\\modified\\' + mod_name
    location2 = location.replace('/', '\\')
    # location = '/C:/Users/billy/Desktop/Projects/Python/Django/UploadDetect/media/modifed/test.png'

    cv2.imwrite(location, swapped_color)

    data = {'name': orig_name, 'url': orig_url, 'swapped': swapped_color, "location": location2}

    return render(request, 'detector/detect.html', {'data': data})
