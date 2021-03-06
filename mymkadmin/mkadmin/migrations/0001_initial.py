# Generated by Django 2.0.6 on 2018-06-14 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, verbose_name='first name')),
                ('lname', models.CharField(max_length=50, verbose_name='last name')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('phone', models.CharField(blank=True, max_length=11, verbose_name='phone number')),
                ('email', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('tax_rate', models.FloatField()),
                ('discount_percentage', models.FloatField()),
                ('gift_certificate', models.FloatField()),
                ('received', models.BooleanField()),
                ('paid', models.BooleanField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mkadmin.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mkadmin.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('retail_cost', models.FloatField(verbose_name='price')),
                ('quantity_in_stock', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='order_products',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mkadmin.Product'),
        ),
    ]
