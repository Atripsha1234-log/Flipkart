# Generated by Django 4.2.1 on 2023-05-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customers_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='adress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='city',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
