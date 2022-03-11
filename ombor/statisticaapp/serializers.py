from rest_framework.serializers import ModelSerializer

from statisticaapp.models import Stats


class StatsSerializer(ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'
