from django.db import models

class Goods(models.Model):
    CATE_CHOICES = (
        (1, 'Food'), (2, 'Drink'), (3, 'Fruit'),
        (4, 'Daily Supply'), (5, 'Electronic'),
    )
    name = models.CharField(max_length=50)
    mfr = models.CharField(max_length=300)
    category = models.IntegerField(choices=CATE_CHOICES, default=1)
    bprice = models.FloatField()
    quantity = models.IntegerField()
    sprice = models.FloatField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Staff: %s>' % (self.name)