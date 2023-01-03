from dataclasses import field
from rest_framework import serializers
from .models import Users, Companies, Items, Likes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"
