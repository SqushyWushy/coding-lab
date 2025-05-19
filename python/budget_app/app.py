from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Data storage paths
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
IMG_DIR = os.path.join(STATIC_DIR, 'img')

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

BUDGET_FILE = os.path.join(DATA_DIR, 'budget.json')
TRANSACTIONS_FILE = os.path.join(DATA_DIR, 'transactions.json')
SAVINGS_GOALS_FILE = os.path.join(DATA_DIR, 'savings_goals.json')

# Initialize data files if they don't exist
def init_data_files():
    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, 'w') as f:
            json.dump({
                'income': {'Partner 1': 0, 'Partner 2': 0},
                'categories': [
                    {'name': 'Housing', 'amount': 0},
                    {'name': 'Food', 'amount': 0},
                    {'name': 'Transportation', 'amount': 0},
                    {'name': 'Entertainment', 'amount': 0},
                    {'name': 'Utilities', 'amount': 0},
                    {'name': 'Savings', 'amount': 0},
                    {'name': 'Miscellaneous', 'amount': 0}
                ]
            }, f)
    
    if not os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, 'w') as f:
            json.dump([], f)
    
    if not os.path.exists(SAVINGS_GOALS_FILE):
        with open(SAVINGS_GOALS_FILE, 'w') as f:
            json.dump([
                {'name': 'Summer Camp', 'target': 0, 'current': 0}
            ], f)

# Load data from files
def load_budget():
    with open(BUDGET_FILE, 'r') as f:
        return json.load(f)

def load_transactions():
    with open(TRANSACTIONS_FILE, 'r') as f:
        return json.load(f)

def load_savings_goals():
    with open(SAVINGS_GOALS_FILE, 'r') as f:
        return json.load(f)

# Save data to files
def save_budget(budget):
    with open(BUDGET_FILE, 'w') as f:
        json.dump(budget, f)

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, 'w') as f:
        json.dump(transactions, f)

def save_savings_goals(goals):
    with open(SAVINGS_GOALS_FILE, 'w') as f:
        json.dump(goals, f)

@app.route('/')
def index():
    init_data_files()
    budget = load_budget()
    transactions = load_transactions()
    goals = load_savings_goals()
    
    # Calculate spending by category for current month
    current_month = datetime.now().strftime('%Y-%m')
    spending_by_category = {}
    for category in budget['categories']:
        spending_by_category[category['name']] = 0
    
    for transaction in transactions:
        if transaction['date'].startswith(current_month) and transaction['type'] == 'expense':
            if transaction['category'] in spending_by_category:
                spending_by_category[transaction['category']] += transaction['amount']
    
    # Calculate total income and expenses
    total_income = budget['income']['Partner 1'] + budget['income']['Partner 2']
    total_budget = sum(category['amount'] for category in budget['categories'])
    total_spent = sum(spending_by_category.values())
    remaining = total_income - total_spent
    
    # Current datetime for the template
    now = datetime.now()
    
    return render_template('index.html', 
                           budget=budget, 
                           spending=spending_by_category, 
                           transactions=sorted(transactions, key=lambda x: x['date'], reverse=True)[:10],
                           goals=goals,
                           total_income=total_income,
                           total_budget=total_budget,
                           total_spent=total_spent,
                           remaining=remaining,
                           now=now)

@app.route('/budget', methods=['GET', 'POST'])
def edit_budget():
    if request.method == 'POST':
        budget = load_budget()
        budget['income']['Partner 1'] = float(request.form.get('income_partner1', 0))
        budget['income']['Partner 2'] = float(request.form.get('income_partner2', 0))
        
        # Update categories
        for i, category in enumerate(budget['categories']):
            category_name = request.form.get(f'category_name_{i}')
            category_amount = float(request.form.get(f'category_amount_{i}', 0))
            if category_name:  # Only update if name is provided
                category['name'] = category_name
                category['amount'] = category_amount
        
        # Add new category if provided
        new_category_name = request.form.get('new_category_name')
        new_category_amount = float(request.form.get('new_category_amount', 0))
        if new_category_name:
            budget['categories'].append({
                'name': new_category_name,
                'amount': new_category_amount
            })
        
        save_budget(budget)
        flash('Budget updated successfully!', 'success')
        return redirect(url_for('index'))
    
    budget = load_budget()
    now = datetime.now()
    return render_template('budget.html', budget=budget, now=now)

@app.route('/transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transactions = load_transactions()
        budget = load_budget()
        
        transaction_type = request.form['type']
        amount = float(request.form['amount'])
        category = request.form['category']
        description = request.form['description']
        date = request.form['date']
        
        transactions.append({
            'type': transaction_type,
            'amount': amount,
            'category': category,
            'description': description,
            'date': date,
            'timestamp': datetime.now().isoformat()
        })
        
        save_transactions(transactions)
        
        # Update savings goal if transaction is related to a savings category
        if category == 'Savings' and transaction_type == 'expense':
            goals = load_savings_goals()
            goal_name = request.form.get('savings_goal')
            if goal_name:
                for goal in goals:
                    if goal['name'] == goal_name:
                        goal['current'] += amount
                        break
                save_savings_goals(goals)
        
        flash('Transaction added successfully!', 'success')
        return redirect(url_for('index'))
    
    budget = load_budget()
    goals = load_savings_goals()
    
    # Get today's date in YYYY-MM-DD format for the date input
    now = datetime.now()
    today = now.strftime('%Y-%m-%d')
    
    return render_template('transaction.html', 
                           categories=[category['name'] for category in budget['categories']],
                           goals=goals,
                           today=today,
                           now=now)

@app.route('/goals', methods=['GET', 'POST'])
def manage_goals():
    if request.method == 'POST':
        goals = load_savings_goals()
        
        # Update existing goals
        for i, goal in enumerate(goals):
            goal_name = request.form.get(f'goal_name_{i}')
            goal_target = float(request.form.get(f'goal_target_{i}', 0))
            if goal_name:  # Only update if name is provided
                goal['name'] = goal_name
                goal['target'] = goal_target
        
        # Add new goal if provided
        new_goal_name = request.form.get('new_goal_name')
        new_goal_target = float(request.form.get('new_goal_target', 0))
        if new_goal_name:
            goals.append({
                'name': new_goal_name,
                'target': new_goal_target,
                'current': 0
            })
        
        save_savings_goals(goals)
        flash('Savings goals updated successfully!', 'success')
        return redirect(url_for('index'))
    
    goals = load_savings_goals()
    now = datetime.now()
    return render_template('goals.html', goals=goals, now=now)

@app.route('/reports')
def reports():
    budget = load_budget()
    transactions = load_transactions()
    
    # Calculate data for reports
    categories = [category['name'] for category in budget['categories']]
    
    # Monthly spending by category
    monthly_spending = {}
    for transaction in transactions:
        if transaction['type'] == 'expense':
            month = transaction['date'][:7]  # Extract YYYY-MM
            category = transaction['category']
            
            if month not in monthly_spending:
                monthly_spending[month] = {cat: 0 for cat in categories}
            
            if category in monthly_spending[month]:
                monthly_spending[month][category] += transaction['amount']
    
    # Sort months chronologically
    sorted_months = sorted(monthly_spending.keys())
    
    now = datetime.now()
    return render_template('reports.html', 
                           categories=categories,
                           months=sorted_months,
                           monthly_spending=monthly_spending,
                           now=now)

if __name__ == '__main__':
    app.run(debug=True)