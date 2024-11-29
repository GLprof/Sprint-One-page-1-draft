from rest_framework import serializers

from .models import GeogrObject

class GeogrObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeogrObject
        fields = [
            'id',
            'title_object',
            'latitude_object',
            'longitude_object',
            'height_object',
            'photo_object',
            'user_name',
            'user_email',
            'user_phone',
            'status',
            ]
