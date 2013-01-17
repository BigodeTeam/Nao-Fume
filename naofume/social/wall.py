# -*- coding: utf-8 -*-
from profiles.models import User
from social.models import Wall
from django.db.models import Q


class WallController(object):

    def __init__(self, user=None):
        pass

    def get_post_by_id(self, id):
        return Wall.objects.get(pk=id)


    def get_posts_by_user(self, user, offset, limit):
        return Wall.objects.filter(user=user).order_by('-date')[offset:limit]


    def get_single_user_wall(self, user, privacy, offset=0, limit=0):
        return Wall.objects.filter(user=user,privacy__in=privacy).order_by('-date')

    def get_user_wall(self, user, offset=0, limit=0):
        #@todo posts friends + user . privacy != private
        return Wall.objects.filter(
            Q(
                user__in = user.friends.all().values_list('id', flat=True)


            )|Q( user = user)
        ).filter(privacy__gte=1).order_by('-date')


    def get_public_wall(self, user, offset=0, limit=0):
        #@todo posts . privacy == public
        return Wall.objects.filter(
            Q(
                user__in = user.friends.all().values_list('id', flat=True)


            )|Q( user = user)|Q(privacy=2)
        ).order_by('-date')


    def remove_post(self,id):
        post = self.get_post_by_id(id)
        post.remove()


    def edit_post_privacy(self, id, privacy):

        if privacy < 1 or privacy >3:
            return False

        post = self.get_post_by_id(id)

        if not post:
            return False

        post.privacy = privacy
        post.save()

        return True


class Post():

    def __init__(self, user, message, privacy, type):
        self.user = user
        self.message = message
        self.privacy = privacy
        self.type = type


    def validate(self):
        if self.privacy < 1 or self.privacy>3:
            return False

        if not self.message or len(str(self.message))<4:
            return False

        return True

    def save(self):
        if self.validate():
            post = Wall(user=self.user, message=self.message,
                privacy=self.privacy, type=self.type)
            post.save()
            return post
        else:
            raise Exception('Mensagem muito pequena')
