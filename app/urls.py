from django.urls import path, include
from .views import CompanyViewSet, ItemViewSet, CurrentUserAPIView, delete_like, OrderViewSet, LikeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('items', ItemViewSet)
router.register('order', OrderViewSet)
router.register('like', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('delete_like/', delete_like),
    path('user/', CurrentUserAPIView.as_view()),
]
