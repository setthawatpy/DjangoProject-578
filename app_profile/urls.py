from django.urls import path
from app_profile import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('educational', views.educational, name='educational'),
    path('interestingThings', views.interestingThings, name='interestingThings'),
    path('dreamCareer', views.dreamCareer, name='dreamCareer'),
    path('modelPerson', views.modelPerson, name='modelPerson'),
    path('createProduct', views.createProduct, name='createProduct'),
    path('lab10', views.lab10, name='lab10'),
    path('lab11', views.lab11, name='lab11'),
    path('lab12', views.lab12, name='lab12'),
]