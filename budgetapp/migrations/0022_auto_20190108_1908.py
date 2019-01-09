# Generated by Django 2.1.2 on 2019-01-09 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budgetapp', '0021_auto_20181115_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='budgetgoal',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='budgetgoal',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='budgetgoal',
            name='long_term_goal',
        ),
        migrations.RemoveField(
            model_name='income',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='longtermgoal',
            name='owner',
        ),
        migrations.AddField(
            model_name='transaction',
            name='inflow',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='budget',
            name='year',
            field=models.IntegerField(default=2019),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='budget_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgetapp.BudgetCategory'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgetapp.Payee'),
        ),
        migrations.DeleteModel(
            name='BudgetGoal',
        ),
        migrations.DeleteModel(
            name='Income',
        ),
        migrations.DeleteModel(
            name='LongTermGoal',
        ),
    ]