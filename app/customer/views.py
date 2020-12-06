from rest_framework import generics, authentication, permissions
from rest_framework.response import Response

from .serializers import CustomerSerializer
from core.models import Customer

class ListCustomerView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

class CreateCustomerView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, TC):
        customer = Customer.objects.get(TC=TC)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

class CustomerDeleteView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, TC):
        customer = Customer.objects.get(TC=TC)
        customer.delete()
        return Response('Deleted successfully')