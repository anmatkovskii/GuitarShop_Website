from django.urls import path, include, re_path
from . import views
from main.views import *

urlpatterns = [
    path('guitars/', GuitarsAPIView.as_view()),
    path('guitars/<int:pk>/', GuitarDeleteAPIView.as_view()),
    path('news/', NewsAPIView.as_view()),
    path('reviews/', ReviewsAPIView.as_view()),
    path('videos/', VideosAPIView.as_view()),
    path('guitar-img/', GuitarImagesAPIView.as_view()),
    path('guitar-img/<int:pk>/', GuitarImageDeleteAPIView.as_view()),
    path('admins/', AdminsAPIView.as_view()),
    path('guitar/<int:guitar_id>/', views.guitar_detail, name='guitar_detail'),
    path('guitar/<int:guitar_id>/order/', views.guitar_order, name='order'),
    path('main/', views.main_page, name='main_page'),
    path('contacts/', views.contacts, name='contacts'),
    path('shipping/', views.shipping, name='shipping'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('about_us/', views.about_us, name='about_us'),
    re_path(r'catalogue/filtered/?', views.catalogue_filtered, name='catalogue_filtered'),
]