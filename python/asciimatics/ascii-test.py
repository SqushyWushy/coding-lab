from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Stars
from asciimatics.renderers import FigletText

def demo(screen):
    effects = [
        Stars(screen, 100),  # Background sparkle
        Print(screen, FigletText("T + J", font='big'), screen.height // 2 - 3)
    ]
    screen.play([Scene(effects, 5)])  # Show it for 5 seconds

Screen.wrapper(demo)
