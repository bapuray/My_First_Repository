# Generated by Django 2.0.2 on 2018-02-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuliza_cart', '0003_auto_20180210_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]