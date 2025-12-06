from django.shortcuts import render
from .models import Expense   # <-- REQUIRED import

def home(request):
    return render(request, 'Tracker/home.html')

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'Tracker/expense_list.html', {'expenses': expenses})
