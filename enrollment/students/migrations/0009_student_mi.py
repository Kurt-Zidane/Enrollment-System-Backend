# Generated by Django 4.2 on 2023-04-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_remove_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mi',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
