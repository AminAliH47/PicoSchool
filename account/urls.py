from django.contrib.auth.views import LogoutView
from django.urls import path
from account import views

app_name = 'account'

urlpatterns = (
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/password-change/', views.ChangePasswordView.as_view(), name='change_password'),
    path('user/password-done/', views.password_change_done, name="user_password_done"),
)
