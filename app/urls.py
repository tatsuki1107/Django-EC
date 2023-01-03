from django.urls import path, include
from .views import CompanyViewSet, ItemViewSet, UserViewSet, LikesViewSet, delete_like
from rest_framework import routers

router = routers.DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('items', ItemViewSet)
router.register('users', UserViewSet)
router.register('like', LikesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('delete_like/', delete_like)
]
