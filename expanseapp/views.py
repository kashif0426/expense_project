from django.shortcuts import render
from .models import *
# Create your views here.
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
    pass