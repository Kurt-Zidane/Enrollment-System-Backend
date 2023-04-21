from rest_framework import serializers
from .models import Schedule
from subjects.models import Subject
from professor.models import Professor
from students.models import Student


class ScheduleSerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)
    subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(), slug_field='subject_name', allow_null=True)
    professor = serializers.SlugRelatedField(
        queryset=Professor.objects.all(), slug_field='full_name', allow_null=True)
    student = serializers.PrimaryKeyRelatedField(many=True,
        queryset=Student.objects.all())
    course_id = serializers.ReadOnlyField(source='subject.course_id')
    
    def update(self, instance, validated_data):
        student_data = validated_data.pop('student', None)
        instance = super().update(instance, validated_data)
        if student_data is not None:
            for student in student_data:
                instance.student.add(student)
        return instance

    class Meta:
        model = Schedule
        fields = ('id', 'schedule_days', 'time',
                  'date_added', 'subject', 'professor', 'student','course_id')
        read_only_fields = ('id', 'date_added',)


class SubjectSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True, read_only=True)
    course_id = serializers.ReadOnlyField(source='subject.course_id')
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
