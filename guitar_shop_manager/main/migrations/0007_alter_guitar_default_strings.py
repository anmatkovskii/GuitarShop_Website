# Generated by Django 4.0.1 on 2023-05-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_guitar_default_strings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='default_strings',
            field=models.CharField(max_length=200),
        ),
    ]
