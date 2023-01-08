from rest_framework import serializers
from .models import CustomUser, Companies, Items, Likes, Orders

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username"]

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
        exclude = ["user"]



class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Orders
        exclude = ["user"]
    
    def get_total_price(self, instance):
        bought_price = instance.quantity * instance.item.price
        return bought_price
        