from django.shortcuts import render

from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from omborapp.models import Ombor, Product, Client
from omborapp.serializers import OmborSerializer, ProductSerializer, ClientSerializer
from rest_framework.permissions import IsAuthenticated


class OmborLC(ListCreateAPIView):

    serializer_class = OmborSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["ism", "dokon_nomi", "turi"]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ombors = Ombor.objects.filter(user=self.request.user)
        return ombors


class OmborRUD(RetrieveUpdateDestroyAPIView):

    serializer_class = OmborSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ombors = Ombor.objects.filter(user=self.request.user)
        return ombors

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer




class ProductLC(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["nom", "brend_nomi"]


class ProductRUD(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class ClientLC(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["ism", "dokon_nomi"]


class ClientRUD(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

