# FocusBeast: A Premium CLI Pomodoro Timer

#### Video Demo: https://youtu.be/kOUViIRqdM0

#### Description:

**FocusBeast** is a terminal-based Pomodoro timer designed to help users stay laser-focused and track their productivity over time. Unlike simple timers, FocusBeast offers a premium CLI experience with ASCII art, colored output, session history logging, and sound alerts.

Users can choose between two Pomodoro styles:

- **Classic Mode**: 25-minute focus + 5-minute break
- **Beast Mode**: 50-minute focus + 10-minute break

At the start, the app prompts users for their preferred mode and how many rounds they want to complete. For each round, it runs a countdown timer for the focus session and then for the break, playing a sound at the end of each phase. At the end of every focus session, a log entry is saved to a local SQLite database, saving the date, time, duration, and mode.

To view progress, users can run the app with a `--stats` flag to display a formatted breakdown of their session history and total focus time — all within the terminal.

---

## 📦 Features

- 🧠 Focus and break countdown timers
- 🎛️ Choice of "Classic" or "Beast" mode
- 🔁 Support for multiple rounds in one session
- 🗃️ SQLite-powered session tracking
- 🎨 Beautiful ASCII + color CLI UI
- 🔔 Sound notifications when timers end
- 📊 CLI stats view for daily focus history

---

## Why This Project?

I wanted to build a tool that I would actually use — something fast, clean, and focused. The Pomodoro technique is powerful, but most apps are bloated or browser-based. I wanted something I could run in the terminal that felt satisfying to use and helped me stay accountable with real data.

This project combines many of the concepts I’ve learned in CS50:

- Python scripting and modules
- SQLite database integration
- File and module organization
- CLI programs
- Argument parsing and flow control

---

## 🚀 How to Run

### Install dependencies:

```bash
pip install -r requirements.txt
```
