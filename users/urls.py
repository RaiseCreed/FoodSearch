from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.userLogin,name="login"),
    path('register/',views.userRegister,name="register"),
    path('logout/',views.userLogout,name="logout"),
    path('account/',views.account,name='account'),
    path('account-edit/',views.editAccount,name="edit-account"),
]
