from rest_framework import viewsets, generics, mixins, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Users, Companies, Items, Likes
from .serializers import UserSerializer, CompanySerializer, ItemSerializer, LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
    
    @action(methods=["get"], detail=False)
    def get_companies(self, request):
        response_list = [{"company_id": dict.company_id} for dict in self.get_queryset()]
        return Response(response_list)
    
    @action(methods=['get'], detail=True)
    def detail_company(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

        
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    
class LikesViewSet(
    mixins.CreateModelMixin, 
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    ):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user_id"]

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

