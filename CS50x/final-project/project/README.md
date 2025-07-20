# FocusBeast

#### Video Demo: https://youtu.be/kOUViIRqdM0

#### Description: **FocusBeast** is a terminal-based Pomodoro timer designed to help users stay laser-focused and track their productivity over time. Unlike simple timers, FocusBeast offers a premium CLI experience with ASCII art, colored output, session history logging, and sound alerts.

⸻

Motivation

I wanted to build something I would genuinely use. I often work from the terminal and wanted a distraction-free timer that looked great, didn’t require a GUI or browser, and could actually track my discipline. Most Pomodoro apps don’t log anything — this one does.

This project allowed me to bring together everything I’ve learned in CS50 — Python scripting, database work, file structure, logic, argument parsing, and designing for real users (myself included).

⸻

⚙️ How to Run

1. Clone the repo and enter the directory:

git clone https://github.com/SqushyWushy/coding-lab.git
cd focusbeast

2. Install dependencies:

pip install -r requirements.txt

3. Run the program:

python focusbeast.py

Or, to view your stats:

python focusbeast.py --stats

⸻

File Overview

File Description
focusbeast.py Main entry point, handles CLI logic and session flow
timer.py Countdown logic for focus and break sessions
utils.py Utility functions like color printing and sound playing
database.py SQLite setup and logging logic
history.py Logic for viewing session stats
schema.sql SQL schema for creating the sessions table
requirements.txt Dependencies (colorama, etc.)
sounds/ Sound files for focus/break transitions
focusbeast.db SQLite database file for session history (auto-generated)
README.md This file! Describes project purpose and usage

⸻

Features

- CLI countdown timer with ASCII art and colors
- Select Classic (25/5) or Beast (50/10) mode
- Sound notifications when sessions complete
- Tracks session history in SQLite
- View total focus time and stats with --stats flag
- Graceful handling of interruptions (e.g. Ctrl+C)

⸻

What I Learned

- This project helped me master:
- Argument parsing (argparse)
- So much patience ;)
- SQLite CRUD operations in Python
- Structuring multi-file Python projects
- Building CLI tools with polish
- Error handling and user experience

⸻

AI and Code Acknowledgments

Parts of this project were inspired by various Pomodoro CLI apps. I used ChatGPT occasionally for troubleshooting bugs and brainstorming CLI design ideas, but all code was written and fully understood by me.

⸻

Next Steps

If I had more time, I’d like to:

- Add a config file to customize session lengths
- Add weekly/monthly stats view
- Add terminal notifications on macOS/Linux

⸻
