from rest_framework import serializers
from models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):

        return Post.objects.create(**validated_data)
