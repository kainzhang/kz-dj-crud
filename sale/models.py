from django.db import models

class Sale(models.Model):
    date = models.DateField()
    total_buy = models.FloatField()
    total_sell = models.FloatField()

    def __str__(self):
        return '<date: %s, Profit: %f>' % (self.date, self.profit)
