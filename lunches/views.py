from django.shortcuts import render, get_object_or_404, redirect
from .models import Lunch
from django.utils import timezone


def lunches(request):
    lunches = Lunch.objects.all()
    return render(request, 'lunches/lunches.html', {'lunches': lunches })
