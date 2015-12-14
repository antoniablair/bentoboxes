from django.conf.urls import url
# adding support for format suffixes to api endpoints (will create url that explicity refers to
# a given format
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

# Needs better error handling for if json is malformed or request is made with method view doesn't handle

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
