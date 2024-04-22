from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.showRecipes,name="recipes"),
    path('recipes/<str:pk>/',views.singleRecipe,name='single-recipe'),
    path('recipes-add/',views.addRecipe,name='add-recipe'),
    path('recipes-edit/<str:pk>/',views.editRecipe,name='edit-recipe'),
    path('recipes-delete/<str:pk>/',views.deleteRecipe,name='delete-recipe'),
]
