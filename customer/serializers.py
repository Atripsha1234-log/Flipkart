from rest_framework import serializers

from customer.models import *
class GetCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields= "__all__"

class CustomersAdressSerializers():

    class Meta:
        model = CustomersAddress
        fields= "__all__"


    class CustomersDetailsAdressSerializers():
 
    class models = Customers
    Fields = ( 'first_name',' last_name','mobile',' city ',' Dob')