from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from statisticaapp.models import Stats
from statisticaapp.serializers import StatsSerializer


class StatsLC(ListCreateAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["client", "product"]





class StatsRUD(RetrieveUpdateDestroyAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer




