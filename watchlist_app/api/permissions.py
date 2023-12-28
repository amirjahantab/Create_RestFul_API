from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    ''' This permission allows read-only access to all users, but only allows write access to admin users '''    
    def has_permission(self, request, view): 

        if request.method in permissions.SAFE_METHODS: # The request is authenticated as a user, or is a read-only request.
            return True
        else:
            return bool(request.user and request.user.is_staff)

        
class IsReviewUserOrReadOnly(permissions.BasePermission):
      
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # The request is authenticated as a user, or is a read-only request.
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff # The request is authenticated as a user, or is a read-only request.