from rest_framework import serializers
from .models import ContractForm

# Serializers define the API representation.
class ContractFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContractForm
        fields = ['id','email','tipoNegocio','descricao']

