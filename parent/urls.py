from django.urls import path
from parent import views

app_name = 'parent'

urlpatterns = (
    path('', views.parent_view, name='parent_panel'),
)
