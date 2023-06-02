# Generated by Django 4.2.1 on 2023-05-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=15, null=True)),
                ('last_name', models.CharField(blank=True, max_length=15, null=True)),
                ('mobile', models.IntegerField(blank=True, max_length=15, null=True)),
                ('adress', models.CharField(blank=True, max_length=15, null=True)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('Dob', models.DateField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]