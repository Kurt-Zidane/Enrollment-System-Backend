from rest_framework import serializers
from .models import Schedule
from subjects.models import Subject


class ScheduleSerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)
    subject = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all())

    class Meta:
        model = Schedule
        fields = ('id','schedule_days', 'time', 'date_added', 'subject')
        read_only_fields = ('id', 'date_added')


class SubjectSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = '__all__'