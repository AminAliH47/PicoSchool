from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
    path('', views.student_view, name='student_panel'),
    # Employment Form Section
    path('create-emp-form/', views.create_emp_form, name='create_emp_form'),
]
