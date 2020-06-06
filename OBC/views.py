from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import StudentForm
# Create your views here.
class IndexView(TemplateView):
    template_name = 'home.html'

class StudentEntryView(CreateView):
    template_name = 'form.html'
    form_class = StudentForm
    success_url = reverse_lazy('home')
