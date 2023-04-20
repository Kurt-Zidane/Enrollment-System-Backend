from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from .serializers import ScheduleSerializer, SubjectSerializer, ProfessorSerializer, StudentSerializer
from .models import Schedule
from subjects.models import Subject
from professor.models import Professor
from students.models import Student


class ScheduleViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all().order_by('date_added')



class SubjectViewSet(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ProfessorViewSet(generics.RetrieveAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class StudentViewSet(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer