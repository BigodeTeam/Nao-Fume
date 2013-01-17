# coding=utf-8
# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson
from django.utils.encoding import force_unicode
from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import View
from profiles.models import User
from shortener.post_short import PostShort
from social.models import Wall
from social.user_history import History
from social.wall import Post, WallController
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from profiles.utils import require_login
from django.core import serializers
from json import dumps

class HistoryView(View):

    def get(self, request):

        try:
            profile = User.objects.filter(
                username=request.GET['username']
            ).exclude(meta=None)[0]
        except Exception, err:
            raise Http404

        user_data = {'user': profile,
                     'method': "get"}
        history = History(user_data)
        return HttpResponse(serializers.serialize("json",
            history.get(order='date')))

    @method_decorator(require_login)
    def post(self, request):
        getdict = request.POST



        user_data = {'user': request.USER,
                     'amount': getdict.get('amount'),
                     'cigarette': getdict.get('cigarette'),
                     'method': "post"}

        history = History(user_data)
        last_history = history.save()

        HistoryCtrl = History({'user': request.USER,
                               'method': "get"})

        msg = HistoryCtrl.get_message_history_prev(last_history)
        post = Post(request.USER, msg, 2,2)
        post = post.save()

        if int(getdict.get('post_fb')) > 0:
            from social.publish import Publish
            fb = Publish(request.USER)
            url = PostShort(post.pk)
            try:
                fb.post(request.USER.primary_name()+post.message, url.url_post())
            except Exception, er: pass

        RES = {
            'status': True,
            'message': post.message,
            'id': post.id,
            'type': post.type,
            'username': post.user.username,
            'picture': post.user.picture_square()
        }

        return HttpResponse(simplejson.dumps(RES), mimetype='text/json')

class WallView(View):

    @method_decorator(require_login)
    def get(self, request):
        wall = WallController()
        if request.GET.get('page','home') != 'profile':
            wall = wall.get_public_wall(request.USER)
        else:
            try:
                profile = User.objects\
                            .filter(username=request.GET['username'])\
                            .exclude(meta=None)[0]
            except Exception, err:
                raise Http404
            is_friend = profile.friends.filter(id=request.USER.id).count()
            if profile.id==request.USER.id:
                privacy = '1,2,3'
            elif is_friend:
                privacy = '2,3'
            else:
                privacy = '2'
            wall = wall.get_single_user_wall(profile,privacy)

        wall = wall.filter(id__lt=request.GET['id'])

        json = {
            'total': wall.count(),
            'data': []
        }

        for i in wall[:10]:
            json['data'].append({
                'id': i.id,
                'message': i.message,
                'type': i.type,
                'username': i.user.username,
                'picture': i.user.picture_square(),
                'is_owner': i.user == request.USER
            })
        return HttpResponse(simplejson.dumps(json), mimetype='text/json')

    @method_decorator(require_login)
    def post(self, request):

        try:
            msg = request.POST['post']
            post_fb = request.POST['post_fb']
            post = Post(request.USER, msg.encode('utf-8'), 2, 1)
            post = post.save()

            if int(post_fb) > 0:
                from social.publish import Publish
                fb = Publish(request.USER)
                url = PostShort(post.pk)
                try:
                    fb.post(post.message, url.url_post())
                except Exception, er: pass

        except Exception, er:
            print er
            return HttpResponse('{"status":false}', mimetype='text/json')

        RES = {
            'status': True,
            'message': post.message,
            'id': post.pk,
            'type': post.type,
            'username': post.user.username,
            'picture': post.user.picture_square()
        }

        return HttpResponse(simplejson.dumps(RES), mimetype='text/json')

    @method_decorator(require_login)
    def delete(self, request):

        try:
            wall = Wall.objects.get(id=request.GET['id'])
            if wall.user.id == request.USER.id:
                wall.delete()
            else: raise Exception('Usuario não é dono do post')
        except:
            return HttpResponse('{"status":false}', mimetype='text/json')

        return HttpResponse('{"status":true}', mimetype='text/json')


def post(request, nickname, id):
    RES = {'LOGGED': False}

    try:
        RES['POST'] = Wall.objects.get(user__username=nickname,id=id)
    except Exception, err:
        raise Http404

    try:
        RES['LOGGED'] = User.objects.get(id=request.session['fb_id'])
    except: pass

    return render_to_response(
        'post.tpl',
        RES,
        context_instance = RequestContext(request)
    )