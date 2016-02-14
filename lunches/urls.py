from django.conf.urls import url, static
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.lunches, name='lunches'),
]

