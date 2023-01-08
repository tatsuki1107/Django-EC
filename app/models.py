from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass


class Companies(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    company_name = models.TextField(null=False)
    populality = models.IntegerField(null=True)

    class Meta:
        db_table = "companies"

class Items(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    item_name = models.TextField(null=False)
    item_type = models.TextField(null=False)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, null=False)
    populality = models.IntegerField(null=True)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = "items"

class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=False)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=False)

    class Meta:
        db_table = "orders"

class Likes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=False)

    class Meta:
       db_table = "likes"
       constraints = [
            models.UniqueConstraint(
                fields=["user", "item"], name="user_like_item")
       ]
