from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib import messages
from .utils import searchRecipes, paginateRecipes
from .forms import RecipeForm, ReviewForm
from django.contrib.auth.decorators import login_required

def showRecipes(request):
    recipes, searchQuery = searchRecipes(request)    
    custom_range, recipes = paginateRecipes(request,recipes,6)

    context = {'recipes':recipes,'searchQuery':searchQuery,'custom_range':custom_range}
    return render(request,'recipes.html',context=context)


def singleRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.recipe = recipe
        review.owner = request.user.profile
        review.save()
        recipe.getVoteCount
        messages.success(request,"Review added!")
        return redirect('single-recipe',pk=recipe.id) 

   
    context = {'recipe':recipe,'form':form}
    return render(request,'single-recipe.html',context=context)


@login_required(login_url='login')
def addRecipe(request):
    print(request.POST)
    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm(request.POST,request.FILES)

        if form.is_valid():
            recipe: Recipe = form.save(commit=False)
            recipe.owner = request.user.profile

            recipe.save()
            form.save_m2m()
            return redirect('account')
        
    context = {'form':form}
    return render(request,'recipe-form.html',context=context)

@login_required(login_url='login')
def editRecipe(request,pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)

    if request.method == "POST":
        form = RecipeForm(request.POST,request.FILES,instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('account')
        
    context = {'form':form}
    return render(request,'recipe-form.html',context=context)


@login_required(login_url='login')
def deleteRecipe(request,pk):
    recipe = Recipe.objects.get(id=pk)

    if request.method == "POST":
        recipe.delete()

        return redirect('account')
        
    context = {'recipe':recipe}
    return render(request,'recipe-delete.html',context=context)
    
