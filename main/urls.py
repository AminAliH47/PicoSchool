from django.urls import path
from main import views

app_name = 'main'

urlpatterns = (
    path('', views.index, name='index'),
    path('pages/events/', views.events, name='events'),
    path('pages/notices/', views.notice_box, name='notices'),
    # Student Section
    path('student/<int:pk>/detail/', views.student_detail, name="student_detail"),
    # Parent Section
    path('parent/<int:pk>/detail/', views.parent_detail, name="parent_detail"),
    # Parent Section
    path('teacher/<int:pk>/detail/', views.teacher_detail, name="teacher_detail"),
    # Class Section
    path('class/list/', views.class_list, name="class_list"),
    path('class/<int:pk>/detail/', views.class_detail, name="class_detail"),
    # Attendance Section
    path('attendance/<int:pk>/<date>/detail/', views.attendance_detail, name="attendance_detail"),
    # Home Work Section
    path('home-work/list/', views.home_work_list, name="home_work_list"),
    path('home-work/<int:pk>/detail/', views.home_work_detail, name="home_work_detail"),
    # Employment Form Section
    path('employment-form/list/', views.employment_form_list, name="employment_form_list"),
    path('employment-form/<int:pk>/detail/', views.employment_form_detail, name="employment_form_detail"),
    # News
    path('news/list/', views.news_list, name="news_list"),
)
