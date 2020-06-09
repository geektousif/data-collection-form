from django.urls import path
from .views import IndexView, StudentNew

app_name = 'obc'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('obcform', StudentNew.as_view(), name='form')
]
