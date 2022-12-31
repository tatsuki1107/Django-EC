from rest_framework import viewsets, filters, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Users, Companies
from .serializers import UserSerializer, CompanySerializer

# Create your views here.


class UserViewSet(generics.ListAPIView):
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

        
