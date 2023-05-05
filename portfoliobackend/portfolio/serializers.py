from .models import Portfolio
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Portfolio
        fields = ['id', 'name', 'phone', 'email']