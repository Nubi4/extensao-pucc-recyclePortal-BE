from django.shortcuts import render
from rest_framework import viewsets
from .models import ContractForm
from .serializers import ContractFormSerializer


class ContractFormViewSet(viewsets.ModelViewSet):
    queryset = ContractForm.objects.all()
    serializer_class = ContractFormSerializer
    
# Create your views here.
