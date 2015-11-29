from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Recipe(models.Model):
    # Should there be more than one author?
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=400)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # __str__ method returns a string of the Post title
    def __str__(self):
        return self.title
