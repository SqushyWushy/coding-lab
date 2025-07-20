import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]

    # Get user's current cash
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    # Get user's current stock holdings
    rows = db.execute("""
        SELECT symbol, SUM(shares) as total_shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
    """, user_id)

    holdings = []
    total_value = 0

    for row in rows:
        symbol = row["symbol"]
        shares = row["total_shares"]
        quote = lookup(symbol)
        price = quote["price"]
        total = shares * price
        total_value += total

        holdings.append({
            "symbol": symbol,
            "name": quote["name"],
            "shares": shares,
            "price": price,
            "total": total
        })

    grand_total = total_value + cash

    return render_template("index.html", holdings=holdings, cash=cash, total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")

    symbol = request.form.get("symbol")
    shares = request.form.get("shares")

    if not symbol:
        return apology("must provide a stock symbol")

    if not shares or not shares.isdigit() or int(shares) <= 0:
        return apology("must provide a positive number of shares")

    quote = lookup(symbol.upper())
    if quote is None:
        return apology("invalid stock symbol")

    price_per_share = quote["price"]
    total_cost = price_per_share * int(shares)

    # Get user's cash
    user_id = session["user_id"]
    user = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]

    if user["cash"] < total_cost:
        return apology("not enough cash")

    # Deduct cost
    db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)

    # Log transaction
    db.execute(
        "INSERT INTO transactions (user_id, symbol, shares, price, type) VALUES (?, ?, ?, ?, 'buy')",
        user_id, quote["symbol"], int(shares), price_per_share
    )

    flash("Purchase complete!")
    return redirect("/")


@app.route("/history")
@login_required
def history():
    user_id = session["user_id"]

    transactions = db.execute("""
        SELECT symbol, shares, price, type, timestamp
        FROM transactions
        WHERE user_id = ?
        ORDER BY timestamp DESC
    """, user_id)

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template("quote.html")

    symbol = request.form.get("symbol")

    if not symbol:
        return apology("must provide a stock symbol")

    quote = lookup(symbol)

    if quote is None:
        return apology("invalid stock symbol")

    return render_template("quoted.html", name=quote["name"], symbol=quote["symbol"], price=quote["price"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    # Get form inputs
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")

    # Validate inputs
    if not username:
        return apology("must provide username")
    if not password:
        return apology("must provide password")
    if password != confirmation:
        return apology("passwords do not match")

    # Try to insert user
    try:
        hashed = generate_password_hash(password)
        new_user_id = db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username, hashed
        )
    except:
        return apology("username already exists")

    # Log the user in automatically
    session["user_id"] = new_user_id

    return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    user_id = session["user_id"]

    if request.method == "GET":
        # Get list of stocks the user owns
        rows = db.execute("""
            SELECT symbol
            FROM transactions
            WHERE user_id = ?
            GROUP BY symbol
            HAVING SUM(shares) > 0
        """, user_id)
        symbols = [row["symbol"] for row in rows]
        return render_template("sell.html", stocks=symbols)

    # POST method
    symbol = request.form.get("symbol")
    shares = request.form.get("shares")

    if not symbol:
        return apology("must select a stock to sell")
    if not shares or not shares.isdigit() or int(shares) <= 0:
        return apology("invalid number of shares")

    shares = int(shares)

    # Check how many shares user owns
    owned = db.execute("""
        SELECT SUM(shares) as total
        FROM transactions
        WHERE user_id = ? AND symbol = ?
    """, user_id, symbol)[0]["total"]

    if owned is None or shares > owned:
        return apology("not enough shares")

    # Lookup price
    quote = lookup(symbol)
    price = quote["price"]
    total_value = price * shares

    # Update cash
    db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_value, user_id)

    # Record the transaction as a 'sell'
    db.execute(
        "INSERT INTO transactions (user_id, symbol, shares, price, type) VALUES (?, ?, ?, ?, 'sell')",
        user_id, symbol, -shares, price  # negative shares = selling
    )

    flash("Sold!")
    return redirect("/")

@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    if request.method == "GET":
        return render_template("add_cash.html")

    amount = request.form.get("amount")
    if not amount:
        return apology("must provide amount")

    try:
        amount = float(amount)
        if amount <= 0:
            return apology("must be positive")
    except ValueError:
        return apology("invalid amount")

    user_id = session["user_id"]

    db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", amount, user_id)

    flash(f"Successfully added {usd(amount)}!")
    return redirect("/")
