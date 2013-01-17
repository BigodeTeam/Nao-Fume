import datetime
from django.db import models
from profiles.models import User
from cigarette.models import Cigarette
from naofume.settings import PRIVACY


class Wall(models.Model):

    TYPES = (
        ('1', 'user'),
        ('2', 'user_system'),
        ('3', 'system'),
        )


    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    type  = models.CharField(max_length=1, default=1,choices=TYPES)
    privacy = models.CharField(max_length=1, choices=PRIVACY)

class UserHistory(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    cigarette = models.ForeignKey(Cigarette)

    class Meta:
        unique_together = (("user", "date"),)

    def get_amount_economy_day(self):
        self.amount * self.cigarette

    def date_subs(self):
        if datetime.date.today() > self.date:
            status = 1
            time = (datetime.date.today() - self.date).days
        elif datetime.date.today() == self.date:
            time = 0
            status = 0
        else:
            time = (self.date - datetime.date.today()).days
            status = -1


        year = time/365
        time = time % 365
        month = time/30
        day = time % 30

        return {
            'STATUS':status,
            'YEAR': year,
            'MONTH': month,
            'DAY': day,
            }
