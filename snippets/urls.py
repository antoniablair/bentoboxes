from django.conf.urls import url
from snippets import views

# Needs better error handling for if json is malformed or request is made with method view doesn't handle

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),]