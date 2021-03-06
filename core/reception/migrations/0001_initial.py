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
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, verbose_name='Client Name')),
                ('client_cin', models.CharField(max_length=20, unique=True, verbose_name='Client CIN')),
                ('command_token', models.CharField(max_length=10, unique=True, verbose_name='Command Token')),
                ('command_quantity', models.IntegerField(verbose_name='Requested Quantity')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Product')),
            ],
        ),
    ]
