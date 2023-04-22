from django.db import models
from django.utils.timezone import now
from django import forms
# Create your models here.


class Schedule(models.Model):

    class Semester(models.TextChoices):
        FIRST_SEMESTER = '1st sem'
        SECOND_SEMESTER = '2nd sem'

    class Schedule_days(models.TextChoices):
        Monday = 'Monday',
        Tuesday = 'Tuesday',
        Wednesday = 'Wednesday',
        Thursday = 'Thursday',
        Friday = 'Friday',
        Saturday = 'Saturday',

    time_slots = (
        ('08:00 - 09:30', '08:00 - 09:30'),
        ('09:30 - 11:00', '09:30 - 11:00'),
        ('11:00 - 12:30', '11:00 - 12:30'),
        ('13:00 - 14:30', '13:00 - 14:30'),
        ('14:30 - 16:00', '14:30 - 16:00'),
        ('16:00 - 17:30', '16:00 - 17:30'),
        ('17:30 - 19:00', '17:30 - 19:00'),
        ('19:00 - 20:30', '19:00 - 20:30'),
        ('20:30 - 22:00', '20:30 - 22:00')
    )
    date_added = models.DateTimeField(default=now, editable=False)
    schedule_days = models.CharField(
        null=True, max_length=20, choices=Schedule_days.choices)
    time = models.CharField(max_length=20, null=True, choices=time_slots)
    semester = models.CharField(
        max_length=10, choices=Semester.choices, default=Semester.FIRST_SEMESTER)
    subject = models.ForeignKey(
        'subjects.Subject', on_delete=models.CASCADE, related_name='schedules', null=True)
    professor = models.ForeignKey(
        'professor.Professor', on_delete=models.CASCADE, related_name='schedules', null=True)
    student = models.ManyToManyField(
        'students.Student', related_name='schedules', blank=True, through='schedules.ScheduleStudent')

    def __str__(self):
        return f"{self.schedule_days + ' ' + self.time} - {self.subject if self.subject else 'No subject'} ({self.semester})"

    @property
    def full_name(self):
        return f"{self.schedule_days + ' ' + self.time} ({self.semester})"


class ScheduleStudent(models.Model):
    schedule = models.ForeignKey(
        'schedules.Schedule', on_delete=models.CASCADE)
    students = models.ForeignKey(
        'students.Student', on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField(default=now, editable=False)
