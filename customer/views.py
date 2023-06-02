from django.shortcuts import render
from customer.serializers import*


# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
class GetCustomerView(APIView):
    def get(self,request):
        instnce = Customers.objects.all()
        serializer =GetCustomerSerializer(instnce,many=True)
        return Response(serializer.data) 

    
    def post(delf,request):
        params=request.data
        print("data",params)
        ser=GetCustomerSerializer(data=params)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"Message:""save successfully"})
    
class GetAdressview(APIView):
    def get(self,request):
        instance = Customers.objects.all()
        serializer =CustomersAdressSerializers(instance,many=True)
        return Response(serializer.data)
    
class CustomersDetailAddressViews(APIView):
    def get(self,request,pk):
         instances = Customers.object.filter(id=pk)
         ser = CustomersDetailAddressSerializer(instances,many=True)
         ser = ser
         
