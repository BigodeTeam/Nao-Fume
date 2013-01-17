from profiles.models import User

def logged(request):
    try:
        user = User.objects.get(id=request.session['fb_id'])
        is_logged = True
    except Exception, e:
        user = False
        is_logged = False

    return {
        'IS_LOGGED': is_logged,
        'LOGGED_USER': user
    }