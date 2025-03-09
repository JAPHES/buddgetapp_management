from django.db import models

# Create your models here.
class Budget(models.Model):
    salary = models.FloatField()
    housing = models.FloatField()
    food = models.FloatField()
    transport = models.FloatField()
    other = models.FloatField()

    def total_expenses(self):
        return self.housing + self.food + self.transport + self.other

    def remaining_balance(self):
        return self.salary - self.total_expenses()

    def budget_breakdown(self):
        return {
            "Savings (20%)": self.salary * 0.2,
            "Needs (50%)": self.salary * 0.5,
            "Wants (30%)": self.salary * 0.3,
        }

    def needs_breakdown(self):
        needs = self.salary * 0.5
        return {
            "Rent (49%)": needs * 0.49,
            "Fare (12%)": needs * 0.12,
            "Utilities (6%)": needs * 0.06,
            "Debt (7%)": needs * 0.07,
            "Groceries (15%)": needs * 0.15,
            "Personal care (5%)": needs * 0.05,
            "Gas (6%)": needs * 0.06,
        }

    def wants_breakdown(self):
        wants = self.salary * 0.3
        return {
            "Eating Out (37%)": wants * 0.37,
            "Entertainment (40%)": wants * 0.4,
            "New Clothing (23%)": wants * 0.23,
        }

    def __str__(self):
        return f"Budget for {self.salary}"
