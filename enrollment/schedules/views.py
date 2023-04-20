from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from .serializers import ScheduleSerializer, SubjectSerializer
from .models import Schedule
from subjects.models import Subject

class ScheduleViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all().order_by('date_added')



class SubjectViewSet(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



