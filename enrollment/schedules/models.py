from django.db import models
from django.utils.timezone import now
from django import forms
# Create your models here.


class Schedule(models.Model):

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
    professors = models.ForeignKey('professor.Professor', related_name='ScheduleProfessor_professor_assigned',on_delete=models.CASCADE, null=True)
    students = models.ManyToManyField('students.Student', related_name='ScheduleStudent_student_assigned', through='schedules.ScheduleStudent')
    subjects = models.ForeignKey('subjects.Subject', related_name='ScheduleSubject_subject_assigned',on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.schedule_days + ' ' + self.time}"

    @property
    def full_name(self):
        return f"{self.schedule_days + ' ' + self.time}"

class ScheduleProfessor(models.Model):
    schedule = models.ForeignKey(
        'schedules.Schedule', on_delete=models.CASCADE)
    professor_assigned = models.ForeignKey(
        'professor.Professor', on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField(default=now, editable=False)


class ScheduleStudent(models.Model):
    schedule = models.ForeignKey(
        'schedules.Schedule', on_delete=models.CASCADE)
    student_assigned = models.ForeignKey(
        'students.Student', on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField(default=now, editable=False)


class ScheduleSubject(models.Model): 
    schedule = models.ForeignKey(
        'schedules.Schedule', on_delete=models.CASCADE)
    subject_assigned = models.ForeignKey(
        'subjects.Subject', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(default=now, editable=False)
