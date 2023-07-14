# Generated by Django 4.0.1 on 2023-05-16 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_guitar_date_add_guitar_default_strings_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=400, unique=True)),
                ('prod_price', models.IntegerField(null=True)),
                ('body', models.CharField(max_length=200)),
                ('discount', models.IntegerField(default=0)),
                ('strings', models.IntegerField(null=True)),
                ('body_material', models.CharField(max_length=200)),
                ('neck_attachment', models.CharField(max_length=200)),
                ('scale', models.FloatField(null=True)),
                ('date_add', models.DateField(null=True)),
                ('bridge', models.CharField(max_length=200)),
                ('frets', models.CharField(max_length=200)),
                ('pickups', models.CharField(max_length=200)),
                ('fretboard_material', models.CharField(max_length=200)),
                ('fretboard_pad_material', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('default_strings', models.FloatField(null=True)),
                ('pegs', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=10000)),
                ('present', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_name', models.CharField(max_length=400)),
                ('content', models.TextField(max_length=111111111111)),
                ('date_add', models.DateField(null=True)),
                ('image', models.TextField(max_length=111111111111)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=111111111111)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(max_length=111111111111)),
            ],
        ),
        migrations.CreateModel(
            name='GuitarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(max_length=111111111111)),
                ('item_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.guitar')),
            ],
        ),
        migrations.CreateModel(
            name='BassImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(max_length=111111111111)),
                ('item_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.bass')),
            ],
        ),
    ]