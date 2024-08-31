from django.db import models


class TimeDimension(models.Model):
    OrderID = models.BigAutoField(primary_key=True, editable=False)
    order_date = models.DateField(auto_now=False, auto_now_add=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    Quarter = models.PositiveIntegerField(blank=True, null=True)
    Month = models.PositiveIntegerField(blank=True, null=True)


class CityDimension(models.Model):
    CityID = models.BigAutoField(primary_key=True, editable=False)
    city_name = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)


class CustomerDimension(models.Model):
    CustomerID = models.BigAutoField(primary_key=True, editable=False)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    Address = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(CityDimension, on_delete=models.CASCADE)


class DepartmentDimension(models.Model):
    DepartmentID = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)


class EmployeeDimension(models.Model):
    EmployeeID = models.BigAutoField(primary_key=True, editable=False)
    employee_name = models.CharField(max_length=255, blank=True, null=True)
    DepartmentID = models.ForeignKey(DepartmentDimension, on_delete=models.CASCADE)
    region = models.CharField(max_length=255, blank=True, null=True)
    territory = models.CharField(max_length=255, blank=True, null=True)


class ProductCategoryDimension(models.Model):
    ProductCategoryID = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    uni_price = models.PositiveIntegerField(blank=True, null=True)


class ProductDimension(models.Model):
    ProductID = models.BigAutoField(primary_key=True, editable=False)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    ProductCategoryID = models.ForeignKey(ProductCategoryDimension, on_delete=models.CASCADE)


class Sales(models.Model):
    ProductID = models.BigAutoField(primary_key=True, editable=False)
    OrderID = models.ForeignKey(TimeDimension, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(CustomerDimension, on_delete=models.CASCADE)
    EmployeeID = models.ForeignKey(EmployeeDimension, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)

