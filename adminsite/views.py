from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from OBC.models import Student
from .filter import StudentFilter

# Create your views here.
class StudentList(ListView, LoginRequiredMixin):
    login_url = 'login/'
    model = Student
    template_name = 'adminsite/obc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = StudentFilter(self.request.GET, queryset=self.get_queryset()) 
        return context
    