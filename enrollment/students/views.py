from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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


def delete(self, request, pk):
    try:
        student = self.queryset.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
