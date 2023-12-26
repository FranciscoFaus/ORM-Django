from django.db import models

# Create your models here.

class Categories(models.Model):
    CategoryID = models.AutoField(db_column='CategoryID', primary_key=True)
    CategoryName = models.CharField(db_column='CategoryName', max_length=15)
    Description = models.TextField(db_column='Description')
    Picture = models.BinaryField(db_column='Picture', null=True)

    class Meta:
        managed = False
        db_table = 'Categories'

class CustomerCustomerDemo(models.Model):
    CustomerID = models.CharField(db_column='CustomerID', max_length=5, primary_key=True)
    CustomerTypeID = models.CharField(db_column='CustomerTypeID', max_length=10)

    class Meta:
        managed = False
        db_table = 'CustomerCustomerDemo'
        unique_together = (('CustomerID', 'CustomerTypeID'),)

class CustomerDemographics(models.Model):
    CustomerTypeID = models.CharField(db_column='CustomerTypeID', max_length=10, primary_key=True)
    CustomerDesc = models.TextField(db_column='CustomerDesc')

    class Meta:
        managed = False
        db_table = 'CustomerDemographics'

class Customers(models.Model):
    CustomerID = models.CharField(db_column='CustomerID', max_length=5, primary_key=True)
    CompanyName = models.CharField(db_column='CompanyName', max_length=40)
    ContactName = models.CharField(db_column='ContactName', max_length=30, null=True)
    ContactTitle = models.CharField(db_column='ContactTitle', max_length=30, null=True)
    Address = models.CharField(db_column='Address', max_length=60, null=True)
    City = models.CharField(db_column='City', max_length=15, null=True)
    Region = models.CharField(db_column='Region', max_length=15, null=True)
    PostalCode = models.CharField(db_column='PostalCode', max_length=10, null=True)
    Country = models.CharField(db_column='Country', max_length=15, null=True)
    Phone = models.CharField(db_column='Phone', max_length=24, null=True)
    Fax = models.CharField(db_column='Fax', max_length=24, null=True)

    class Meta:
        managed = False
        db_table = 'Customers'

class Employees(models.Model):
    EmployeeID = models.AutoField(db_column='EmployeeID', primary_key=True)
    LastName = models.CharField(db_column='LastName', max_length=20)
    FirstName = models.CharField(db_column='FirstName', max_length=10)
    Title = models.CharField(db_column='Title', max_length=30, null=True)
    TitleOfCourtesy = models.CharField(db_column='TitleOfCourtesy', max_length=25, null=True)
    BirthDate = models.DateTimeField(db_column='BirthDate', null=True)
    HireDate = models.DateTimeField(db_column='HireDate', null=True)
    Address = models.CharField(db_column='Address', max_length=60, null=True)
    City = models.CharField(db_column='City', max_length=15, null=True)
    Region = models.CharField(db_column='Region', max_length=15, null=True)
    PostalCode = models.CharField(db_column='PostalCode', max_length=10, null=True)
    Country = models.CharField(db_column='Country', max_length=15, null=True)
    HomePhone = models.CharField(db_column='HomePhone', max_length=24, null=True)
    Extension = models.CharField(db_column='Extension', max_length=4, null=True)
    Photo = models.BinaryField(db_column='Photo', null=True)
    Notes = models.TextField(db_column='Notes')
    ReportsTo = models.ForeignKey('self', db_column='ReportsTo', null=True, on_delete=models.SET_NULL)
    PhotoPath = models.CharField(db_column='PhotoPath', max_length=255, null=True)
    Salary = models.FloatField(db_column='Salary', null=True)

    class Meta:
        managed = False
        db_table = 'Employees'

class EmployeeTerritories(models.Model):
    EmployeeID = models.IntegerField(db_column='EmployeeID',primary_key=True)
    TerritoryID = models.CharField(db_column='TerritoryID', max_length=20)

    class Meta:
        managed = False
        db_table = 'EmployeeTerritories'
        unique_together = (('EmployeeID', 'TerritoryID'),)

class OrderDetails(models.Model):
    OrderID = models.IntegerField(db_column='OrderID', primary_key=True)
    ProductID = models.IntegerField(db_column='ProductID')
    UnitPrice = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=4, default=0)
    Quantity = models.SmallIntegerField(db_column='Quantity', default=1)
    Discount = models.FloatField(db_column='Discount', default=0)

    class Meta:
        managed = False
        db_table = 'OrderDetails'
        unique_together = (('OrderID', 'ProductID'),)

