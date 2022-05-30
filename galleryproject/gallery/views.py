from django.shortcuts import render
from .models import Category, Location, Image

# Create your views here.
def home(request):
    category =request.GET.get('category')
    if category == None:
        images = Image.objects.all()
    else:
        images = Image.objects.filter(category__name=category)
        
    categories = Category.objects.filter()
    context = {'categories': categories, 'images': images}
    return render(request, 'gallery/home.html', context)

def about(request):
    return render(request, 'gallery/about.html', {'title': 'About'})

def viewPhoto(request, pk):
    image = Image.objects.get(id=pk)
    return render(request, 'gallery/viewphoto.html',{'image': image})

def addPhoto(request):
    categories = Category.objects.all()
    location = Location.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category =Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(name=data['new_category'])
        else:
            category = None

        if data['location'] != 'none':
            location =Location.objects.get(id=data['location'])
        elif data['new_location'] != '':
            location, created = Location.objects.get_or_create(name=data['new_location'])
        else:
            location = None

        image = Image.objects.create(
            category=category,
            location=location,
            description=data['description'],
            image=image,
        )

    context = {'categories': categories, 'location': location}
    return render(request, 'gallery/addphoto.html', context)

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})