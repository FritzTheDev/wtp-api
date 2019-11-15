from django.contrib.auth.models import User
from rest_framework.serializers import PrimaryKeyRelatedField

from .listing import Listing

class UserSerializer(serializers.ModelSerializer):
    snippets = PrimaryKeyRelatedField(many=True, queryset=Listing.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'listings']