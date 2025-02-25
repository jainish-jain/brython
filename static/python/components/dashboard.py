# components/dashboard.py
from browser import html
from datetime import datetime, date
from utils.currency_helpers import format_currency

class Dashboard:
    def __init__(self, db):
        self.db = db
        self.element = self.create_element()
        self.load_data()
    
    def create_element(self):
        dashboard = html.DIV(Class="dashboard")
        
        # Month summary card
        self.month_summary = html.DIV(Class="card month-summary")
        self.month_summary <= html.H2("This Month")
        self.month_expenses = html.DIV(Class="amount")
        self.month_summary <= self.month_expenses
        
        # Budget progress card
        self.budget_progress = html.DIV(Class="card budget-progress")
        self.budget_progress <= html.H2("Budget Progress")
        
        # Recent transactions
        self.recent_transactions = html.DIV(Class="card recent-transactions")
        self.recent_transactions <= html.H2("Recent Transactions")
        
        dashboard <= self.month_summary
        dashboard <= self.budget_progress
        dashboard <= self.recent_transactions
        
        return dashboard
    
    def load_data(self):
        # Load month's expenses
        def on_expenses_loaded(expenses):
            total = sum(exp['amount'] for exp in expenses)
            self.month_expenses.text = format_currency(total)
            
        self.db.get_expenses_for_month(date.today(), on_expenses_loaded)
        
        # Load budget progress
        def on_budget_loaded(budgets):
            self.update_budget_progress(budgets)
            
        self.db.get_current_budgets(on_budget_loaded)
        
        # Load recent transactions
        def on_transactions_loaded(transactions):
            self.show_recent_transactions(transactions)
            
        self.db.get_recent_transactions(5, on_transactions_loaded)