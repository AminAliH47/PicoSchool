from django.urls import path
from poll import views

app_name = 'poll'

urlpatterns = (
    path('list/', views.poll_list, name='poll_list'),
    path('options/<int:pk>/list/', views.poll_options_list, name='poll_options_list'),
    path('create/', views.PollCreate.as_view(), name='poll_create'),
    path('update/<int:pk>/', views.PollUpdate.as_view(), name='poll_update'),
    path('vote/<int:pk>/', views.poll_vote, name='poll_vote'),
    path('result/<int:pk>/', views.poll_result, name='poll_result'),
)
