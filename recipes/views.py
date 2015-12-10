from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Recipe


def recipes_list(request):
    recipes = Recipe.objects.filter(published_date__lte=timezone.now()).order_by(
        'published_date').reverse()

    return render(request, 'recipes/recipe_list.html', {'recipes': recipes })


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
