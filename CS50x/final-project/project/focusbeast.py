import argparse
from timer import run_focus_session, run_break_session
from database import init_db
from history import show_stats
from utils import print_banner, print_mode_options, get_mode_settings, print_colored

def main():
    # CLI Flags
    parser = argparse.ArgumentParser(description="FocusBeast CLI Pomodoro Timer")
    parser.add_argument("--stats", action="store_true", help="Show session history and focus stats")
    args = parser.parse_args()

    # Handle stats flag
    if args.stats:
        show_stats()
        return

    # ASCII banner
    print_banner()

    # Ensure DB exists
    init_db()

    # Mode selection
    print_mode_options()
    mode_choice = input("Your choice (1 or 2): ").strip()
    while mode_choice not in ["1", "2"]:
        mode_choice = input("Invalid choice. Please enter 1 or 2: ").strip()

    mode = "classic" if mode_choice == "1" else "beast"
    focus_minutes, break_minutes = get_mode_settings(mode)

    # Rounds
    try:
        rounds = int(input("How many rounds would you like to do? ").strip())
    except ValueError:
        print_colored("⚠️ Invalid input. Defaulting to 1 round.\n", "red")
        rounds = 1

    print_colored(f"\n🔥 Starting {mode.title()} Mode — {rounds} round(s)!\n", "green")

    try:
        for round_num in range(1, rounds + 1):
            print_colored(f"🔁 Round {round_num}/{rounds} — Focus Time!", "yellow")
            interrupted = run_focus_session(focus_minutes, mode)
            if interrupted:
                break

            if round_num < rounds:
                print_colored("☕ Break Time!", "cyan")
                if run_break_session(break_minutes):
                    break

        print_colored("\n🎉 All rounds complete! Great job!\n", "magenta")

    except KeyboardInterrupt:
        print_colored("\n🛑 Session interrupted. Logging partial progress...\n", "red")

    print_colored("View your stats with: python focusbeast.py --stats\n", "white")

if __name__ == "__main__":
    main()
