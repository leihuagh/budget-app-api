from datetime import datetime

from django.db import models


class Budget(models.Model):
    related_name = 'budgets'

    MONTH_CHOICES = (
        ('JAN', 'January'),
        ('FEB', 'February'),
        ('MAR', 'March'),
        ('APR', 'April'),
        ('MAY', 'May'),
        ('JUN', 'June'),
        ('JUL', 'July'),
        ('AUG', 'August'),
        ('SEP', 'September'),
        ('OCT', 'October'),
        ('NOV', 'November'),
        ('DEC', 'December')
    )

    month = models.CharField(
        max_length=100,
        choices=MONTH_CHOICES,
        default='JAN',
    )
    year = models.IntegerField(default=datetime.now().year)
    owner = models.ForeignKey(
        'auth.User', related_name=related_name, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('owner', 'month', 'year')

    def __str__(self):  # pragma: no cover
        return self.owner.username + \
               '\'s ' + \
               str(self.month) + \
               ' ' + \
               str(self.year) + \
               ' Budget'


class BudgetCategoryGroup(models.Model):
    related_name = 'budget_category_groups'
    name = models.CharField(max_length=100)
    budget = models.ForeignKey(
        Budget, on_delete=models.CASCADE, related_name=related_name
    )

    @property
    def owner(self):
        return self.budget.owner

    class Meta:
        unique_together = ('name', 'budget',)

    def __str__(self):  # pragma: no cover
        return self.name + ' [owner=' + self.budget.owner.username + ']'


class BudgetCategory(models.Model):
    related_name = 'budget_categories'
    category = models.CharField(max_length=100)
    group = models.ForeignKey(
        BudgetCategoryGroup,
        on_delete=models.CASCADE,
        related_name=related_name
    )
    limit = models.DecimalField(
        max_digits=20, decimal_places=2, default=0
    )
    spent = models.DecimalField(
        max_digits=20, decimal_places=2, default=0
    )

    @property
    def remaining(self):
        return self.limit - self.spent

    @property
    def owner(self):
        return self.group.budget.owner

    def __str__(self):  # pragma: no cover
        return str(self.category) + ' ' + \
               self.group.budget.month + ' ' + \
               str(self.group.budget.year) + \
               ' [owner=' + self.group.budget.owner.username + ']'


class Transaction(models.Model):
    related_name = 'transactions'
    amount = models.DecimalField(
        max_digits=20, decimal_places=2
    )
    recipient = models.ForeignKey('Payee', on_delete=models.CASCADE)
    budget_category = models.ForeignKey(
        'BudgetCategory', on_delete=models.CASCADE
    )
    date = models.DateField()
    inflow = models.BooleanField()

    @property
    def owner(self):
        return self.budget_category.group.budget.owner

    def __str__(self):  # pragma: no cover
        return str(self.amount) + ' ' \
               + self.recipient.name + ' ' \
               + str(self.budget_category) + ' ' \
               + str(self.date) + ' ' \
               + self.budget_category.group.budget.owner.username + ' ' \
               + self.inflow


class Payee(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
