from django.core.exceptions import PermissionDenied
from functools import wraps

def staff_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            raise PermissionDenied("У вас немає прав для доступу до цієї сторінки.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view