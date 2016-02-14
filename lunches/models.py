from django.conf import settings
from django.db import models
from recipes.models import Recipe
from django.utils import timezone

# A lunch has many foods
# A food may have a recipe (i.e. a sandwich)
# A recipe has many ingredients
# A lunch can be labeled with any of the following if desired: Featured, Healthy, Cheap, Veggie, Vegan, Easy, Fast, Fun
# A recipe is in a category (i.e. Bento, Sandwiches, Soups, etc)
# A lunch can have be tagged with keywords that can be used for search

class Food(models.Model):
    name = models.CharField(max_length=200, default='apple')
    recipe = models.ForeignKey(Recipe, blank=True)


class Lunch(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=400, default='My lunch')
    tagline = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    is_featured = models.BooleanField(default=False)
    foods = models.ManyToManyField(Food, related_name='lunches')

    def __unicode__(self):
        return self.title


