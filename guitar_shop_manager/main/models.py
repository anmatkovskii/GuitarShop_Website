from django.db import models


class Guitar(models.Model):
    type = models.CharField(max_length=100)
    prod_name = models.CharField(max_length=200)
    model = models.CharField(max_length=400, unique=True)
    prod_price = models.IntegerField(null=True)
    body = models.CharField(max_length=200, null=True, blank=True)
    discount = models.IntegerField(default=0)
    strings = models.IntegerField(null=True)
    body_material = models.CharField(max_length=200)
    neck_attachment = models.CharField(max_length=200)
    scale = models.CharField(max_length=200)
    date_add = models.DateField(null=True)
    bridge = models.CharField(max_length=200)
    frets = models.CharField(max_length=200)
    pickups = models.CharField(max_length=200)
    fretboard_material = models.CharField(max_length=200)
    fretboard_pad_material = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    default_strings = models.CharField(max_length=200)
    pegs = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    present = models.IntegerField(null=True)


class New(models.Model):
    new_name = models.CharField(max_length=400)
    content = models.TextField(max_length=111111111111)
    date_add = models.DateField(null=True)
    image = models.TextField(max_length=111111111111)


class Review(models.Model):
    rating = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    user_name = models.CharField(max_length=50)
    content = models.TextField(max_length=111111111111)
    rating = models.IntegerField(choices=rating)
    item_bought = models.ForeignKey(Guitar, on_delete=models.SET_NULL, null=True)


class Video(models.Model):
    link = models.TextField(max_length=111111111111, unique=True)


class GuitarImage(models.Model):
    item_name = models.ForeignKey(Guitar, on_delete=models.SET_NULL, null=True)
    image = models.TextField(max_length=111111111111)


class Admin(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)


class Order(models.Model):
    adress = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    item_bought = models.ForeignKey(Guitar, on_delete=models.SET_NULL, null=True)
    date_order = models.DateTimeField(null=True)

