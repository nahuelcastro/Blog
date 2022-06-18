from rest_framework import serializers
from comments.models import Comment
from users.api.serializers import UserSerializer
from posts.api.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    # post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'user', 'post']
        read_only_fields = ['id', 'created_at']


