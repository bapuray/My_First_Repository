# Generated by Django 2.0.2 on 2018-02-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuliza_cart', '0004_cart_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]