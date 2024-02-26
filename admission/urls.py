from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', index, name='home'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('admission/', admission, name='admission'),
    path('feeedback/', feedback, name='feedback'),
]