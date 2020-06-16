from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from .forms import LoginForm

app_name='adminsite'
urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name="adminsite/login.html",
            authentication_form=LoginForm
            ),
        name='login'
),
   path('dashboard', TemplateView.as_view(template_name = 'adminsite/index.html'), name='dashboard')
]
