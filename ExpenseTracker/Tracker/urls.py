from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Homepage
    path('', views.home, name='home'),

    # Auth
    path('login/', auth_views.LoginView.as_view(
        template_name='Tracker/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Protected routes
    path('expenses/', views.expense_list, name='expense_list'),
]
