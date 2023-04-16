from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework import generics

class StudentViewSet(generics.RetrieveUpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentsViewSet(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
