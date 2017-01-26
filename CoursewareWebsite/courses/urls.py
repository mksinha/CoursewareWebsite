from django.conf.urls import url
import django.contrib.auth.views

import courses.views

urlpatterns = [
    # Examples:
    url(r'^$', courses.views.home, name='coursehome'),
    url(r'^search/$', courses.views.search, name='coursesearch'),
    url(r'^(?P<subject>\w*)/(?P<courseid>\w*)/', courses.views.course),
]