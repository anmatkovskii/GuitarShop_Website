from rest_framework import serializers
from .models import *


class GuitarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guitar
        fields = "__all__"


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class GuitarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuitarImage
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"
