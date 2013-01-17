# -*- coding: utf-8 -*-
from profiles.models import User
from social.models import UserHistory
from social.user_history import History
from cigarette.models import Cigarette

from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime
from datetime import date,timedelta
from json import dumps
from django.utils.decorators import method_decorator
from profiles.utils import require_login
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext

class StatsView(View):
    """ Módulo de estatísticas de usuário """


    @method_decorator(require_login)
    def get(self, request, nickname=None, method=None):

        if not method:
            return HttpResponseRedirect("/")

        if not nickname:
            user = request.USER
        else:
            user = get_object_or_404(User, username=nickname)

        if method == "user":
            return self.user_stats_page(request, user)

        history = UserHistory.objects.filter(user=user).order_by('date')

        stats = self.Stats(user, history)
        stats.meta_analisys()

        response_json = dumps(stats.get_stats(), cls=DjangoJSONEncoder)

        return HttpResponse(response_json, mimetype="application/json")

    def user_stats_page(self, request, user):

        try:
            user.name = user.name.split(' ')[0]
        except:
            user.name = user.name

        RES = {'USER': user,
               'CIGARETTES': Cigarette.objects.all()}

        return render_to_response('stats.tpl', RES,
               context_instance = RequestContext(request))

    class Stats():
        
        def __init__(self, user, history):
            self.meta = user.meta
            self.name = user.name
            self.history = history
            # list com registros de histórico tratados
            self.stats = list()
            self.data_parser()

        def get_stats(self):
            if not hasattr(self, 'stats'):
                self.meta_analisys()
            return self.stats[len(self.stats)-6:len(self.stats)]

        def data_parser(self):
            first_mark = True
            base_date = date.today()

            if len(self.history) == 1:
                self.single_data_parser()
            else:
                for hist in self.history:
                    #o primeiro loop nao conta pois a economia é a diferenca entre 2 marcasx
                    if first_mark:
                        first_mark = False
                        continue

                    date_diff = (base_date - hist.date)
                    saved_money =  self.calculate_money(hist, date_diff.days * hist.amount)
                    if date_diff.days == 0:
                        date_diff = date_diff + timedelta(+1)

                    self.stats.append({'price': hist.cigarette.price,
                                       'cigs': hist.amount,
                                       'box_amount': hist.cigarette.amount,
                                       'date': hist.date.strftime("%d/%m/%Y"), 
                                       'days': date_diff.days,
                                       'amount': date_diff.days * hist.amount,
                                       'saved': "%.2f" % saved_money,
                                       'avg': "%.2f" % self.avarage(saved_money, date_diff.days)})

        def single_data_parser(self):
            hist = self.history[0]
            date_diff = (date.today() - hist.date)
            self.stats.append({'price': hist.cigarette.price,
                               'cigs': hist.amount,
                               'box_amount': hist.cigarette.amount,
                               'date': hist.date.strftime("%d/%m/%Y"), 
                               'days': date_diff.days,
                               'amount': date_diff.days * hist.amount,
                               'saved': self.calculate_money(hist, 
                                        date_diff.days * hist.amount)})

        def meta_analisys(self):
            analisys = dict()
            

            if len(self.history) > 1:
                money_avg = self.daily_money_avarage()
                saved = self.saved_money()
                not_smoked = self.not_smoked()
                analisys['global_avg'] = {'value': money_avg,
                                          'msg': "Foram economizados R$%.2f por dia" % money_avg}
                analisys['saved'] = {'value': saved,
                                     'msg': "Foram economizados R$%.2f em compra de cigarros" % saved }
                analisys['not_smoked'] = {'value': not_smoked,
                                          'msg': "Deixou de fumar %d cigarros" % not_smoked}

            self.stats.append({'analisys': analisys})

        def meta_sum_saved(self):
            return round(sum([float(stat['saved']) for stat in self.stats]), 2)

        def remaining_time(self):
            date_diff = self.meta - date.today()
            return "Faltam %d dia(s) para alcançar a meta (%s)" % (date_diff.days, self.meta.strftime("%d/%m/%Y"))

        def daily_money_avarage(self):
            daily_money = [float(stat['avg']) for stat in self.stats]
            return round(sum(daily_money)/len(daily_money), 2)


        def calculate_money(self, hist, amount):
            return round((hist.cigarette.price / hist.cigarette.amount) * amount, 2)

        def avarage(self, money, days):
            return round(money / days, 2)

        def saved_money(self):
            saved_money = [float(stat['saved']) for stat in self.stats]
            return round(sum(saved_money), 2)

        def not_smoked(self):
            amount = [int(stat['amount']) for stat in self.stats]
            return round(sum(amount),2)

#        def stat_calculation(self):
#            min_date = min([stat['date'] for stat in self.stats if stat['date'] < self.meta])])
#            days = (self.meta - min_date).days
#            before_stat = None
#            for stat in self.stats:
                










