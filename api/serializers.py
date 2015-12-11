from .models import Like
from rest_framework import serializers

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = ('creator', 'created_date', 'recipe')