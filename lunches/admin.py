from django.contrib import admin
from .models import Lunch, Food, LunchImage

class LunchImageInline(admin.TabularInline):
    model = LunchImage
    fk_name = 'lunch'

class LunchAdmin(admin.ModelAdmin):
    inlines = [ LunchImageInline, ]


admin.site.register(Lunch, LunchAdmin)