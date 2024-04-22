from .models import Recipe, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


def searchRecipes(request):
    searchQuery = request.GET.get("search_query","")

    matchingTags = Tag.objects.filter(name__icontains=searchQuery)

    recipes = Recipe.objects.distinct().filter(
        Q(name__icontains=searchQuery) |
        Q(owner__username__icontains=searchQuery) |
        Q(intro__icontains=searchQuery) |
        Q(tags__in=matchingTags)
    )

    return recipes, searchQuery


def paginateRecipes(request,recipes,results):

    pageNumber = request.GET.get('page')
    paginator = Paginator(recipes,results)

    try:
        recipes = paginator.page(pageNumber)
    except PageNotAnInteger:
        pageNumber = 1
        recipes = paginator.page(pageNumber)
    except EmptyPage:
        pageNumber = paginator.num_pages
        recipes = paginator.page(pageNumber)

    leftIndex = (int(pageNumber) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(pageNumber) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex,rightIndex)

    return custom_range, recipes