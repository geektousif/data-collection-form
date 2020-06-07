from django.urls import path
from .views import IndexView, post_new

app_name = 'obc'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('obcform', post_new, name='form')
]
