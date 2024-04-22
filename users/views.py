from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from catalogue.models import Profile
from .forms import CustomUserForm, ProfileForm

def userLogin(request):

    if request.user.is_authenticated:
        return redirect("recipes")
    
    if request.method == "POST":
        username: str = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            userProfile = User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist!")
        else:

            userProfile = authenticate(request,username=username,password=password)

            if userProfile:
                login(request,userProfile)
                return redirect('recipes')
            else:
                messages.error(request,"Wrong login or password!")

    return render(request,'login.html')

def userLogout(request):
    logout(request)
    messages.info(request,"User was logged out!")
    return redirect('login')

def userRegister(request):

    if request.user.is_authenticated:
        return redirect("recipes")
    
    form = CustomUserForm()

    if request.method=="POST":
        form = CustomUserForm(request.POST)

        if form.is_valid():
            user: User = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request,"New account has been created!")

            login(request, user)
            return redirect('account')
        
        else:
            messages.error(request,"An error has occured during registration") 

    context = {'form':form}
    return render(request,"register.html",context=context)


@login_required(login_url='login')
def account(request):
    profile: Profile = Profile.objects.get(id=request.user.profile.id)
    recipes = profile.recipes.all()

    context = {'profile':profile,'recipes':recipes}
    return render(request,'account.html',context=context)



@login_required(login_url='login')
def editAccount(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)

        if form.is_valid():
            form.save()   

            return redirect('account')


    context = {'form':form}
    return render(request,'edit-account.html',context=context)

    