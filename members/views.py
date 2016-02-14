from django.shortcuts import render
from .models import Member

# Iexact makes query case insensitive
def member_profile(request, name):
    member = Member.objects.filter(first_name__iexact=name).first()
    return render(request, 'profile.html', {'member': member})



