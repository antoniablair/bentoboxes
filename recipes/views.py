from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.utils import timezone
from .forms import LikeForm
from .models import Recipe
from django.template import RequestContext


def recipes_list(request):
    recipes = Recipe.objects.filter(published_date__lte=timezone.now()).order_by(
        'published_date').reverse()

    return render(request, 'recipes/recipe_list.html', {'recipes': recipes })


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def like_recipe(request, pk):
    context = RequestContext(request)
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        form = LikeForm(request.POST)

        if form.is_valid():
            like = form.save(commit=False)
            like.recipe = recipe
            like.creator = request.user
            like.created_date = timezone.now()
            like.save()
            return redirect('recipes.views.recipe_detail', pk=recipe.pk)
        else:
            print form.errors

    else:
        form = LikeForm()
    # Bad form or form details, or no form supplied
    # Render the form with error messages (if any)
    return render_to_response('recipes/like_recipe.html', {'form': form}, context)
