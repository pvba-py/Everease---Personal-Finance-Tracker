from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = 'flask-secret-placeholder'

users = {
    "demo_user": {"password": "demo123", "budget": None, "expenses": []},
    "test_user": {"password": "test123", "budget": None, "expenses": []},
    "john_doe": {"password": "password", "budget": None, "expenses": []},
    "jane_smith": {"password": "12345", "budget": None, "expenses": []}
}

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['user'] = username
            return redirect(url_for('set_budget'))  # Redirect to set budget after login
        else:
            flash("Invalid credentials. Try again.", "error")
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user' in session:
        user = session['user']
        budget = users[user]['budget']
        expenses = users[user]['expenses']
        
        # Redirect to set budget if it's not set
        if budget is None:
            flash("Please set a budget first.", "warning")
            return redirect(url_for('set_budget'))

        total_expenses = sum(expense['amount'] for expense in expenses)
        budget_status = "Within Budget" if not budget or total_expenses <= budget else "Over Budget"
        return render_template('home.html', user=user, expenses=expenses, budget=budget, budget_status=budget_status)
    return redirect(url_for('login'))

@app.route('/set_budget', methods=['GET', 'POST'])
def set_budget():
    if 'user' in session:
        user = session['user']
        if request.method == 'POST':
            budget = request.form.get('budget', '').strip()
            try:
                budget = float(budget)
                users[user]['budget'] = budget
                flash("Budget set successfully!", "success")
                return redirect(url_for('home'))
            except ValueError:
                flash("Invalid budget entered.", "error")
        return render_template('set_budget.html')
    return redirect(url_for('login'))

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if 'user' in session:
        user = session['user']

        # Ensure budget is set before adding expenses
        if users[user]['budget'] is None:
            flash("Please set a budget before adding expenses.", "error")
            return redirect(url_for('set_budget'))

        if request.method == 'POST':
            description = request.form.get('description', '').strip()
            amount = request.form.get('amount', '').strip()

            if not description or not amount:
                flash("All fields are required.", "error")
                return redirect(url_for('add_expense'))
            
            try:
                amount = float(amount)
            except ValueError:
                flash("Invalid amount entered.", "error")
                return redirect(url_for('add_expense'))
            
            expense = {'description': description, 'amount': amount}
            users[user]['expenses'].append(expense)
            flash("Expense added successfully!", "success")
            return redirect(url_for('home'))
        
        return render_template('add_expense.html')
    return redirect(url_for('login'))

@app.route('/view_summary')
def view_summary():
    if 'user' in session:
        user = session['user']
        budget = users[user]['budget']
        expenses = users[user]['expenses']
        total_expenses = sum(expense['amount'] for expense in expenses)
        budget_status = "Within Budget" if not budget or total_expenses <= budget else "Over Budget"
        return render_template('view_summary.html', budget=budget, total_expenses=total_expenses, expenses=expenses, budget_status=budget_status)
    return redirect(url_for('login'))

@app.route('/check_budget')
def check_budget():
    if 'user' in session:
        user = session['user']
        budget = users[user]['budget']
        total_expenses = sum(expense['amount'] for expense in users[user]['expenses'])
        budget_exceeded = total_expenses > budget if budget else False
        return render_template('check_budget.html', budget_exceeded=budget_exceeded)
    return redirect(url_for('login'))

@app.route('/loan_management')
def loan_management():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    user = session['user']
    loan_amount = users[user].get("loan_amount", "N/A")
    due_date = users[user].get("due_date", "Not Set")

    return render_template('loan_management.html', loan_amount=loan_amount, due_date=due_date)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('main_page'))

if __name__ == '__main__':
    app.run(debug=True)
