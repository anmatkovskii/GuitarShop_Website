# Generated by Django 4.2.2 on 2023-06-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_order_remove_bassimage_item_name_guitar_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
    ]
