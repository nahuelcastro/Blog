from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.permissions import IsOwnerOrReadAndCreateOnly

from comments.models import Comment
from comments.api.serializers import CommentSerializer

class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['-created_at', '-id']
    filterset_fields = ['post__title', 'post__slug', 'post__category__slug', 'post__user__username', 'post__user__email']

