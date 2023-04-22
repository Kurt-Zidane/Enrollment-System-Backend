from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'schedules', views.SchedulesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('schedules/<int:pk>/', views.ScheduleViewSet.as_view()),
    path('schedules/', views.SchedulesViewSet.as_view()),
    path('schedules/student/<int:student_id>/', views.StudentScheduleViewSet.as_view()),
    path('schedules/<int:schedule_id>/enrollments/',views.ScheduleEnrollmentListView.as_view()),
]
