# Generated by Django 2.0.2 on 2018-02-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuliza_cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='productImages'),
        ),
    ]
