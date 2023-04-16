from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('students/<pk>', views.StudentViewSet.as_view()),
    path('students/', views.StudentsViewSet.as_view()),

]
