from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import Customers


class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ['id',
                  'full_name',
                  'cpf_cnpj',
                  'address',
                  'value',
                  'approved_value',
                  'status',
                  'score',
                  'updated_at',
                  'created_at']
