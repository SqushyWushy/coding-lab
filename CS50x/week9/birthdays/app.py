import os
from cs50 import SQL
from flask import Flask, redirect, render_template, request

# Set up the app and database
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
db = SQL("sqlite:///birthdays.db")

@app.after_request
def after_request(response):
    # Don’t use old cached versions of the page
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the info from the form
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Basic check to make sure data is there
        if not name or not month or not day:
            return redirect("/")

        try:
            month = int(month)
            day = int(day)
        except ValueError:
            return redirect("/")

        # Make sure month and day are in good range
        if month < 1 or month > 12 or day < 1 or day > 31:
            return redirect("/")

        # Add to the database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)

        # Go back to the homepage
        return redirect("/")

    else:
        # Read all birthdays from the database
        birthdays = db.execute("SELECT * FROM birthdays")

        # Show them on the website
        return render_template("index.html", birthdays=birthdays)
