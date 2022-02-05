from django.urls import path
from account.views import password_change_done
from manager import views

app_name = 'manager'

urlpatterns = (
    path('', views.manager_panel, name='manager_panel'),
    # Calendar section
    path('calendar/', views.calendar, name='calendar'),
    path('add-event/', views.add_event, name='add_event'),
    path('add-ex-event/', views.add_external_event, name='add_external_event'),
    path('update-event/', views.update_event, name='update_event'),
    path('update-event-desc/', views.update_event_desc, name='update_event_desc'),
    path('delete-event/', views.delete_event, name='delete_event'),
    path('delete-ex-event/', views.delete_ex_event, name='delete_ex_event'),
    # Notice Box section
    path('add-notice/', views.add_notice, name='add_notice'),
    path('edit-notice/', views.edit_notice, name='edit_notice'),
    path('delete-notice/', views.delete_notice, name='delete_notice'),
    # Student section
    path('student/list/', views.student_list, name="student_list"),
    path('student/create/', views.CreateStudent.as_view(), name="student_create"),
    path('student/<int:pk>/change', views.UpdateStudent.as_view(), name="student_update"),
    path('student/<int:pk>/delete', views.DeleteStudent.as_view(), name="student_delete"),
    # Parent section
    path('parent/list/', views.parent_list, name="parent_list"),
    path('parent/create/', views.CreateParent.as_view(), name="parent_create"),
    path('parent/<int:pk>/change', views.UpdateParent.as_view(), name="parent_update"),
    path('parent/<int:pk>/delete', views.DeleteParent.as_view(), name="parent_delete"),
    # Teacher section
    path('teacher/list/', views.teacher_list, name="teacher_list"),
    path('teacher/create/', views.CreateTeacher.as_view(), name="teacher_create"),
    path('teacher/<int:pk>/change', views.UpdateTeacher.as_view(), name="teacher_update"),
    path('teacher/<int:pk>/delete', views.DeleteTeacher.as_view(), name="teacher_delete"),
    # Persons Section
    path('user/<int:pk>/password/', views.password_change, name="user_password"),
    path('password-done/', password_change_done, name="user_password_done"),
    # Attendance Section
    path('change-att-status/', views.change_att_status, name='change_att_status'),
    path('add-att-status/', views.add_att_status, name='add_att_status'),
    path('create-att/', views.create_att, name='create_att'),
    path('change-att-note/', views.change_att_note, name='change_att_note'),
    # Report Card Section
    path('report-card/', views.report_card, name='report_card'),
    # Home Work Section
    path('create-hw/', views.create_hw, name='create_hw'),
    # Employment Form Section
    path('upload-emp-form/', views.upload_emp_form, name='upload_emp_form'),
)
