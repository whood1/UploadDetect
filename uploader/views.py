from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms
from django.views.decorators.csrf import csrf_exempt
import os
from django.core.files.images import ImageFile
from django.conf import settings




# Create your views here.
@csrf_exempt
def index(request):
    form = forms.UploadForm(request.POST)
    data = {'form': form}

    index_html = render(request, 'uploader/index.html', data)

    return index_html


@csrf_exempt
def upload_image(request):



    if str(request.FILES) == '<MultiValueDict: {}>':
        return render(request, 'uploader/nofile.html')



    print("REquest.post:    ",request.POST)
    print("REquest post get text",request.POST.get('text'))
    print("Request Files:  ",request.FILES)
    print("Request Files[0]:   ", request.FILES.get)

    print("Post Length: ", len(request.POST))
    print("File length: ", len(request.FILES))

    if request.method == "POST":

        # data = {'title': request.POST[0], 'file': request.FILES}

        form = forms.UploadForm(request.POST, request.FILES)
        print(form.errors)

        if form.is_valid():
            form.save()

            print('form', str(form))
            print('form instace:  ',str(form.instance))
            print('form instance image',  str(form.instance.image))
            print('url:  ', str(form.instance.image.url))

            theimg = form._meta.model.image
            print('form fields  ', form.fields)

            imagefield = form.fields['image']







            MEDIA_ROOT = getattr(settings, "MEDIA_ROOT")
            MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'img')
            print("MEDIA_ROOT:  ", MEDIA_ROOT)



            inmemobj = request.FILES['image']
            img_name = str(inmemobj)
            img_src = os.path.join(MEDIA_ROOT, img_name)

            print("src: ",img_src)

            data = {"src": img_src, "form": form, 'MEDIA_ROOT': MEDIA_ROOT}

            djangofileobj = inmemobj.open(mode='r')
            print(djangofileobj)
            print('1:   ',djangofileobj)
            print(djangofileobj.content_type)
            print(djangofileobj.size)

            imgobj = djangofileobj.file
            print(imgobj)

            #print("2:   ",imgobj)






            return render(request, 'uploader/image.html', {'data': data})

        elif not form.is_valid():
            return HttpResponse('Form Invalid')



    else:
        return HttpResponse('Not POST')


def test(request):
    print(request.POST)

    if request.method == "POST":
        form = forms.TestForm(request.POST)

        if form.is_valid():
            return HttpResponse("VALID")
        else:
            print(form.errors)
            return HttpResponse('FORM INVALID')

    else:
        return HttpResponse('NOT POST')
