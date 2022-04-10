from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allow_users(allow_roles=[]):
    def decarator(view_func):
        def wrapper_func(request,*args,**kwargs):
            print("working",allow_roles)
            return view_func(request,*args,**kwargs)
        return wrapper_func
    return decarator


