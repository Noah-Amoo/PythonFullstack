from fastapi import Depends, HTTPException, status

from app.dependencies.auth import get_current_user
from app.models.user import User, UserRole

from app.core.exceptions import PermissionDeniedException


def require_roles(*roles: UserRole):

    async def role_checker(
        current_user: User = Depends(get_current_user),
    ):

        if current_user.role not in roles:
            raise PermissionDeniedException()

        return current_user

    return role_checker