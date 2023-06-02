from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name =models.CharField(max_length=15,null=True,blank=True)
    last_name =models.CharField(max_length=15,null=True,blank=True)
    mobile =models.IntegerField(null=True,blank=True)
    adress =models.TextField(null=True,blank=True)
    country =models.CharField(max_length=15,null=True,blank=True)
    city=models.CharField(max_length=15,null=True,blank=True)
    Dob =models.DateField(max_length=15,null=True,blank=True)
    def __str__(self):
        return self.first_name   
    
    
class CustomersAddress(models.Model):
    cutomer =models.ForeignKey(Customers,on_delete=models.CASCADE,null=True,related_name="customers_address")
    street_name = models.CharField(max_length=15,null=True,blank=True)
    street_number =models.IntegerField(null=True,blank=True)
    country_name =models.CharField(max_length=15,null=True,blank=True)
    pin_code =models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.street_name
    
class CustomersAddhar(models.Model):
    customer =models.OneToOneField(Customers,on_delete=models.CASCADE)
    addhar_name =models.CharField(max_length=15,null=True,blank=True)
    adahar_number =models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.addhar_name



    

    
    