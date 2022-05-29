from django.shortcuts import render
from .models import Category, Location, Image

# Create your views here.
def home(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    context = {'categories': categories, 'images': images}
    return render(request, 'gallery/home.html', context)

def about(request):
    return render(request, 'gallery/about.html', {'title': 'About'})

def viewPhoto(request, pk):
    image = Image.objects.get(id=pk)
    return render(request, 'gallery/viewphoto.html', {'title': 'ViewPhoto'}, {'image': image})

def addPhoto(request):
    return render(request, 'gallery/addphoto.html', {'title': 'AddPhoto'})