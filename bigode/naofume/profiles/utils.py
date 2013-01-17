from functools import wraps
from django.http import HttpResponseRedirect
from profiles.models import User

def require_login(func):

    @wraps( func )
    def login( request, *args, **kwds ):
        user = request.session.get('fb_id', False)
        try:
            user = User.objects.get(id=user)
        except:
            return HttpResponseRedirect('/login/')

        request.USER = user

        if user.meta == None:
            return HttpResponseRedirect('/registrar/')


        return func(request, *args, **kwds)

    return login

