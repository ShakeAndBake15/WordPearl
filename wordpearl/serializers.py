from rest_framework import serializers
from .models import Pearl, Oyster

class PearlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pearl
        fields = ['id', 'title', 'body', 'username', 'created_at', 'votes']

class OystersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oyster
        fields = ['id', 'points', 'password', 'username', 'avatar_url']