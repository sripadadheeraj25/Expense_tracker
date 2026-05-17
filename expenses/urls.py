from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense-list'),
    path('add/', views.add_expense, name='add-expense'),
    path('edit/<int:pk>/', views.edit_expense, name='edit-expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete-expense'),

    path('login/', auth_views.LoginView.as_view(
        template_name='expenses/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('export/', views.export_csv, name='export-csv'),
]