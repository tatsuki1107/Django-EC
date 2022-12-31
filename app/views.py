from django.http import HttpResponse
import json
from rest_framework import viewsets, filters, generics
from .models import Users
from .serializers import UserSerializer

# Create your views here.


class UserViewSet(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


def createUser(request):
    res = {"user": "tatsuki"}
    dumped_res = json.dumps(res)
    return HttpResponse(dumped_res)
