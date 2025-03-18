from rest_framework import permissions

class IsPetOwner(permissions.BasePermission):
    """
    Проверяет, что пользователь является владельцем животного/клиентом.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        return request.user.status == 'client'
    
class IsPetSitter(permissions.BasePermission):
    """
    Проверяет, что пользователь является исполнителем.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        return request.user.status == 'petsitter'