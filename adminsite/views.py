from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from OBC.models import Student

# Create your views here.
class StudentList(ListView, LoginRequiredMixin):
    login_url = 'login/'
    context_object_name = 'obc_data'
    model = Student
    template_name = 'adminsite/obc.html'