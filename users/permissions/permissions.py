from rest_framework.permissions import BasePermission   
    
class UserPermission(BasePermission):
    def has_permission(self, request, view):

        user = request.user
        
        if not request.user.is_authenticated:
            return False
        
        groups = user.groups.values_list('name', flat=True)


        if view.action in ['list', 'retrieve', 'create']:
            return 'Admin' in groups or 'Tech' in groups

        return 'Admin' in groups
    
class RolePermission(BasePermission):
    def has_permission(self, request, view):

        user = request.user
        
        if not request.user.is_authenticated:
            return False
        
        groups = user.groups.values_list('name', flat=True)


        if view.action in ['list', 'retrieve']:
            return 'Admin' in groups or 'Tech' in groups

        return 'Admin' in groups