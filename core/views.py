from django.shortcuts import render, redirect
from core.forms import Upload
from core.models import Images
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == "POST":
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image Uploaded Successfully")
            return redirect("/")
    form = Upload()
    photos = Images.objects.all()
    context = {
        'form': form,
        'photos': photos
    }
    return render(request, 'core/home.html', context)


def delete(request, id):
    photo = Images.objects.get(id=id)
    if photo:
        photo.delete()
    messages.warning(request, "Image has been deleted !!")
    return redirect('/')

