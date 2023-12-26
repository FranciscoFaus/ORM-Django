from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework import renderers
from .views import *

router = routers.DefaultRouter()
router.register(r"Categories", CategoriesViewset,basename="Categories")
router.register(r"Customercustomerdemo", CustomercustomerdemoViewset,basename="Customercustomerdemo")
router.register(r"Customerdemographics", CustomerdemographicsViewset,basename="Customerdemographics")
router.register(r"Customers", CustomersViewset,basename="Customers")
router.register(r"Employeeterritories", EmployeeterritoriesViewset,basename="Employeeterritories")
router.register(r"Employees", EmployeesViewset,basename="Employees")
router.register(r"Orderdetails", OrderdetailsViewset,basename="Orderdetails")
router.register(r"Orders", OrdersViewset,basename="Orders")
router.register(r"Products", ProductsViewset,basename="Products")
router.register(r"Region", RegionViewset,basename="Region")
router.register(r"Shippers", ShippersViewset,basename="Shippers")
router.register(r"Suppliers", SuppliersViewset,basename="Suppliers")
router.register(r"Territories", TerritoriesViewset,basename="Territories")

urlpatterns = [
    path('', include(router.urls)),
]