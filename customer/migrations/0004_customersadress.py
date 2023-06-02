# Generated by Django 4.2.1 on 2023-05-25 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customers_adress_alter_customers_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomersAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(blank=True, max_length=15, null=True)),
                ('street_number', models.IntegerField(blank=True, max_length=15, null=True)),
                ('country_name', models.CharField(blank=True, max_length=15, null=True)),
                ('pin_code', models.IntegerField(blank=True, max_length=15, null=True)),
                ('cutomer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customers')),
            ],
        ),
    ]