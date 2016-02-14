from django.conf.urls import url, static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^profile/(?P<name>\w+)/$', views.member_profile, name='member_profile'),
]
#
# url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),