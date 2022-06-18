from rest_framework. permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in 'GET':
            return True
        elif request.method in 'POST':
            return request.user.is_authenticated
        else:
            id_comment = view.kwargs['pk']
            comment = Comment.objects.get(pk=id_comment)
            return request.user == comment.user
