from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'published', 'category', 'user', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
