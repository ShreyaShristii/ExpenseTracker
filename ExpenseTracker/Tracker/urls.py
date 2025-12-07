from django.urls import path
from . import views

urlpatterns = [
    # Public root → always show login page
    path('', views.CustomLoginView.as_view(), name='login_page'),

    # Auth
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    # Protected pages
    path('home/', views.home, name='home'),
    path('expenses/', views.expense_list, name='expense_list'),
]
