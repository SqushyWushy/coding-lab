import time
import sys
from datetime import datetime
from database import log_session
from utils import print_colored, play_sound

def countdown(minutes):
    total_seconds = int(minutes * 60)
    try:
        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            timer_str = f"{int(mins):02d}:{int(secs):02d}"
            print(f"\r⏳ Time left: {timer_str}   ", end="")
            sys.stdout.flush()
            time.sleep(1)
            total_seconds -= 1
        print("\r✅ Done!                     ")
        return False  # not interrupted
    except KeyboardInterrupt:
        print_colored("\n🛑 Timer interrupted by user.\n", "red")
        return True  # interrupted

def run_focus_session(focus_minutes, mode):
    print_colored("💡 (Press Ctrl+C to quit early)\n", "cyan")
    start_time = datetime.now()
    interrupted = countdown(focus_minutes)
    end_time = datetime.now()
    duration = (end_time - start_time).seconds // 60

    # Always log session
    log_session(start_time, end_time, duration, mode)

    if not interrupted:
        play_sound("sounds/focus_end.wav")
        print_colored("\n✅ Focus session complete!", "green")
    else:
        print_colored("\n⚠️ Partial focus session logged.", "red")

    return interrupted

def run_break_session(break_minutes):
    print_colored("💤 Break started.\n", "cyan")
    interrupted = countdown(break_minutes)

    if not interrupted:
        play_sound("sounds/break_end.wav")
        print_colored("\n🔔 Break over. Back to the grind!", "yellow")
    else:
        print_colored("\n⚠️ Break was interrupted.", "red")

    return interrupted
