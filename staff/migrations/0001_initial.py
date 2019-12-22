# Generated by Django 3.0.1 on 2019-12-22 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1)),
                ('age', models.IntegerField()),
                ('department', models.IntegerField(choices=[(1, 'AD'), (2, 'HRD'), (3, 'MD'), (4, 'TD'), (5, 'CSD')], default=1)),
                ('position', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('salary', models.FloatField()),
                ('address', models.CharField(max_length=300)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]