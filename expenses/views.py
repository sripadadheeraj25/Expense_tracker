import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm
import json
from datetime import date

def expense_list(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user)
    else:
        expenses = Expense.objects.none()
    # rest stays the same...

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # link to logged in user
            expense.save()
            return redirect('expense-list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form})

@login_required
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)  # only own expenses
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense-list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_form.html', {'form': form})

@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)  # only own expenses
    if request.method == 'POST':
        expense.delete()
        return redirect('expense-list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})

@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expenses.csv"'
    writer = csv.writer(response)
    writer.writerow(['Title', 'Amount', 'Category', 'Date', 'Notes'])
    expenses = Expense.objects.filter(user=request.user)  # only own expenses
    for expense in expenses:
        writer.writerow([
            expense.title,
            expense.amount,
            expense.get_category_display(),
            expense.date,
            expense.notes or '',
        ])
    return response