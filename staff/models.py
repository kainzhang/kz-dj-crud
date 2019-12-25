from django.db import models


class Staff(models.Model):
    GENDER_CHOICES = (
        (1, 'Male'), (2, 'Female'),
    )
    DEPT_CHOICES = (
        (1, 'AD'), (2, 'HRD'), (3, 'MD'),
        (4, 'TD'), (5, 'CSD'),
    )
    name = models.CharField(max_length=50)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
    age = models.PositiveIntegerField()
    department = models.IntegerField(choices=DEPT_CHOICES, default=1)
    position = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    salary = models.FloatField()
    address = models.CharField(max_length=300)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Staff: %s>' % self.name

    class Meta:
        db_table = 'staff'
