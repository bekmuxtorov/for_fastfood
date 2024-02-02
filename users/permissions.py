from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if bool(user.is_authenticated and user.role == 'admin'):
            return True
        return False


class IsWaiter(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if bool(user.is_authenticated and user.role == 'waiter'):
            return True
        return False


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if bool(user.is_authenticated and user.role == 'customer'):
            return True
        return False
