from rest_framework import serializers

from .models import Poodle

class PoodleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poodle
        fields = [
            'id', 'author', 'title', 'created_at'
        ]