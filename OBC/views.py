from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import StudentForm
# Create your views here.
class IndexView(TemplateView):
    template_name = 'home.html'

def post_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'form.html', {'form': form})