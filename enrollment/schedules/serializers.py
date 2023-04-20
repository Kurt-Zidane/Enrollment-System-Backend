from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    class Meta:
        model = Schedule
        fields = ('schedule_days', 'time', 'date_added')
        read_only_fields = ('id', 'date_added')
