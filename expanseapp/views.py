from django.shortcuts import render, redirect
from django.contrib import *
from .models import *
from .forms import *
from django.contrib.auth import *
from django.contrib.auth.decorators import *

@login_required
def expense(request):
    all_expense = Expense.objects.all()
    print(all_expense)
    total_expence = sum(all_expense.values_list('amount', flat=True))
    print(total_expence)
    context = {"all_expense": all_expense,"total_expense": total_expence}
    return render(request, 'expense.html', context)


def del_views(request,id):
    print(id)
    obj = Expense.objects.get(id=id)
    obj.delete()
    messages.error(request, "deleted succesfuly")
    return redirect('expense')


def edit_views(request,id):
    print(id)
    obj = Expense.objects.get(id=id)
    print(obj.purpose)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance = obj)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("expense")
    form = ExpenseForm(instance = obj)
    context = {"form": form }
    return render(request, "edit.html", context)

def user_login(request):
    if request.method == "POST":
        username = request.POST["uname"]
        # print(username)
        password = request.POST["psw"]
        # print(password)
        user = authenticate(request, username = username, password = password)
        print(user)
        if user:
            user = login(request,user)
            return redirect("expense")

    return render(request, "login.html")


def log_out(request):
    logout(request)
    return redirect("login")