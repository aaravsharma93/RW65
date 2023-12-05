from rest_framework import serializers
from .models import Vehicle, Customer, Supplier, Article, BuildingSite, Warehouse, Transaction, Combination

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class BuildingSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingSite
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactSerializer(serializers.ModelSerializer):
    vehicle = serializers.StringRelatedField()
    article = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()
    supplier = serializers.StringRelatedField()
    class Meta:
        model = Transaction
        fields = '__all__'
        

class CombinationtionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combination
        fields = '__all__'

class CombinationReadSerializer(serializers.ModelSerializer):
    vehicle = serializers.StringRelatedField()
    article = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()
    supplier = serializers.StringRelatedField()
    class Meta:
        model = Combination
        fields = '__all__'