import sqlite3
from tabulate import tabulate
from datetime import datetime
from utils import print_colored

DB_NAME = "focusbeast.db"

def show_stats():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    # Get all sessions
    cursor.execute("""
        SELECT date, start_time, end_time, duration, mode
        FROM sessions
        ORDER BY date DESC, start_time DESC
    """)
    rows = cursor.fetchall()

    if not rows:
        print_colored("📭 No sessions logged yet!", "red")
        return

    # Calculate total focus time for today
    cursor.execute("""
        SELECT SUM(duration)
        FROM sessions
        WHERE date = ?
    """, (today,))
    total_today = cursor.fetchone()[0] or 0

    # Count sessions
    cursor.execute("""
        SELECT COUNT(*)
        FROM sessions
        WHERE date = ?
    """, (today,))
    session_count = cursor.fetchone()[0]

    conn.close()

    # Print Summary
    print_colored(f"\n🧠 Focus Stats — {today}", "cyan")
    print_colored(f"Total Focused Today: {total_today} minutes", "green")
    print_colored(f"Total Sessions Today: {session_count}\n", "yellow")

    # Format table
    headers = ["Date", "Start", "End", "Duration (min)", "Mode"]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
