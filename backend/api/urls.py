from django.urls import path
from . import views

urlpatterns = [
    path('edit-todos/', views.edit_todos),
    path('return-users-PL/', views.return_users_PL),
    path('edit-PL/', views.edit_PL),
    path('register-user', views.register_user),
    path('login-user', views.login_user)
]
