from rest_framework import permissions

class IsApprovedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and approved
        return request.user.is_authenticated and request.user.user_is_approved
    

