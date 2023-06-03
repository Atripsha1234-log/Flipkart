from rest_framework import serializers

from customer.models import *
class GetCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields= "__all__"

class CustomersAdressSerializers(serializers.ModelSerializer):

    class Meta:
        model = CustomersAddress
        fields= "__all__"


class CustomersDetailsAdressSerializers(serializers.ModelSerializer):
    customer_address = CustomersAdressSerializers(many = True)
    class Meta:
        model = Customers
        fields = ('  first_name','last_name','mobile','adress','country','city','Dob')
