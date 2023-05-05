from django.shortcuts import render
from .models import Portfolio
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PortfolioSerializer
# Create your views here.

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    
    permission_classes = [permissions.AllowAny]
