from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Ingredients, i.e., one recipe might call for 2 slices of bread, etc
# Ingredient needs to be moved inside Recipe???
class Ingredient(models.Model):
    quantity = models.DecimalField(max_digits=5, decimal_places=2,
                                   default='1',
                                   blank=True, null=True)
    measurement = models.CharField(max_length=200, default='pinch', blank=True, null=True)
    name = models.CharField(max_length=200, default='salt')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    # Should there be more than one author?
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=400)
    text = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    # likes = models.ManyToManyField(Like, related_name='likes')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # __str__ method returns a string of the Post title
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    recipes = models.ManyToManyField(Recipe, related_name='recipes')

    def __str__(self):
        return self.title


class Like(models.Model):
    creator = models.ForeignKey('auth.user')
    created_date = models.DateTimeField(default=timezone.now)
    recipe = models.ForeignKey(Recipe, related_name='likes')

    def __str__(self):
        return self.recipe.title
