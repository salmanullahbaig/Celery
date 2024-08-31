# Generated by Django 4.2.15 on 2024-08-21 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDimension',
            fields=[
                ('CityID', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('city_name', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDimension',
            fields=[
                ('CustomerID', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelapp.citydimension')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentDimension',
            fields=[
                ('DepartmentID', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDimension',
            fields=[
                ('EmployeeID', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('territory', models.CharField(blank=True, max_length=255, null=True)),
                ('DepartmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelapp.departmentdimension')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategoryDimension',
            fields=[
                ('ProductCategoryID', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('uni_price', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeDimension',
            fields=[
                ('OrderID', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('Quarter', models.PositiveIntegerField(blank=True, null=True)),
                ('Month', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('ProductID', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelapp.customerdimension')),
                ('EmployeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelapp.employeedimension')),
                ('OrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelapp.timedimension')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDimension',
            fields=[
                ('ProductID', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('ProductCategoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelapp.productcategorydimension')),
            ],
        ),
    ]
