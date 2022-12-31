from dataclasses import field
from rest_framework import serializers
from .models import Users, Companies


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("user_id", "user_name", "user_address")

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ("company_id", "company_name", "populality")
