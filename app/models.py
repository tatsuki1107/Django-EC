from django.db import models

# Create your models here.


class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.TextField(null=False)
    user_address = models.TextField(null=False)

    class Meta:
        db_table = "users"


class Items(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    item_name = models.TextField(null=False)
    item_type = models.TextField(null=False)
    company_id = models.ForeignKey(
        "Companies", on_delete=models.CASCADE, null=False)
    populality = models.IntegerField(null=True)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = "items"


class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE, null=False)
    item_id = models.ForeignKey("Items", on_delete=models.CASCADE, null=False)
    order_date = models.DateTimeField(null=False)
    quantity = models.IntegerField(null=False)

    class Meta:
        db_table = "orders"


class Companies(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    company_name = models.TextField(null=False)
    populality = models.IntegerField(null=True)

    class Meta:
        db_table = "companies"


class Likes(models.Model):
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE, null=False)
    item_id = models.ForeignKey("Items", on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = "likes"
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "item_id"], name="user_like_item")
        ]
