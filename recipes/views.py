from django.shortcuts import render
from .models import Recipe


def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes })
