from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from rest_framework import generics
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from django.core import serializers
from . service import GuitarFilter
from django.views.generic import ListView
import requests
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
# from telegram import Bot
import telebot
from telebot import types
import requests


def about_us(request):
    return render(request, 'about_us.html')


def shipping(request):
    return render(request, 'shipping.html')


def contacts(request):
    return render(request, 'contacts.html')


@csrf_exempt
def guitar_order(request, guitar_id):
    if request.method == "GET":
        datalist = []
        guitar = get_object_or_404(Guitar, id=guitar_id)
        imgs = GuitarImage.objects.values("item_name", "image")
        datalist.append(guitar)
        img_list = []


        for j in imgs:
            img_list.append(j)

        for n in img_list:
            if guitar_id == n['item_name']:
                datalist.append(n)

        return render(request, 'order.html', {'guitar': datalist})

    elif request.method == "POST":
        guitar = Guitar.objects.get(id=guitar_id)

        customer_name = request.POST.get('customer_name')
        customer_address = request.POST.get('customer_address')
        customer_phone = request.POST.get('customer_phone')
        date = datetime.now()

        order = Order(adress=customer_address, phone_number=customer_phone, name=customer_name, item_bought=guitar,
                      date_order=date)
        order.save()

        config = {
            'name': 'GuitarShopManager',
            'token': '6011605172:AAExztACmzo32S4_aQAEIF_UBDLp-MTeBCg'
        }
        chat_id = '879609510'

        message = f"У вас нове замовлення!\n {customer_name} замовив гітару: {guitar.prod_name, guitar.model}." \
                  f" \n\nАдреса доставки: {customer_address}\n\n" \
                  f"Контактний номер телефону: {customer_phone} \n\nДата та час замовлення: {date}"

        bot = telebot.TeleBot(config["token"])
        bot.send_message(chat_id, message)

        return HttpResponseRedirect(reverse('guitar_detail', args=[guitar_id]))


def main_page(request):
    link = Guitar.objects.values("id", "prod_name", "model", "prod_price")
    link_json = []
    discount_list = []
    date_list = []
    imgs = GuitarImage.objects.values("item_name", "image")
    img_list = []
    x = 0
    ordered_discount = link.order_by("-discount")
    ordered_date = link.order_by("-date_add")

    news = New.objects.all().values()

    for j in imgs:
        img_list.append(j)

    for i in link:
        guitar_id = i["id"]
        guitar_images = imgs.filter(item_name=guitar_id)
        if guitar_images:
            first_image = guitar_images[0]
            i.update(first_image)
        link_json.append(i)
        if len(link_json) == 3:
            break

    for i in ordered_discount:
        guitar_id = i["id"]
        guitar_images = imgs.filter(item_name=guitar_id)
        if guitar_images:
            first_image = guitar_images[0]
            i.update(first_image)
        discount_list.append(i)
        if len(discount_list) == 3:
            break

    for i in ordered_date:
        guitar_id = i["id"]
        guitar_images = imgs.filter(item_name=guitar_id)
        if guitar_images:
            first_image = guitar_images[0]
            i.update(first_image)
        date_list.append(i)
        if len(date_list) == 3:
            break


    return render(request, 'landing.html', {"context": link_json, "discount": discount_list,
                                            "date": date_list, "news": news})


def catalogue(request):
    if request.method == 'GET':
        link = Guitar.objects.all().values()
        link_json = []
        imgs = GuitarImage.objects.values("item_name", "image")
        img_list = []
        x = 0

        for j in imgs:
            img_list.append(j)

        for i in link:
            for n in img_list:
                if i['id'] == n['item_name']:
                    i.update(n)
                    break
            link_json.append(i)

        return render(request, 'catalogue.html', context={"context": link_json})


def catalogue_filtered(request):
    if request.method == 'GET':
        sort_method = request.GET.get('sortMethod')
        guitars = Guitar.objects.all()
        types = request.GET.get('type')
        if types:
            types = types.split(',')
            guitars = guitars.filter(type__in=types)

        prod_names = request.GET.get('prod_name')
        if prod_names:
            prod_names = prod_names.split(',')
            guitars = guitars.filter(prod_name__in=prod_names)

        bodies = request.GET.get('body')
        if bodies:
            bodies = bodies.split(',')
            guitars = guitars.filter(body__in=bodies)

        strings = request.GET.get('strings')
        if strings:
            strings = strings.split(',')
            guitars = guitars.filter(strings__in=strings)

        body_materials = request.GET.get('body_material')
        if body_materials:
            body_materials = body_materials.split(',')
            guitars = guitars.filter(body_material__in=body_materials)

        neck_materials = request.GET.get('neck_material')
        if neck_materials:
            neck_materials = neck_materials.split(',')
            guitars = guitars.filter(neck_material__in=neck_materials)

        scales = request.GET.get('scale')
        if scales:
            scales = scales.split(',')
            guitars = guitars.filter(scale__in=scales)

        bridges = request.GET.get('bridge')
        if bridges:
            bridges = bridges.split(',')
            guitars = guitars.filter(bridge__in=bridges)

        frets = request.GET.get('frets')
        if frets:
            frets = frets.split(',')
            guitars = guitars.filter(frets__in=frets)

        fretboard_materials = request.GET.get('fretboard_material')
        if fretboard_materials:
            fretboard_materials = fretboard_materials.split(',')
            guitars = guitars.filter(fretboard_material__in=fretboard_materials)

        fretboard_pad_materials = request.GET.get('fretboard_pad_material')
        if fretboard_pad_materials:
            fretboard_pad_materials = fretboard_pad_materials.split(',')
            guitars = guitars.filter(fretboard_pad_material__in=fretboard_pad_materials)

        prod_price_min = request.GET.get('prod_price__min')
        prod_price_max = request.GET.get('prod_price__max')
        if prod_price_min:
            guitars = guitars.filter(prod_price__gte=prod_price_min)
        if prod_price_max:
            guitars = guitars.filter(prod_price__lte=prod_price_max)

        if sort_method == 'price_asc':
            guitars = guitars.order_by('prod_price')
        elif sort_method == 'price_desc':
            guitars = guitars.order_by('-prod_price')
        elif sort_method == 'name_asc':
            guitars = guitars.order_by('prod_name').order_by('model')
        elif sort_method == 'name_desc':
            guitars = guitars.order_by('-prod_name').order_by('-model')
        elif sort_method == 'discount_desc':
            guitars = guitars.order_by('-discount')

        link = guitars.values()
        link_json = []
        imgs = GuitarImage.objects.values("item_name", "image")
        img_list = []
        x = 0


        for j in imgs:
            img_list.append(j)


        for i in link:
            for n in img_list:
                if i['id'] == n['item_name']:
                    i.update(n)
                    break

            link_json.append(i)

        return render(request, 'catalogue.html', context={'context': link_json})


@csrf_exempt
def guitar_detail(request, guitar_id):
    if request.method == "GET":
        datalist = []
        guitar = get_object_or_404(Guitar, id=guitar_id)
        imgs = GuitarImage.objects.values("item_name", "image")
        datalist.append(guitar)
        img_list = []

        reviewlist = []

        reviews = Review.objects.all().values()
        for i in reviews:
            if i['item_bought_id'] == guitar_id:
                reviewlist.append(i)


        for j in imgs:
            img_list.append(j)

        for n in img_list:
            if guitar_id == n['item_name']:
                datalist.append(n)

        return render(request, 'guitar.html', {'guitar': datalist, 'reviews': reviewlist})

    elif request.method == "POST":
        guitar = Guitar.objects.get(id=guitar_id)
        user_name = request.POST.get('user_name')
        review_content = request.POST.get('review_content')
        rating = int(request.POST.get('rating'))

        review = Review(user_name=user_name, content=review_content, rating=rating, item_bought=guitar)
        review.save()

        return HttpResponseRedirect(reverse('guitar_detail', args=[guitar_id]))



class GuitarsAPIView(generics.ListCreateAPIView):
    queryset = Guitar.objects.all()
    serializer_class = GuitarSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GuitarFilter


class GuitarDeleteAPIView(generics.DestroyAPIView):
    queryset = Guitar.objects.all()
    serializer_class = GuitarSerializer


class NewsAPIView(generics.ListCreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class ReviewsAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class VideosAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class GuitarImagesAPIView(generics.ListCreateAPIView):
    queryset = GuitarImage.objects.all()
    serializer_class = GuitarImageSerializer


class GuitarImageDeleteAPIView(generics.DestroyAPIView):
    queryset = GuitarImage.objects.all()
    serializer_class = GuitarImageSerializer


class AdminsAPIView(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
