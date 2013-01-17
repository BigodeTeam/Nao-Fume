# coding=utf-8
import datetime
from django.http import HttpResponseRedirect, Http404
from django.views.generic.base import View
from django.conf import settings
from urllib import urlencode, urlopen
from urlparse import parse_qs
import json
from cigarette.models import Cigarette
from profiles.models import User
from django.template import RequestContext
from django.utils.encoding import force_unicode
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from profiles.utils import require_login
from social.wall import WallController

class Login(View):

    def get(self, request):

        args = dict(
            client_id=settings.FACEBOOK_APP_ID,
            redirect_uri=settings.FACEBOOK_URL_CALLBACK,
            scope="email,user_about_me,friends_about_me,user_hometown,publish_stream",
            state='454k4j54fijfs',
        )

        try:
            args['code'] = request.GET['code']
            args["client_secret"] = settings.FACEBOOK_APP_TOKEN
            response = parse_qs(urlopen("https://graph.facebook"
                                        ".com/oauth/access_token?" +
                                        urlencode(args)).read())
            access_token = response["access_token"][-1]
            profile = json.load(urlopen("https://graph.facebook.com/me?"
            + urlencode(dict(access_token=access_token))))
            f_friends = json.load(
                urlopen("https://graph.facebook.com/me/friends?fields=id&"
                + urlencode(dict(access_token=access_token, limit=0)))
            )

            try:
                user = User.objects.get(id=profile['id'])
                user.token = access_token
                user.save()
                request.session['fb_id'] = user.id
                request.session['token'] = access_token
                if user.meta == None:
                    return HttpResponseRedirect('/registrar/')

                return HttpResponseRedirect('/')
            except:
                user = User(
                    id = profile['id'],
                    token = access_token,
                    name = force_unicode(profile['name']),
                    email = profile['email'],
                    picture = 'http://graph.facebook'
                              '.com/%s/picture?type=large' % profile['id'],
                    username = profile.get('username', profile['id']),
                )
                user.save()

                friends_fb = [ int(i[u'id']) for i in f_friends['data']]

                for user_friend in User.objects.filter(id__in=friends_fb):
                    user_friend.friends.add(user)
                    user.friends.add(user_friend)

                user.save()
                return HttpResponseRedirect('/registrar/')

        except Exception, er:
            print er
            return HttpResponseRedirect('https://www.facebook'
                                        '.com/dialog/oauth?'+ urlencode(args))


class Home(View):
    def get(self, request):

        try:

            user_id = request.session.get('fb_id', False)
            user = User.objects.get(id=user_id)

            if user.meta == None:
                return HttpResponseRedirect('/registrar/')

            try:
                user.name = user.name.split(' ')[0]
            except: pass

            wall = WallController()


            RES = {
                'USER': user,
                "WALL": wall.get_public_wall(user, 0, 10),
                'CIGARETTES': Cigarette.objects.all()
            }
            return render_to_response(
                'home.tpl',
                RES,
                context_instance = RequestContext(request)
            )
        except Exception, er:
            print er
            return render_to_response(
                'landing.tpl',
                context_instance = RequestContext(request)
            )


