from django.db import models


class Cigarette(models.Model):
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    picture = models.ImageField(blank=True, null=True, upload_to='pictures/')
    price = models.FloatField(blank=False)
    amount = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.name
