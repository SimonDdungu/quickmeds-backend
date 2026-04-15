from rest_framework.permissions import BasePermission   
    
class InventoryPermission(BasePermission):
    def has_permission(self, request, view):

        user = request.user
        
        if not request.user.is_authenticated:
            return False
        
        groups = user.groups.values_list('name', flat=True)

        if view.action in ['list', 'retrieve']:
            return True
        
        if view.action in ['create', 'update', 'partial_update']:
            return 'Admin' in groups or 'Tech' in groups

        return 'Admin' in groups
