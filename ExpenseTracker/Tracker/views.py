
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

from .models import Expense

# --------------------------
# AUTHENTICATION VIEWS
# --------------------------

class CustomLoginView(LoginView):
    template_name = 'Tracker/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    pass


def register(request):
    if request.user.is_authenticated:
        return redirect('expense_list')

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('expense_list')

    return render(request, 'Tracker/register.html', {'form': form})


# --------------------------
# PROTECTED VIEWS
# --------------------------

@login_required
def home(request):
    return render(request, 'Tracker/home.html')


@login_required
def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'Tracker/expense_list.html', {'expenses': expenses})
