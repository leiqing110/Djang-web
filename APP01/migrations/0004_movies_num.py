# Generated by Django 2.2 on 2019-05-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0003_cart_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
