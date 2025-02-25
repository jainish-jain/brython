# main.py
from browser import document, html, window
from components.dashboard import Dashboard
from components.expense_form import ExpenseForm
from components.budget_form import BudgetForm
from components.category_manager import CategoryManager
from components.reports import Reports
from models import Database

class MyMoneyApp:
    def __init__(self):
        self.db = Database()
        self.current_view = 'dashboard'
        self.setup_ui()
        
    def setup_ui(self):
        self.container = document["app"]
        self.setup_navigation()
        self.load_view('dashboard')
    
    def setup_navigation(self):
        nav = html.NAV(Class="bottom-nav")
        
        nav_items = [
            ("dashboard", "Dashboard", self.show_dashboard),
            ("expenses", "Expenses", self.show_expenses),
            ("budgets", "Budgets", self.show_budgets),
            ("reports", "Reports", self.show_reports),
            ("categories", "Categories", self.show_categories)
        ]
        
        for id, label, handler in nav_items:
            button = html.BUTTON(label, Class="nav-button")
            button.bind("click", lambda ev, h=handler: h())
            nav <= button
            
        self.container <= nav
    
    def load_view(self, view_name):
        self.container.clear()
        self.current_view = view_name
        
        if view_name == 'dashboard':
            self.container <= Dashboard(self.db).element
        elif view_name == 'expenses':
            self.container <= ExpenseForm(self.db).element
        elif view_name == 'budgets':
            self.container <= BudgetForm(self.db).element
        elif view_name == 'reports':
            self.container <= Reports(self.db).element
        elif view_name == 'categories':
            self.container <= CategoryManager(self.db).element
            
        self.setup_navigation()

app = MyMoneyApp()