from rest_framework. permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in 'GET':
            return True
        else:
            return request.user.is_staff
