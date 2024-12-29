from core.models import Booking, Destination
from django.utils import timezone
from rest_framework import serializers


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('status', 'total_price')

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date")
        if data['start_date'] < timezone.now().date():
            raise serializers.ValidationError("Start date cannot be in the past")
        return data