from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.api.permissions import IsAdminOrReadOnly

from posts.models import Post
from posts.api.serializers import PostSerializer

class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'slug', 'category__slug', 'user__username', 'user__email']

