from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# Create your views here.

def login_user(request):
    page='login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('gallery')
        else:
            return render(request, 'photos/login_register.html', {'page':page})
    return render(request, 'photos/login_register.html', {'page': page})

def logout_user(request):
    logout(request)
    return redirect('login_user')

def register_user(request):
    form = CustomUserCreationForm()
    page = 'register'
    context = {
        'form': form,
        'page' : page
    }
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user =form.save(commit= False)
            user.save()

            user=authenticate(request, username=user.username, password=request.POST['password2'])
            if user is not None:
                login(request, user)
                return redirect('gallery')


    return render(request, 'photos/login_register.html', context)

@login_required(login_url='login_user')
def gallery(request):
    user = request.user
    categories = Category.objects.filter(user= user)
    photos = Photo.objects.filter(category__user = user)
    context = {
        'categories' : categories,
        'photos' : photos
    }
    return render(request,'photos/gallery.html', context)

@login_required(login_url='login_user')
def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {
        'photo': photo
    }
    return render(request, 'photos/view.html', context)

@login_required(login_url='login_user')
def addphoto(request):
    user = request.user
    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user = user,
                name=data['category_new'])
        else:
            category =None
        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image = image
        )
        return redirect('gallery')
    return render(request, 'photos/add.html', {'categories': categories})

@login_required(login_url='login_user')
def viewcategory(request, pk):
    user =request.user
    category = Category.objects.get(id = pk)
    categories = Category.objects.filter(user = user)
    photo_in_category =[]
    photos = Photo.objects.filter(category__user = user)
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