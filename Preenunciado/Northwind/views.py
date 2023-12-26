from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *

from rest_framework.response import Response

# Create your views here.

class CategoriesViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class CustomercustomerdemoViewset(viewsets.ModelViewSet):
    queryset = CustomerCustomerDemo.objects.all()
    serializer_class = CustomerCustomerDemoSerializer

class CustomerdemographicsViewset(viewsets.ModelViewSet):
    queryset = CustomerDemographics.objects.all()
    serializer_class = CustomerDemographicsSerializer

class CustomersViewset(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class EmployeeterritoriesViewset(viewsets.ModelViewSet):
    queryset = EmployeeTerritories.objects.all()
    serializer_class = EmployeeTerritoriesSerializer

class EmployeesViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class OrderdetailsViewset(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer

class OrdersViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class ProductsViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class RegionViewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ShippersViewset(viewsets.ModelViewSet):
    queryset = Shippers.objects.all()
    serializer_class = ShippersSerializer

class SuppliersViewset(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer

class TerritoriesViewset(viewsets.ModelViewSet):
    queryset = Territories.objects.all()
    serializer_class = TerritoriesSerializer

from django.http import JsonResponse

class ProductListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def get_queryset(self):
        SupplierID = self.request.query_params.get('supplierid')
        CategoryID = self.request.query_params.get('categoryid')
        stockmin = self.request.query_params.get('stockmin')

        if not SupplierID or not CategoryID:
            return JsonResponse({'error': 'Los parámetros supplierid y categoryid son obligatorios'}, status=400)

        try:
            supplier = Suppliers.objects.get(SupplierID=SupplierID)
            category = Categories.objects.get(CategoryID=CategoryID)
        except Suppliers.DoesNotExist:
            return JsonResponse({'error': f'No existe un proveedor con id {CategoryID}'}, status=404)
        except Categories.DoesNotExist:
            return JsonResponse({'error': f'No existe una categoría con id {CategoryID}'}, status=404)

        queryset = Products.objects.filter(
            SupplierID=supplier,
            CategoryID=category,
            Discontinued=False,
            UnitsInStock__lte=stockmin
        ).order_by('UnitsInStock', 'UnitsOnOrder', 'UnitPrice')

        return queryset
    
class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrdersSerializer

    def create(self, request, *args, **kwargs):
        SupplierID = request.data.get('supplierid')
        CategoryID = request.data.get('categoryid')
        StockRequerido = int(request.data.get('stockRequerido', 0))
        CustomerID = request.data.get('customerid')
        EmployeeID = request.data.get('employeeid')
        ShipVia = request.data.get('shipperid')

        if not SupplierID or not CategoryID or not CustomerID or not EmployeeID or not ShipVia:
            return JsonResponse({'error': 'Los parámetros SupplierID, CategoryID, CustomerID, EmployeeID y ShipVia son obligatorios'}, status=400)

        try:
            supplier = Suppliers.objects.get(SupplierID=SupplierID)
            category = Categories.objects.get(CategoryID=CategoryID)
        except Suppliers.DoesNotExist:
            return JsonResponse({'error': f'No existe un proveedor con id {SupplierID}'}, status=404)
        except Categories.DoesNotExist:
            return JsonResponse({'error': f'No existe una categoría con id {CategoryID}'}, status=404)

        products_to_order = Products.objects.filter(
            SupplierID=supplier,
            CategoryID=category,
            Discontinued=False,
            UnitsInStock__lte=StockRequerido
        )

        if not products_to_order.exists():
            return JsonResponse({'error': 'No hay productos en condiciones de ser pedidos'}, status=204)

        order_data = {
            'SupplierID': SupplierID,
            'CategoryID': CategoryID,
            'stockRequerido': StockRequerido,
            'CustomerID': CustomerID,
            'EmployeeID': EmployeeID,
            'ShipVia': ShipVia,
            'freight': 0,
        }

        order_serializer = self.get_serializer(data=order_data)
        order_serializer.is_valid(raise_exception=True)
        order = order_serializer.save()

        total_quantity = 0
        for Product in products_to_order:
            Quantity = StockRequerido - (Product.UnitsOnOrder + Product.UnitsInStock)
            if Quantity > 0:
                UnitPrice = Product.UnitPrice
                Discount = 0 if Quantity < 100 else 0.10

                order_detail_data = {
                    'Order': order,
                    'Product': Product,
                    'UnitPrice': UnitPrice,
                    'Quantity': Quantity,
                    'Discount': Discount,
                }

                order_detail_serializer = OrderDetailsSerializer(data=order_detail_data)
                order_detail_serializer.is_valid(raise_exception=True)
                order_detail_serializer.save()

                totalQuantity += Quantity

        order.freight = 0
        order.save()

        response_data = OrdersSerializer(order).data
        response_data['total_quantity'] = total_quantity

        return Response(response_data, status=201)
