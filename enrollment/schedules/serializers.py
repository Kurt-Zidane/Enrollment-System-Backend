from rest_framework import serializers
from .models import Schedule
from subjects.models import Subject
from professor.models import Professor
from students.models import Student


class ScheduleSerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)
    subject = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all())
    professor = serializers.PrimaryKeyRelatedField(
        queryset=Professor.objects.all())
    student = serializers.SlugRelatedField(
        queryset=Student.objects.all(), many=True, slug_field='full_name', allow_null=True)

    class Meta:
        model = Schedule
        fields = ('id', 'schedule_days', 'time',
                  'date_added', 'subject', 'professor', 'student')
        read_only_fields = ('id', 'date_added',)


class SubjectSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Professor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
