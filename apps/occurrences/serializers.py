from rest_framework import serializers
from .models import Status, Road, Occurrence


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ["name", "color_hex"]


class RoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Road
        fields = ["name", "uf_code", "length"]


# add new code below

class OccurrenceSerializer(serializers.HyperlinkedModelSerializer):
    road_name = serializers.CharField(source='road.name', read_only=True)
    status_name = serializers.CharField(source='status.name', read_only=True)

    class Meta:
        model = Occurrence
        fields = [
            'description',
            'road',
            'road_name',
            'km',
            'status',
            'status_name',
            'created_at',
            'updated_at',
        ]