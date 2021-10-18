from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .form import ImageForm
from .models import Image
from django.views.generic import DetailView, DeleteView


# Create your views here.
def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "index.html", {"obj": obj})
    else:
        form = ImageForm()
        img = Image.objects.all()
    return render(request, "index.html", {"img": img, "form": form})


class ImageDetail(DetailView):
    model = Image
    template_name = 'image-detail.html'


class ImageDelete(DeleteView):
    model = Image
    template_name = 'image-delete .html'
    success_url = reverse_lazy('home')
