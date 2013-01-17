import datetime
from django.db import models
from django.conf import settings
from django.db.models.query_utils import Q


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    picture = models.URLField(max_length=255)
    meta = models.DateField(null=True, default=None)
    privacy = models.CharField(max_length=1, choices=settings.PRIVACY, default='2')
    friends = models.ManyToManyField('self', null=True, blank=True)
    username = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    __unicode__ = lambda self: self.name

    picture_square = lambda self: 'http://graph.facebook.com/%d/picture?type=square' % self.id

    @property
    def history(self):
        from social.user_history import History
        return History({
            'method':'get',
            'user': self
        }).get_last_history()

    def friends_privacy(self):
        return self.friends.exclude(Q(meta=None) | Q(privacy=1))

    def m(self):
        try:
            time = (self.meta - datetime.date.today()).days
            year = time/365
            time = time % 365
            month = time/30
            day = time % 30
            return {
                'YEAR': year,
                'MONTH': month,
                'DAY': day,
            }
        except:
            return False

    def primary_name(self):
        try:
            return str(self.name.split(' ')[0])
        except:
            return str(self.name)


