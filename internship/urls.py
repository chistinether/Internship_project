from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.home, name='home'),

    path('redirect-dashboard/', views.redirect_dashboard, name='redirect_dashboard'),

    path('dashboard/', views.student_dashboard, name='student_dashboard'),

    path('submit-report/', views.submit_report, name='submit_report'),

    path('supervisor/', views.supervisor_dashboard, name='supervisor_dashboard'),

    path('feedback/<int:report_id>/', views.give_feedback, name='give_feedback'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.student_register, name='student_register'),
]