from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.recipes_list, name='recipes_list'),
]
