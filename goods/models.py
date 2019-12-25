from django.db import models


class Goods(models.Model):
    CATE_CHOICES = (
        (1, 'Food'), (2, 'Drink'), (3, 'Fruit'),
        (4, 'Daily Supply'), (5, 'Electronic'),
    )
    name = models.CharField(max_length=50)
    mfr = models.CharField(max_length=300, verbose_name='Manufacturer')
    category = models.IntegerField(choices=CATE_CHOICES, default=1)
    buy_price = models.FloatField(verbose_name='Buying Price')
    quantity = models.PositiveIntegerField()
    sell_price = models.FloatField(verbose_name='Selling Price')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Goods: %s>' % self.name

    class Meta:
        db_table = 'goods'
        verbose_name = 'goods'
        verbose_name_plural = verbose_name
