# Generated by Django 4.0.1 on 2023-05-16 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='date_add',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='guitar',
            name='default_strings',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='guitar',
            name='present',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='guitar',
            name='prod_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='guitar',
            name='scale',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='guitar',
            name='strings',
            field=models.IntegerField(null=True),
        ),
    ]
