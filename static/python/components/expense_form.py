# components/expense_form.py
from browser import html, window
from datetime import datetime
from utils.currency_helpers import format_currency

class ExpenseForm:
    def __init__(self, db):
        self.db = db
        self.element = self.create_element()
        self.load_categories()
    
    def create_element(self):
        form = html.FORM(Class="expense-form")
        
        # Amount input
        amount_group = html.DIV(Class="form-group")
        amount_group <= html.LABEL("Amount")
        self.amount_input = html.INPUT(type="number", step="0.01")
        amount_group <= self.amount_input
        
        # Category select
        category_group = html.DIV(Class="form-group")
        category_group <= html.LABEL("Category")
        self.category_select = html.SELECT()
        category_group <= self.category_select
        
        # Date input
        date_group = html.DIV(Class="form-group")
        date_group <= html.LABEL("Date")
        self.date_input = html.INPUT(type="date")
        self.date_input.value = datetime.now().strftime("%Y-%m-%d")
        date_group <= self.date_input
        
        # Note input
        note_group = html.DIV(Class="form-group")
        note_group <= html.LABEL("Note")
        self.note_input = html.INPUT(type="text")
        note_group <= self.note_input
        
        # Submit button
        submit_btn = html.BUTTON("Add Expense", type="submit")
        submit_btn.bind("click", self.handle_submit)
        
        form <= amount_group
        form <= category_group
        form <= date_group
        form <= note_group
        form <= submit_btn
        
        return form
    
    def load_categories(self):
        def on_categories_loaded(categories):
            self.category_select.clear()
            for category in categories:
                option = html.OPTION(category['name'])
                option.value = category['id']
                self.category_select <= option
                
        self.db.get_categories(on_categories_loaded)
    
    def handle_submit(self, event):
        event.preventDefault()
        
        expense = {
            'amount': float(self.amount_input.value),
            'category': self.category_select.value,
            'date': self.date_input.value,
            'note': self.note_input.value
        }
        
        def on_saved():
            # Clear form
            self.amount_input.value = ""
            self.note_input.value = ""
            window.alert("Expense saved successfully!")
            
        self.db.save_expense(expense, on_saved)