from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
            if view.action in ['list', 'retrieve']:
                return request.user.is_authenticated 
            return request.user.is_authenticated and request.user.groups.filter(name='Admin').exists()

class IsAdminOrTech(BasePermission):
    def has_permission(self, request, view):
            if view.action in ['list', 'retrieve']:
                return request.user.is_authenticated 
            return request.user.is_authenticated and request.user.groups.filter(name__in=['Admin', 'Tech']).exists()

    
    