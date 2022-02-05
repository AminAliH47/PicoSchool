from django.urls import path

from quiz import views

app_name = "quiz"

urlpatterns = (
    path('list/', views.quiz_list, name='quiz_list'),
    path('<int:pk>/detail/', views.quiz_detail, name='quiz_detail'),
    path('detail/<int:pk>/<uuid>/', views.quiz_start, name='quiz_start'),
    path('create/', views.CreateQuiz.as_view(), name='quiz_create'),
    path('<int:pk>/update/', views.UpdateQuiz.as_view(), name='quiz_update'),
    # Questions Section
    path('questions/<int:pk>/list/', views.quiz_questions_list, name='quiz_questions_list'),
    path('questions/<int:pk>/update/', views.UpdateQuestion.as_view(), name='question_update'),
    path('questions-update/', views.update_question, name='update_question'),
    path('answers-update/', views.update_answers, name='update_answers'),
    path('create-answers/', views.create_answers, name='create_answers'),
    path('get-question/', views.get_questions, name='get_questions'),
    path('answers/', views.answers_data, name='answers_data'),
    # Result Section
    path('result/list/', views.result_list, name='result_list'),
    path('result/<pk>/<stu_pk>/detail/', views.result_detail, name='result_detail'),
    path('create-result/', views.create_result, name='create_result'),
    path('create-result-2/', views.create_result_2, name='create_result_2'),
    path('result-data/<int:pk>/', views.result_data, name='result_data'),
)
