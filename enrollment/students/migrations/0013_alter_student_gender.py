# Generated by Django 4.2 on 2023-04-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_student_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20),
        ),
    ]
