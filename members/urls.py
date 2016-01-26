from django.conf.urls import url, static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^tonia/$', views.member_profile, name='member_profile'),
]