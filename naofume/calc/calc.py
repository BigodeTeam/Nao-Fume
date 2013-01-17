# -*- coding: utf-8 -*- 
from django.views.generic.base import View
from django.http import HttpResponse
from datetime import datetime
from json import dumps


class Calc(View):

    def get(self, request):

        http_get = self.check_GET(request.GET)
        if not http_get:
            return HttpResponse(dumps({'erro': "missing arguments"}))

        response = self.get_stats(http_get)

        return HttpResponse(dumps(response))

    def check_GET(self, get_dict):
        required = ['day', 'month', 'year', 'cigs', 'price', 'cig_box']
        
        keys = get_dict.keys()
        if len(required) != len(keys):
            return False
        
        for value in get_dict.values():
            if not value or len(value) == 0:
                return False        
            
        return get_dict

    def get_stats(self, http_get):
        date =  "%s-%s-%s" % (http_get['year'], http_get['month'], http_get['day'])
        date = datetime.strptime(date, "%Y-%m-%d")
        now = datetime.now()
        time = now - date
        cigs = int(http_get['cigs'], 10)
        price = float(http_get['price'].replace(',', '.'))
        cig_box = int(http_get['cig_box'])
        amount = time.days * cigs
        return {'lapsed_time': self.lapsed_time(time),
                'cig_amount': "Deixou de fumar %d cigarros" % amount,
                'saved': self.calculate_money(price, cig_box, amount)}


    def calculate_money(self, price, cig_box, amount):
        money = "%.2f" % (amount / cig_box * price)
        return "Economizou R$%s em compra de cigarros" % money


    def lapsed_time(self, time):
        days = (time.days, "dia", "dias")
        months = (days[0] / 30, "mês", "meses")
        years = (days[0] / 365, "ano", "anos")

        timeago = "está a %d %s sem fumar"
        if months[0] > 0 and months[0] < 12:
            return timeago % (months[0], months[1] if months==1 else months[2])
        elif years[0] > 0:
            return timeago % (years[0], years[1] if years==1 else years[2])
        else:
            return  timeago % (days[0], days[1] if days==1 else days[2])
            
