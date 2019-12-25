from django.db import models


class Sale(models.Model):
    date = models.DateField()
    total_buy = models.FloatField(verbose_name='Total Purchase')
    total_sell = models.FloatField(verbose_name='Total Sales')

    def __str__(self):
        return '<Sale: date: %s, total_buy: %f, total_sell: %f>' % (self.date, self.total_buy, self.total_sell)

    class Meta:
        db_table = 'sale'
