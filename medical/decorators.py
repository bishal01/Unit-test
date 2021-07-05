from django.shortcuts import redirect,render
from django.http import HttpResponse


def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return render(request,'error.html')


        return wrapper_func
    return decorators

def checkgroup(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group =='doctor':
                return view_func(request,*args,**kwargs)
            if group=='patient':
                return redirect('patient')


        return wrapper_func

