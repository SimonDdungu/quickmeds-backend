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

class UserAuth(BasePermission):
    def has_permission(self, request, view):
            if view.action in ['list']:
                return request.user.is_authenticated 
            return request.user.is_authenticated and request.user.groups.filter(name__in=['Admin']).exists()

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='admin').exists():
            return True
        return obj.id == request.user.id
    
    