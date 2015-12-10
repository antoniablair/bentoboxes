from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.recipes_list, name='recipes_list'),
    url(r'^recipe/(?P<pk>[0-9]+)/$', views.recipe_detail,
        name='recipe_detail'),
    # url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove,
    # name='comment_remove'),
]
