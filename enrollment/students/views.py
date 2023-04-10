from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework import generics

class StudentViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    queryset = Student.objects.all().order_by('date_joined')

