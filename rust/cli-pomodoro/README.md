# 🍅 PomoRust

A minimalist Pomodoro timer built in Rust for personal use.

This CLI tool runs a customizable Pomodoro session directly in the terminal, showing a live countdown and alternating between focus and break periods. Built for deep work, distraction-free coding, and keeping sessions tight without switching apps.

---

## Features

- ⏱️ Customizable durations (`--work`, `--break`)
- 🧠 Clean real-time countdown
- ✅ Session complete notifications
- ⚡ No GUI, no distractions — just terminal flow

---

## Usage

Run with default settings (25min work / 5min break):

```bash
cargo run

Or specify custom durations:

cargo run -- --work 50 --break 10


⸻

Options

Flag	Description	Default
--work, -w	Work session length in minutes	25
--break, -b	Break session length in minutes	5


⸻

Tech Stack
	•	clap — command-line argument parsing
	•	crossterm — terminal cursor + clearing
	•	std::time, std::thread — for countdown logic

⸻

Notes

This is a personal project I use to stay focused while coding. It lives in my terminal, runs fast, and doesn’t try to do too much. No GUI. No distractions. Just you and the clock.

⸻
```
