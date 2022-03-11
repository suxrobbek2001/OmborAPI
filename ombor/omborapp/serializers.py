from omborapp.models import Ombor, Product, Client
from rest_framework.serializers import ModelSerializer


class OmborSerializer(ModelSerializer):
    class Meta:
        model = Ombor
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
