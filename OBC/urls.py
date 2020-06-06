from django.urls import path
from .views import IndexView, StudentEntryView

app_name = 'obc'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('obcform', StudentEntryView.as_view(), name='form')
]
