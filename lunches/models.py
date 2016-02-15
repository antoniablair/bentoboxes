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
    needs_instructions = models.BooleanField(default=False, help_text=(u'Does this lunch addition require '
                                                                       u'instructions (e.g., a sandwich?) '
                                                                       u'Choose yes or no.'))
    recipe = models.ForeignKey(Recipe, blank=True, null=True, help_text=(u'If instructions are necessary, include '
                                                                         u'the recipe here.'))

    def __unicode__(self):
        return self.name


class Lunch(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=400, default='My lunch')
    tagline = models.TextField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    is_featured = models.BooleanField(default=False)
    foods = models.ManyToManyField(Food, related_name='lunches', blank=True)

    def __unicode__(self):
        return self.title


class LunchImage(models.Model):
    lunch = models.ForeignKey(Lunch, related_name='images')
    image = models.ImageField(upload_to='images/')

    def __unicode__(self):
        return self.lunch.title


