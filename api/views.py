from .models import Like
from rest_framework import serializers
from api.serializers import LikeSerializer

class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Likes to be viewed or edited.
    """
# Create your views here.
