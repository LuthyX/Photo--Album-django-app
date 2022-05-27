from unicodedata import category
from django.shortcuts import render, redirect
from .models import Category, Photo
# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {
        'categories' : categories,
        'photos' : photos
    }
    return render(request,'photos/gallery.html', context)

def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {
        'photo': photo
    }
    return render(request, 'photos/view.html', context)

def addphoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category =None
        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image = image
        )
        return redirect('gallery')
    return render(request, 'photos/add.html', {'categories': categories})

def viewcategory(request, pk):
    category = Category.objects.get(id = pk)
    categories = Category.objects.all()
    photo_in_category =[]
    photos = Photo.objects.all()
    for photo in photos:
        if photo.category == category:
            photo_in_category.append(photo)
    context={
        'photo_in_category':photo_in_category,
        'categories' : categories,
        'category' : category
    }

    return render(request, 'photos/viewcategory.html', context)

def deletephoto(request,pk):
    deletephoto = Photo.objects.get(id =pk)
    deletephoto.delete()
    return redirect('gallery')