from django.urls import path
from . import views

from django.views.generic import TemplateView


urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.SignUp, name='register'),

    path('password_change/', views.change_password, name='password_change'),
    path('password_change/done/', TemplateView.as_view(template_name='accounts/registration/password_change_done.html'), name='password_change_done'),


    #dashboard
    path('dashboard/', views.UserDashboard, name='dashboard'),
    path('update/', views.update_profile, name='update-profile'),

]