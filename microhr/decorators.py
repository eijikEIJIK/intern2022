from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

from django.core.exceptions import PermissionDenied

def worker_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """Decorator for views that checks that the logged in user is a worker."""
    
    def check(user):
        if user.is_active and user.is_worker:
            return True
        else:
            raise PermissionDenied

    actual_decorator = user_passes_test(
        check, login_url=login_url, redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def company_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """Decorator for views that checks that the logged in user is a company"""

    def check(user):
        if user.is_active and user.is_company:
            return True
        else:
            raise PermissionDenied

    actual_decorator = user_passes_test(
        check, login_url=login_url, redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

