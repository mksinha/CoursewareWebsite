"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'courses/index.html',
        {
            'title':'Study',
        }
    )

def search(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'courses/search.html',
        {
            'title':'Search',
        }
    )

def course(request, subject, courseid):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'courses/course.html',
        {
            'title':'Course',
            'subject':subject,
            'courseid':courseid,
        }
    )
