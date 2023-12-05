from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Vehicle, Customer, Supplier, Article, BuildingSite, Warehouse, Transaction, Combination
from .serializers import VehicleSerializer, CustomerSerializer, SupplierSerializer, ArticleSerializer, BuildingSiteSerializer, WarehouseSerializer,\
    TransactionSerializer, CombinationtionSerializer, TransactSerializer, CombinationReadSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from django_filters.rest_framework import DjangoFilterBackend



class VehicleView(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = VehicleSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CustomerView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = CustomerSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class SupplierView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = SupplierSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = ArticleSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class BuildingSiteView(ModelViewSet):
    queryset = BuildingSite.objects.all()
    serializer_class = BuildingSiteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = BuildingSiteSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class WarehouseView(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = WarehouseSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class TransactionView(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def create(self, request):
        serializer = TransactionSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
### READ ONLY VIEW ###

class TransactView(ReadOnlyModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

##### END #####


class CombinationReadView(ReadOnlyModelViewSet):
    queryset = Combination.objects.all()
    serializer_class = CombinationReadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class CombinationView(ModelViewSet):
    queryset = Combination.objects.all()
    serializer_class = CombinationtionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = CombinationtionSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
   