from django.shortcuts import render
from django.http import HttpResponse
from . import forms, models
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings





# Create your views here.
@csrf_exempt
def index(request):
    form = forms.UploadForm(request.POST)
    data = {'form': form}

    index_html = render(request, 'uploader/index.html', data)

    return index_html



def upload_image(request):

    #If no image, redirect
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

            print('FORM: ', form)
            print('FORM INSTANCE IMAGE URL:  ', form.instance.image.url)

            weird_path = form.instance.image.url
            fixed_path = 'C:/' + weird_path.split('3A/')[1]

            print(fixed_path)





            print('form', str(form))
            print('form instace:  ',str(form.instance))
            print('form instance image',  str(form.instance.image))
            print('url:  ', str(form.instance.image.url))
            print('form fields  ', form.fields)

            MEDIA_ROOT = getattr(settings, "MEDIA_ROOT")
            MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'uploader\\')
            print("MEDIA_ROOT:  ", MEDIA_ROOT)

            inmemobj = request.FILES['image']
            img_name = str(inmemobj)
            img_path = os.path.join(MEDIA_ROOT, img_name)

            print("img_path: ", img_path)

            data = {'path': fixed_path, "form": form, 'MEDIA_ROOT': MEDIA_ROOT, 'name': img_name}

            return render(request, 'uploader/image.html', {'data': data})

        elif not form.is_valid():
            return HttpResponse('Form Invalid')

    else:
        return HttpResponse('Not POST')

