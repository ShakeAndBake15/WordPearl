from rest_framework import serializers
from .models import Pearl

class PearlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pearl
        fields = ['id', 'title', 'body', 'username', 'created_at', 'votes']