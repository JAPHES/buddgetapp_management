from django.shortcuts import render
from .forms import BudgetForm

def budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save()  # Save to database
            return render(request, 'budget/budget_result.html', {'budget': budget})
    else:
        form = BudgetForm()
    return render(request, 'budget/budget_form.html', {'form': form})
