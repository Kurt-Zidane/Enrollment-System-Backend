from django.db import models
from django.utils.timezone import now

# Create your models here.


class Student(models.Model):

    class Genders(models.TextChoices):
        MALE = 'Male',
        FEMALE = 'Female',
        OTHER = 'Other',
    

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    mi = models.CharField(max_length=5)
    date_joined = models.DateTimeField(null=True, default=now, editable=False)
    gender = models.CharField(max_length=20, choices=Genders.choices)
    address = models.CharField(max_length=250)
    suffix = models.CharField(blank=True, max_length=40)
    birthdate = models.DateField(blank=True)
    
    STUDENT_CHOICES = (
        ('Undergraduate', 'Undergraduate'),

    )

    studentType = models.CharField(max_length=15, null='Choose', choices=STUDENT_CHOICES)


    form137_done = models.BooleanField(null=True)
    PSA_done = models.BooleanField(null=True)
    TwoByTwo_done = models.BooleanField(null=True)
    GoodMorale_done = models.BooleanField(null=True)

    ##subjects = models.ManyToManyField(
    ##    'subjects.Subject', through='subjects.SubjectStudent', null=True)
    full_name = models.CharField(max_length=80, blank= True,editable=False)

    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name