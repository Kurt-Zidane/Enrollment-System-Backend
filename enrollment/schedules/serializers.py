from rest_framework import serializers
from schedules.models import Schedule
from professor.models import Professor
from students.models import Student
from subjects.models import Subject


class ScheduleSerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    professors = serializers.SlugRelatedField(
        queryset=Professor.objects.all(), slug_field='full_name', allow_null=True)

    subjects = serializers.SlugRelatedField(
        queryset=Subject.objects.all(), slug_field='subject_name', allow_null=True)

    students = serializers.SlugRelatedField(
        queryset=Student.objects.all(), many=True, slug_field='full_name', allow_null=True)

    class Meta:
        model = Schedule
        fields = ('id', 'schedule_days', 'time',
                  'professors', 'subjects', 'students', 'date_added')
        read_only_fields = ['id', 'date_added',
                            'professors', 'subjects', 'students']


class ScheduleProfessorSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    professor_assigned = serializers.SlugRelatedField(queryset=Professor.objects.all(), slug_field='full_name', allow_null=True)

    schedule = serializers.SlugRelatedField(queryset=Schedule.objects.all(), slug_field='full_name', allow_null=True)

    class Meta:
        model = Schedule
        fields = ('id', 'schedule', 
                  'professor_assigned',  'date_joined')
        read_only_fields = ('id', 'professor_assigned',
                            'shedule_days', 'time', 'date_joined',)


class ScheduleStudentSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    student_assigned = serializers.SlugRelatedField(
        queryset=Student.objects.all(), slug_field='full_name', allow_null=True)

    schedule = serializers.SlugRelatedField(
        queryset=Schedule.objects.all(), slug_field='full_name', allow_null=True)

    class Meta:
        model = Schedule
        fields = ('id', 'schedule', 'student_assigned', 'date_joined')
        read_only_fields = ('id', 'student_assigned',
                            'schedule', 'date_joined')


class ScheduleSubjectSerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    schedule = serializers.SlugRelatedField(
        queryset=Schedule.objects.all(), slug_field='full_name', allow_null=True)

    subject_assigned = serializers.SlugRelatedField(
        queryset=Subject.objects.all(), slug_field='subject_name', allow_null=True)

    class Meta:
        model = Schedule
        fields = ('id', 'schedule', 'subject_assigned', 'date_added')
        read_only_fields = ('id', 'subject_assigned',
                            'schedule', 'date_added')
