# -*- coding: utf-8 -*-
from history_short import HistoryShort
from post_short import PostShort
from django.views.generic.base import View
from django.http import HttpResponseNotFound

class ShortenerView(View):

    def get(self, request, code, type):
        
        if not code:
            return HttpResponseNotFound

        if type == "post":
            post = PostShort(code)
            return post.give_me_what_i_want()
             
        elif type == "history":
            history = HistoryShort(code)
            return history.give_me_what_i_want()
