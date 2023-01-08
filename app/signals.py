from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Orders, Items, Companies

# 購買後のorderテーブルに存在するアイテムと会社のレコードの数をpopualityとする
@receiver(post_save, sender=Orders)
def calc_item_and_company_populality(sender, instance, **kwargs):
  target_item = Items.objects.get(item_id=instance.item_id)
  target_company = Companies.objects.get(company_id=target_item.company_id)
  
  orderd_items = Orders.objects.filter(item_id=instance.item_id).count()
  target_item.populality = orderd_items
  target_item.save()
  
  orderd_companies = Orders.objects.filter(
    item__company__company_id=target_company.company_id
  ).count()
  target_company.populality = orderd_companies
  target_company.save()
