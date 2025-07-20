from colorama import Fore, Style, init
import pyfiglet
import os

# Initialize colorama
init()

def print_banner():
    banner = pyfiglet.figlet_format("FocusBeast")
    print(Fore.RED + banner + Style.RESET_ALL)
    print(Fore.WHITE + "Unleash your discipline. One Pomodoro at a time. 🧠🔥\n" + Style.RESET_ALL)

def print_mode_options():
    print(Fore.CYAN + "Choose your mode:" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Classic Mode  (25 min focus / 5 min break)" + Style.RESET_ALL)
    print(Fore.MAGENTA + "2. Beast Mode    (50 min focus / 10 min break)\n" + Style.RESET_ALL)

def get_mode_settings(mode):
    if mode == "classic":
        return (25, 5)
    elif mode == "beast":
        return (50, 10)
    else:
        return (25, 5)

def print_colored(message, color):
    color_dict = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE
    }
    print(color_dict.get(color, Fore.WHITE) + message + Style.RESET_ALL)

def play_sound(path):
    try:
        os.system(f'afplay "{path}" &')  # play in background
    except Exception as e:
        print(f"🔕 Couldn't play sound: {e}")
