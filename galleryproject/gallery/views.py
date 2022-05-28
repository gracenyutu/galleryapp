from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'gallery/home.html')

def about(request):
    return render(request, 'gallery/about.html')

def viewPhoto(request, id):
    return render(request, 'gallery/viewphoto.html')

def addPhoto(request):
    return render(request, 'gallery/addphoto.html')