# -*- coding: utf-8 -*- 
from social.user_history import History
from django.http import HttpResponseRedirect

class HistoryShort():
    """ Encurtador de url de Post """

    NAOFUME_URL = "http://naofu.me/h/%s"

    def __init__(self, code):
        print type(code)
        if isinstance(code, basestring):
            self.code = int(code, 16)
            self.what_i_want = "history"
        else:
            self.code = "%x" % int(code)
            self.what_i_want = "url"

    def give_me_what_i_want(self):
        if self.what_i_want == "history":
            return self.get_history()
        return self.url_history()

    def url_history(self):
        return self.NAOFUME_URL % self.code

    def get_history(self):
        try:
            history = History().get_history_by_id(self.code)
            return HttpResponseRedirect("/%s/historico/%d/" % (history.user.username, history.pk))
        except:
            return HttpResponseRedirect("/")
