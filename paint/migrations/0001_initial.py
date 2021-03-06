# Generated by Django 3.0.4 on 2020-03-30 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('Customer_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Customer ID')),
                ('Customer_name', models.CharField(max_length=50, verbose_name='Customer Name')),
                ('Contact', models.BigIntegerField(blank=True, null=True, verbose_name='Contact')),
                ('Address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Address')),
            ],
            options={
                'verbose_name_plural': 'Customer',
                'db_table': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Delivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(verbose_name='Date')),
                ('Place_of_Delivery', models.CharField(max_length=50, verbose_name='Place Of delivery')),
                ('Delivery_status', models.CharField(max_length=50, verbose_name='Delivery Status')),
            ],
            options={
                'verbose_name_plural': 'Delivers',
                'db_table': 'Delivers',
            },
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('Distributor_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Distributor ID')),
                ('Distributor_name', models.CharField(max_length=50)),
                ('GSTIN', models.CharField(max_length=50, verbose_name='GSTIN')),
                ('Address', models.CharField(max_length=50, verbose_name='Address')),
                ('Email_id', models.EmailField(max_length=70, verbose_name='Email ID')),
                ('Contact_no', models.BigIntegerField(blank=True, null=True, verbose_name='Contact No')),
            ],
            options={
                'verbose_name_plural': 'Distributor',
                'db_table': 'Distributor',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Employee Id')),
                ('Employee_firstname', models.CharField(max_length=50, verbose_name='Employee First Name')),
                ('Employee_lastname', models.CharField(max_length=50, verbose_name='Employee Last Name')),
                ('Address', models.CharField(max_length=50, verbose_name='Address')),
                ('Job_description', models.CharField(max_length=50, verbose_name='Job Description')),
                ('salary', models.IntegerField(verbose_name='Salary')),
                ('Bank_name', models.CharField(max_length=50, verbose_name='Bank Name')),
                ('Bank_branch', models.CharField(max_length=50, verbose_name='Bank Branch')),
                ('Bank_Accno', models.BigIntegerField(verbose_name='Bank Account Number')),
                ('Email_id', models.EmailField(max_length=70, verbose_name='Email ID')),
                ('Phone_no', models.BigIntegerField(verbose_name='Phone No')),
                ('Education_level', models.CharField(max_length=50, verbose_name='Educaton Level')),
                ('Date_of_joining', models.DateField(verbose_name='Date Of Joining')),
            ],
            options={
                'verbose_name_plural': 'Employee',
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('Prod_code', models.AutoField(primary_key=True, serialize=False, verbose_name='Product Code')),
                ('Product_name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('Quantity', models.CharField(max_length=20, verbose_name='Quantity(kg/L)')),
                ('Rate', models.FloatField(verbose_name='Rate')),
                ('Colour', models.CharField(max_length=50, verbose_name='Colour')),
                ('Product_description', models.CharField(max_length=50, verbose_name='Product Description')),
                ('Stock_level', models.IntegerField(verbose_name='Stock Level')),
                ('Shelf_life', models.IntegerField(blank=True, null=True, verbose_name='Shelf Life')),
            ],
            options={
                'verbose_name_plural': 'Product',
                'db_table': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('Purchase_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Purchase ID')),
                ('Date_of_Purchase', models.DateField(verbose_name='Date Of Puchase')),
                ('Discount_in_percentage', models.FloatField(verbose_name='Discount(in percent)')),
                ('Tax_in_percentage', models.FloatField(verbose_name='Tax(in percent)')),
                ('Total_amount', models.FloatField(verbose_name='Total Amount')),
                ('Distributor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint.Distributor', verbose_name='Distributor ID')),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint.Employee', verbose_name='Employee ID')),
            ],
            options={
                'verbose_name_plural': 'Purchase',
                'db_table': 'Purchase',
            },
        ),
        migrations.CreateModel(
            name='Sale_Consists_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.CharField(max_length=20, verbose_name='Quantity')),
            ],
            options={
                'verbose_name_plural': 'Sale Consists of',
                'db_table': 'Sale_Consists_Of',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('Invoice_no', models.AutoField(primary_key=True, serialize=False, verbose_name='Invoice No')),
                ('Date_of_order', models.DateField(verbose_name='Date Of Order')),
                ('Discount_in_percentage', models.FloatField(verbose_name='Discount(in percent)')),
                ('Tax_in_percentage', models.FloatField(verbose_name='Tax(in percent)')),
                ('Total_amount', models.FloatField(verbose_name='Total Amount')),
                ('Mode_of_Payment', models.CharField(max_length=50, verbose_name='Mode Of Payment')),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint.Customers', verbose_name='Customer ID')),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint.Employee', verbose_name='Employee ID')),
                ('Products', models.ManyToManyField(through='paint.Sale_Consists_of', to='paint.Products')),
            ],
            options={
                'verbose_name_plural': 'Sales',
                'db_table': 'Sales',
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('Transport_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Transport ID')),
                ('Transport_name', models.CharField(max_length=50, verbose_name='Transport Name')),
                ('Address', models.CharField(max_length=50, verbose_name='Address')),
                ('Contact', models.BigIntegerField(verbose_name='Contact No')),
                ('Sales', models.ManyToManyField(through='paint.Delivers', to='paint.Sales')),
            ],
            options={
                'verbose_name_plural': 'Transport',
                'db_table': 'Transport',
            },
        ),
        migrations.AddField(
            model_name='sale_consists_of',
            name='Invoice_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint.Sales', verbose_name='Invoice No'),
        ),
        migrations.AddField(
            model_name='sale_consists_of',
            name='Prod_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint.Products', verbose_name='Product Code'),
        ),
        migrations.CreateModel(
            name='Purchase_Consists_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.CharField(max_length=20, verbose_name='Quantity')),
                ('Prod_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint.Products', verbose_name='Product Code')),
                ('Purchase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint.Purchase', verbose_name='Purchase ID')),
            ],
            options={
                'verbose_name_plural': 'Purchase Consists of',
                'db_table': 'Purchase_Consists_Of',
            },
        ),
        migrations.AddField(
            model_name='purchase',
            name='Products',
            field=models.ManyToManyField(through='paint.Purchase_Consists_of', to='paint.Products'),
        ),
        migrations.CreateModel(
            name='Office_Expense',
            fields=[
                ('Expenditure_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Expenditure ID')),
                ('Expenditure_date', models.DateField(verbose_name='Expenditure Date')),
                ('Expense_description', models.CharField(max_length=100, verbose_name='Expense Description')),
                ('Mode_of_payment', models.CharField(max_length=50, verbose_name='Mode Of Payment')),
                ('Amount', models.FloatField(verbose_name='Amount')),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint.Employee', verbose_name='Employee ID')),
            ],
            options={
                'verbose_name_plural': 'Office Expense',
                'db_table': 'Office Expense',
            },
        ),
        migrations.AddField(
            model_name='delivers',
            name='Invoice_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint.Sales', verbose_name='Invoice No'),
        ),
        migrations.AddField(
            model_name='delivers',
            name='Transport_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint.Transport', verbose_name='Transport ID'),
        ),
    ]
