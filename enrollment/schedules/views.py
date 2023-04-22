from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, generics
from .serializers import ScheduleSerializer, SubjectSerializer, ProfessorSerializer, StudentSerializer
from .models import Schedule
from subjects.models import Subject
from professor.models import Professor
from students.models import Student

class ScheduleViewSet(generics.RetrieveUpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all().order_by('date_added')

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        student_id = request.data.get('student_id', None)
        if student_id:
            instance.student.remove(student_id)
            instance.save()
            return Response({'message': 'Student removed from schedule'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'student_id is required'}, status=status.HTTP_400_BAD_REQUEST)

class SchedulesViewSet(generics.ListCreateAPIView):
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


class StudentScheduleViewSet(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        return Schedule.objects.filter(student__id=student_id)
    
class ScheduleEnrollmentListView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        schedule_id = self.kwargs.get('schedule_id')
        return Schedule.objects.get(id=schedule_id).student.all()