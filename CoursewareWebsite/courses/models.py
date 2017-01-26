from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    SUBJECTS = (
        ('PHY', 'Physics'),
        ('CHE', 'Chemistry'),
        ('MTH', 'Mathematics'),
        ('BIO', 'Biology'),
        ('CTA', 'Computers'),
    )
    LEVELS = (
        ('P', 'Primary'),
        ('M', 'Middle'),
        ('H', 'High'),
        ('B', 'Bachelors'),
        ('M', 'Masters'),
        ('X', 'Professional'),
    )
    topic = models.CharField(max_length=100)
    subject = models.CharField(max_length=3, choices=SUBJECTS)
    levels = models.CharField(max_length=1, choices=LEVELS)

class CourseContent(models.Model):
    CONTENT_TYPES = (
        ('L', 'Video Lecture'),
        ('T', 'Video Tutorial'),
        ('R', 'Reading Material'),
        ('P', 'Problem Set'),
    )
    order = models.IntegerField()
    name = models.CharField(max_length=100)
    source = models.URLField()
    type = models.CharField(max_length=1)
    note = models.TextField(max_length=1000)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currentcourse = models.ForeignKey(Course,  on_delete=models.CASCADE)
    
class CourseCompletion(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    degree = models.IntegerField()
    complete = models.BooleanField()