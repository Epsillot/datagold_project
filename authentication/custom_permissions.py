from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_admin

class IsAnonymous(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_anonymous

class IsUser(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_user