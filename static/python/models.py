# models.py
from browser import window
from datetime import datetime

class Database:
    def __init__(self):
        self.db = None
        self.init_db()
    
    def init_db(self):
        indexedDB = window.indexedDB
        request = indexedDB.open("MyMoneyDB", 1)
        
        def on_upgrade_needed(event):
            db = event.target.result
            
            # Expenses store
            if not "expenses" in db.objectStoreNames:
                expense_store = db.createObjectStore("expenses", 
                    keyPath="id", autoIncrement=True)
                expense_store.createIndex("date", "date")
                expense_store.createIndex("category", "category")
                
            # Budget store
            if not "budgets" in db.objectStoreNames:
                budget_store = db.createObjectStore("budgets",
                    keyPath="id", autoIncrement=True)
                budget_store.createIndex("category", "category")
                budget_store.createIndex("period", "period")
                
            # Categories store
            if not "categories" in db.objectStoreNames:
                category_store = db.createObjectStore("categories",
                    keyPath="id", autoIncrement=True)
                
        request.bind("upgradeneeded", on_upgrade_needed)