# Generated by Django 4.0.1 on 2023-05-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=400, unique=True)),
                ('body', models.CharField(max_length=200)),
                ('discount', models.IntegerField(default=0)),
                ('body_material', models.CharField(max_length=200)),
                ('neck_attachment', models.CharField(max_length=200)),
                ('bridge', models.CharField(max_length=200)),
                ('frets', models.CharField(max_length=200)),
                ('pickups', models.CharField(max_length=200)),
                ('fretboard_material', models.CharField(max_length=200)),
                ('fretboard_pad_material', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('pegs', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=10000)),
            ],
        ),
    ]
