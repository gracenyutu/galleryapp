from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'gallery/home.html')

def about(request):
    return render(request, 'gallery/about.html', {'title': 'About'})

def viewPhoto(request, pk):
    return render(request, 'gallery/viewphoto.html', {'title': 'ViewPhoto'})

def addPhoto(request):
    return render(request, 'gallery/addphoto.html', {'title': 'AddPhoto'})