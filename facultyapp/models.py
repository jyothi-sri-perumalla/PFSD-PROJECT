from django.db import models
from adminapp.models import StudentList


# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=100, unique=True)
    Content = models.TextField()

    def __str__(self):
        return self.Title


class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'Advanced Object-Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
    ]
    SECTION_CHOICES = [
        ('S11', 'Section S11'),
        ('S12', 'Section S12'),
        ('S13', 'Section S13'),
        ('S14', 'Section S14'),
        ('S15', 'Section S15'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def str(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'