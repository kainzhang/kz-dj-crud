from django.db import models

class Vip(models.Model):
    GENDER_CHOICES = (
        (1, 'Male'), (2, 'Female'),
    )
    name = models.CharField(max_length=50)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)
    discount = models.FloatField()
    create_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '<Vip: %s>' % (self.name)