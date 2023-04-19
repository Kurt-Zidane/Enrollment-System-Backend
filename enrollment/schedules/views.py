from rest_framework import viewsets
from .models import Schedule, ScheduleProfessor, ScheduleStudent, ScheduleSubject
from .serializers import ScheduleSerializer, ScheduleProfessorSerializer, ScheduleStudentSerializer, ScheduleSubjectSerializer
from rest_framework import generics

# Create your views here.

class ScheduleViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

class SubjectProfessorViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleProfessorSerializer
    queryset = ScheduleProfessor.objects.all().order_by('date_joined')


class ScheduleStudentViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleStudentSerializer
    queryset = ScheduleStudent.objects.all().order_by('date_joined')

class ScheduleSubjectViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSubjectSerializer
    queryset = ScheduleSubject.objects.all().order_by('date_added')