from rest_framework import permissions

class IsSuperuserOrSelf(permissions.BasePermission):
    """
    Custom permission to allow superusers to view all users and
    allow users to view only themselves.
    """

    def has_permission(self, request, view):
        # Superusers can view all users
        if request.user.is_superuser:
            return True

        # Users can view only themselves
        return view.kwargs.get('pk') == str(request.user.id)
