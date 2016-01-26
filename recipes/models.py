from django.conf import settings
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import Member

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


# A lunch has many recipes
# A recipe has many ingredients
# A recipe be labeled with any of the following if desired: Featured, Healthy, Cheap, Veggie, Vegan, Easy, Fast, Fun
# A recipe is in a category (i.e. Bento, Sandwiches, Soups, etc)
# A recipe can have be tagged with keywords that can be used for search
# Ingredients

class Recipe(models.Model):
    # Should there be more than one author?
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=400)
    text = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
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


# class Label(models.Model):
#     name = models.CharField(max_length=200)
#     recipes = models.ManyToManyField(Recipe)
#     creator = models.ManyToManyField(Member, related_name='labels')


class Category(models.Model):
    title = models.CharField(max_length=200)
    recipes = models.ManyToManyField(Recipe, related_name='categories')

    def __str__(self):
        return self.title


class Like(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(default=timezone.now)
    recipe = models.ForeignKey(Recipe, related_name='likes')

    def __str__(self):
        return self.recipe.title
