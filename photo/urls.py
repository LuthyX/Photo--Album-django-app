from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    path('addphoto/', views.addphoto, name = 'addphoto'),
    path('viewphoto/<str:pk>/', views.viewphoto, name = 'viewphoto'),
    path('viewcategory/<str:pk>/', views.viewcategory, name= 'viewcategory'),
    path('deletephoto/<str:pk>/', views.deletephoto, name='deletephoto'),
    path('login/', views.login_user, name= 'login_user'),
    path('logout/', views.logout_user, name= 'logout_user'),
    path('register/', views.register_user, name='register_user')
]