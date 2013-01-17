# -*- coding: utf-8 -*- 
from social.wall import WallController
from django.http import HttpResponseRedirect

class PostShort():
    """ Encurtador de url de Post """

    NAOFUME_URL = "http://naofu.me/p/%s"

    def __init__(self, code):

        if isinstance(code, basestring):
            self.code = int(code, 16)
            self.what_i_want = "post"
        else:
            self.code = "%x" % int(code)
            self.what_i_want = "url"

    def give_me_what_i_want(self):
        if self.what_i_want == "post":
            return self.get_post()
        return self.url_post()

    def url_post(self):
        return self.NAOFUME_URL % self.code

    def get_post(self):
        try:
            post = WallController().get_post_by_id(self.code)
            return HttpResponseRedirect("/%s/%d/" % (post.user.username, post.pk))
        except:
            return HttpResponseRedirect("/")


