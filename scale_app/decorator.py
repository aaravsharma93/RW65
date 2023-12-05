# from functools import wraps
# from django.http import HttpResponseRedirect

# def my_login_required(function):
#     def wrapper(request, *args, **kw):
#         user=request.session.user  
#         if not user:
#             return HttpResponseRedirect('/authenticate/')
#         else:
#             return function(request, *args, **kw)
#     return wrapper

from django.utils.decorators import method_decorator

def my_login_required(function_decorator):
    """Convert a function based decorator into a class based decorator usable
    on class based Views.

    Can't subclass the `View` as it breaks inheritance (super in particular),
    so we monkey-patch instead.
    """

    def simple_decorator(View):
        View.dispatch = method_decorator(function_decorator)(View.dispatch)
        return View

    return simple_decorator