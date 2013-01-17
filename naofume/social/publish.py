import json
from urllib import urlopen, urlencode
from django.conf import settings

class Publish(object):
    args = dict(
        client_id=settings.FACEBOOK_APP_ID,
        access_token='',
        scope="email,user_about_me,friends_about_me,user_hometown,publish_stream",
        state='454k4j54fijfs',
    )

    def __init__(self, user):
        self.user = user
        self.args['access_token'] = user.token

    def post(self, message, link = False):
        self.args['message'] = message
        if link:
            self.args['link'] = link
        return json.load(urlopen(
            ("https://graph.facebook.com/%s/feed?" % self.user.id),
            data=urlencode(self.args)
        ))