@csrf_protect
def register(request,edit):

    from social.user_history import History

    try:
        user_id = request.session.get('fb_id', False)
        user = User.objects.get(id=user_id)
        if  user.meta != None and not edit:
            return HttpResponseRedirect('/')
        elif user.meta == None and edit:
            return HttpResponseRedirect('/registrar/')
    except:
        return HttpResponseRedirect('/login/')


    if request.POST:

        getdict = request.POST
        goal_number = int(getdict.get('goal-num'),10)
        goal_time = getdict.get('goal-time')


        if goal_time == 'week':
            goal = goal_number * 7
        elif goal_time == 'month':
            goal = goal_number * 30
        elif goal_time == 'year':
            goal = goal_number * 365
        else:
            goal = goal_number

        #só em dias por enquanto
        goal_date = datetime.datetime.now() + datetime.timedelta(days=+goal)

        user.privacy = getdict.get('privacy')
        user.meta = goal_date
        user.save()

        amount = int(getdict.get('amount'))
        if amount > 200:
            amount = 200

        user_data = {'user': user,
                     'amount': amount,
                     'cigarette': getdict.get('cigarette'),
                     'method': 'post'
        }

        history = History(user_data)

        history_id = history.save()
        return HttpResponseRedirect('/')




    from social.models import UserHistory
    from cigarette.models import Cigarette

    from django.core.cache import cache
    savings = cache.get('cache_saved')
    if not savings:

        from calc.stats import StatsView

        def return_saving_per_user(u):
            history = UserHistory.objects.filter(user=u).order_by('date')
            stats = StatsView.Stats(u, history)
            return stats.meta_sum_saved()

        
        savings = float(sum( [return_saving_per_user(u) for u in User.objects.all()]))
        cache.set('cache_saved', savings, 3600)


    users = User.objects.filter(privacy=2).exclude(meta=None).order_by('-created')[:7]
    total_users = User.objects.count()
    cigarettes = Cigarette.objects.all()
    total_stop_users = UserHistory.objects.values('user').distinct().filter(amount=0).count()


    RES = {
        'EDIT': edit,
        'USER': user,
        'USERS': users,
        'TOTAL_USERS': total_users,
        'TOTAL_STOP_USERS': total_stop_users,
        'SAVINGS': "%.02f" % savings,
        'CIGARETTE': cigarettes
    }

    if edit:
        RES['goal_time'] = 'day'
        RES['goal_date'] = (user.meta - datetime.date.today()).days
        if RES['goal_date'] % 7 == 0:
            RES['goal_date'] = RES['goal_date']/7
            RES['goal_time'] = 'week'
        if RES['goal_date'] % 30 == 0:
            RES['goal_date'] = RES['goal_date']/30
            RES['goal_time'] = 'month'
        if RES['goal_date'] % 365 == 0:
            RES['goal_date'] = RES['goal_date']/365
            RES['goal_time'] = 'year'
        
        history = History({'user': user, 'method':'get'})
        last_history = history.get_last_history()

        RES['amount'] = last_history.amount
        RES['privacy'] = user.privacy
        RES['cigarette_id'] = last_history.cigarette.id

    return render_to_response(
        'register.tpl',
        RES,
        context_instance = RequestContext(request),
    )


def profile(request, nickname):


    try:
        profile = User.objects.filter(username=nickname).exclude(meta=None)[0]
    except Exception, err:
        raise Http404

    user_logged_id = request.session.get('fb_id', False)

    is_friend = profile.friends.filter(id=user_logged_id).count()

    is_owner = False
    if profile.id==user_logged_id:
        is_owner = True
        privacy = '1,2,3'
    elif is_friend:
        privacy = '2,3'
    else:
        privacy = '2'


    try:
        profile.name = profile.name.split(' ')[0]
    except: pass

    wall = WallController()

    

    RES = {
        'USER': profile,
        "WALL": wall.get_single_user_wall(profile,privacy, 0, 10),
        'IS_OWNER': is_owner,
        'IS_FRIEND': is_friend
    }

    return render_to_response(
        'profile.tpl',
        RES,
        context_instance = RequestContext(request)
    )


@require_login
def friends(request):

    try:
        request.USER.name = request.USER.name.split(' ')[0]
    except: pass
    RES = {
        'USER': request.USER,
        'CIGARETTES': Cigarette.objects.all()
    }
    return render_to_response(
        'friends.tpl',
        RES,
        context_instance = RequestContext(request)
    )


def about(request):

    return render_to_response(
        'about.tpl',
        context_instance = RequestContext(request)
    )
def privacy(request):


    return render_to_response(
        'privacy.tpl',
        context_instance = RequestContext(request)
    )
def midia(request):

    return render_to_response(
        'midia.tpl',
        context_instance = RequestContext(request)
    )
@require_login
def logout(request):
    for sesskey in request.session.keys():
        del request.session[sesskey]

    return HttpResponseRedirect('/')

@require_login
def excluir(request):
    for sesskey in request.session.keys():
        del request.session[sesskey]
    request.USER.delete()

    return HttpResponseRedirect('/')
