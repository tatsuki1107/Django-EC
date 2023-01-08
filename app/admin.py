from django.contrib import admin
from .models import CustomUser, Items, Orders, Companies, Likes

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Items)
admin.site.register(Orders)
admin.site.register(Companies)
admin.site.register(Likes)