class Orders(models.Model):
    OrderID = models.AutoField(db_column='OrderID', primary_key=True)
    CustomerID = models.CharField(db_column='CustomerID', max_length=5, null=True)
    EmployeeID = models.IntegerField(db_column='EmployeeID', null=True)
    OrderDate = models.DateTimeField(db_column='OrderDate', null=True)
    RequiredDate = models.DateTimeField(db_column='RequiredDate', null=True)
    ShippedDate = models.DateTimeField(db_column='ShippedDate', null=True)
    ShipVia = models.IntegerField(db_column='ShipVia', null=True)
    Freight = models.DecimalField(db_column='Freight', max_digits=10, decimal_places=4, default=0)
    ShipName = models.CharField(db_column='ShipName', max_length=40, null=True)
    ShipAddress = models.CharField(db_column='ShipAddress', max_length=60, null=True)
    ShipCity = models.CharField(db_column='ShipCity', max_length=15, null=True)
    ShipRegion = models.CharField(db_column='ShipRegion', max_length=15, null=True)
    ShipPostalCode = models.CharField(db_column='ShipPostalCode', max_length=10, null=True)
    ShipCountry = models.CharField(db_column='ShipCountry', max_length=15, null=True)
    
    class Meta:
        managed = False
        db_table = 'Orders'

class Products(models.Model):
    ProductID = models.AutoField(db_column='ProductID', primary_key=True)
    ProductName = models.CharField(db_column='ProductName', max_length=40)
    SupplierID = models.IntegerField(db_column='SupplierID', null=True)
    CategoryID = models.IntegerField(db_column='CategoryID', null=True)
    QuantityPerUnit = models.CharField(db_column='QuantityPerUnit', max_length=20, null=True)
    UnitPrice = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=4, default=0)
    UnitsInStock = models.SmallIntegerField(db_column='UnitsInStock', default=0)
    UnitsOnOrder = models.SmallIntegerField(db_column='UnitsOnOrder', default=0)
    ReorderLevel = models.SmallIntegerField(db_column='ReorderLevel', default=0)
    Discontinued = models.BooleanField(db_column='Discontinued', default=False)

    class Meta:
        managed = False
        db_table = 'Products'

class Region(models.Model):
    RegionID = models.IntegerField(db_column='RegionID', primary_key=True)
    RegionDescription = models.CharField(db_column='RegionDescription', max_length=50)

    class Meta:
        managed = False
        db_table = 'Region'

class Shippers(models.Model):
    ShipperID = models.AutoField(db_column='ShipperID', primary_key=True)
    CompanyName = models.CharField(db_column='CompanyName', max_length=40)
    Phone = models.CharField(db_column='Phone', max_length=24, null=True)

    class Meta:
        managed = False
        db_table = 'Shippers'

class Suppliers(models.Model):
    SupplierID = models.AutoField(db_column='SupplierID', primary_key=True)
    CompanyName = models.CharField(db_column='CompanyName', max_length=40)
    ContactName = models.CharField(db_column='ContactName', max_length=30, null=True)
    ContactTitle = models.CharField(db_column='ContactTitle', max_length=30, null=True)
    Address = models.CharField(db_column='Address', max_length=60, null=True)
    City = models.CharField(db_column='City', max_length=15, null=True)
    Region = models.CharField(db_column='Region', max_length=15, null=True)
    PostalCode = models.CharField(db_column='PostalCode', max_length=10, null=True)
    Country = models.CharField(db_column='Country', max_length=15, null=True)
    Phone = models.CharField(db_column='Phone', max_length=24, null=True)
    Fax = models.CharField(db_column='Fax', max_length=24, null=True)
    HomePage = models.TextField(db_column='HomePage', null=True)

    class Meta:
        managed = False
        db_table = 'Suppliers'

class Territories(models.Model):
    TerritoryID = models.CharField(db_column='TerritoryID', primary_key=True, max_length=20)
    TerritoryDescription = models.CharField(db_column='TerritoryDescription', max_length=50)
    RegionID = models.IntegerField(db_column='RegionID')

    class Meta:
        managed = False
        db_table = 'Territories'