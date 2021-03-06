# Generated by Django 3.0.5 on 2020-04-23 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100, verbose_name='History Action')),
                ('target', models.CharField(max_length=50, verbose_name='History Target')),
                ('category_id', models.IntegerField(verbose_name='Category Id')),
                ('category_title', models.CharField(max_length=50, verbose_name='Category Title')),
                ('product_id', models.IntegerField(verbose_name='Product Id')),
                ('product_title', models.CharField(max_length=100, verbose_name='Product Title')),
                ('product_description', models.TextField(verbose_name='Product Title')),
                ('product_quantity', models.IntegerField(verbose_name='Product Quantity')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Product Price')),
                ('product_is_run_out', models.BooleanField(verbose_name='Product is run out ?')),
                ('command_id', models.IntegerField(verbose_name='Command Id')),
                ('command_client_name', models.CharField(max_length=100, verbose_name='Command Client Name')),
                ('command_client_cin', models.CharField(max_length=20, verbose_name='Command Client CIN')),
                ('command_token', models.CharField(max_length=10, verbose_name='Command Title')),
                ('command_quantity', models.IntegerField(verbose_name='Command Quantity')),
                ('command_is_active', models.BooleanField(verbose_name='Command is active ?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('command_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Product', verbose_name='Command Title')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Category', verbose_name='Product Category')),
            ],
        ),
    ]
