from django.urls import path
from .views import createUser, UserViewSet

urlpatterns = [
    path('users', UserViewSet.as_view())

]
