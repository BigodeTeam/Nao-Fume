# -*- coding: utf-8 -*-
from social.models import UserHistory
from cigarette.models import Cigarette
from django.db import IntegrityError


class History(object):

    def __init__(self, user_data=None):
        if not user_data or not isinstance(user_data, dict):
            raise Exception("Invalid user data")
        
        if user_data['method'] == "get":
            self.data = {'user': user_data['user']}
        else:
            self.data = {'user': user_data['user'],
                         'cigarette': Cigarette.objects.get(
                                      id=user_data['cigarette']
                         ),
                         'amount': user_data.get('amount')}
        self.history = None

    def get(self,limit=40, order='-id'):
        return UserHistory.objects.filter(
            user=self.data['user']).order_by(order)[:limit]

    def get_message_history_prev(self, last_history):

        try:
            prev_history = UserHistory.objects.filter(user=self.data['user']).exclude(pk=last_history.pk).order_by('-date')[0]
        except :
            prev_history = False


        RES = {
            "status":0,
            "amount":0,
            "p":0,
            "days":0
        }

        if prev_history:
            last_history.amount = int(last_history.amount)
            prev_history.amount = int(prev_history.amount)
            RES['days'] = (last_history.date - prev_history.date).days


            if last_history.amount == 0:
                RES['status'] = 2
                RES['amount'] = 0
                RES['p'] = self.data['user'].username
            elif last_history.amount>prev_history.amount:
                RES['status'] = 1
                RES['amount'] = last_history.amount - prev_history.amount
                RES['p'] = 100.0 - prev_history.amount*100.0/last_history.amount
            elif last_history.amount<prev_history.amount:
                RES['status'] = -1
                RES['amount'] =  prev_history.amount - last_history.amount
                RES['p'] = 100.0 - last_history.amount*100.0/prev_history.amount
            else:
                RES['status'] = 0
                RES['amount'] = 0
                RES['p'] = 0

        return self.get_message_system(RES['status'],RES['p'],RES['days'])

    def get_message_system(self, status, data, days):

        if status == 2:
            m = ' parou de fumar! Parabens pela força de vontade! Acesse as <a href="/%s/estatistica/">estatísticas</a> e veja como foi seu progresso e a economia gerada em tempo real!' % str(data)

        elif status>0:
            if days>1:
                m = ' aumentou seu consumo em %.02f%% em relação a marca estabelecida a %s dias! Vamos lá, você consegue mudar essa situação!' % (data,days)
            else:
                m = ' aumentou seu consumo em %.02f%%! Vamos lá, você consegue mudar essa situação!' % (data)

        elif status<0:
            if data <50:
                if days>1:
                    m = ' diminuiu seu consumo em %.02f%% em relação a marca estabelecida a %s dias! Parabéns, continue assim :)' % (data,days)
                else:
                    m = ' diminuiu seu consumo em %.02f%%! Parabéns, continue assim :)' % (data)
            else:
                if days>1:
                    m = ' diminuiu seu consumo em %.02f%% em relação a marca estabelecida a %s dias! Uow!!! Muito bom!!' % (data,days)
                else:
                    m = ' diminuiu seu consumo em %.02f%%! Uow!!! Muito bom!!' % (data)
        else:
            m = ' atualizou seus dados de consumo.'

        return m


    def get_history_by_id(self, id):
        return UserHistory.objects.get(pk=id)

    def get_last_history(self):
        return UserHistory.objects.filter(
            user=self.data['user']).order_by('-date')[0]

    def save(self):
        """ Insert new user history """
        try:
            self.history = UserHistory(user = self.data['user'],
                                       amount = self.data['amount'],
                                       cigarette = self.data['cigarette'])
            self.history.save()
                
            return self.history
        except IntegrityError, e:
            self.history = UserHistory.objects.filter(
                           user=self.data['user']).order_by('-id')[0]
            self.history.cigarette = self.data['cigarette']
            self.history.amount = self.data['amount']
            self.history.save()
            return self.history
        except:
            raise Exception("Failed on save User History")
