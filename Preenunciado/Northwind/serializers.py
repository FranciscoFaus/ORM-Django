from rest_framework import serializers, viewsets
from .models import *

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class CustomerCustomerDemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCustomerDemo
        fields = '__all__'

class CustomerDemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDemographics
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class EmployeeTerritoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTerritories
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    SupplierID = serializers.PrimaryKeyRelatedField(required=False, queryset=Suppliers.objects.all())
    CategoryID = serializers.PrimaryKeyRelatedField(required=False, queryset=Categories.objects.all())

    stockRequerido = serializers.IntegerField(required=False)

    class Meta:
        model = Orders
        fields = ['OrderID','CustomerID','EmployeeID','ShipVia','SupplierID','CategoryID','stockRequerido']

class ProductsSerializer(serializers.ModelSerializer):
    stockFuturo = serializers.SerializerMethodField()

    def get_stockFuturo(self,obj):
        if obj.UnitsInStock is not None and obj.UnitsOnOrder is not None:
            return obj.UnitsInStock + obj.UnitsOnOrder
        return None

    class Meta:
        model = Products
        fields = ['ProductID','ProductName','UnitPrice','stockFuturo']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ShippersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shippers
        fields = '__all__'

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'

class TerritoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Territories
        fields = '__all__'