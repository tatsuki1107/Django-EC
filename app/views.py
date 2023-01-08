from rest_framework import viewsets, mixins, status, views
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Companies, Items, Likes, Orders
from .serializers import UserDisplaySerializer, CompanySerializer, ItemSerializer, OrderSerializer, LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
        
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    

class LikeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
     queryset = Likes.objects.all()
     serializer_class = LikeSerializer
     
     def perform_create(self, serializer):
         request_user = self.request.user
         serializer.save(user_id=request_user.id)
    
     def get_queryset(self):
         request_user = self.request.user
         return Likes.objects.filter(user_id=request_user.id)
        

@api_view(["DELETE"])
def delete_like(request):
    try:
        user_id = request.POST.get("user_id")
        item_id = request.POST.get('item_id')
        queryset = Likes.objects.filter(user_id=user_id, item_id=item_id)
    except Likes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)     


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
         request_user = self.request.user
         serializer.save(user_id=request_user.id)
    
    def get_queryset(self):
         request_user = self.request.user
         return Orders.objects.filter(user_id=request_user.id).order_by('-order_date')
         
                
class CurrentUserAPIView(views.APIView):
    
    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)    
    


