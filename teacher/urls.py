from django.urls import path, include
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.teacher_view, name='teacher_panel'),
]
