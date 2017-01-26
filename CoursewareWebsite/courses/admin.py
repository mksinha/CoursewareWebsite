from django.contrib import admin
from courses.models import *

# Register your models here.

admin.site.register(Course)
admin.site.register(CourseContent)
admin.site.register(Student)
admin.site.register(CourseCompletion)