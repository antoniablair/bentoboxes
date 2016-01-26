from members.models import Member
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# ModelSerializer is a shortcut for creating serializer classes -
    # an automatically determined set of fields
    # simple default implentations for create() and update() methods
#
# Member = django.contrib.auth.get_user_model()

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class MemberSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    # class Meta:
    #     model = Member
    #     fields = ('id', 'username', 'snippets')
