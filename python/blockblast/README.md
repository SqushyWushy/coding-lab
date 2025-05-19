# Block Blast Game

A polished block-matching puzzle game built with Python and Pygame. Match blocks, earn points, and advance through increasingly challenging levels!

![Block Blast Screenshot](screenshot.png)

## Features

- Intuitive block-matching gameplay
- Beautiful visual effects and animations
- Combo system for strategic play
- Level progression with increasing difficulty
- Score tracking and high score system
- Multiple game states (menu, playing, paused, game over)
- Time and move limitations for added challenge

## How to Play

1. Click on a block that is adjacent to at least one other block of the same color
2. Groups must contain at least 2 blocks of the same color to be removed
3. Larger groups give more points - aim for big matches!
4. Make quick consecutive matches to build up combos for bonus points
5. After blocks are removed, the blocks above will fall down
6. New blocks will appear at the top of the grid
7. Reach the target score to advance to the next level
8. Manage your limited moves and time carefully
9. Try to get the highest score possible!

## Requirements

- Python 3.x
- Pygame

## Installation

1. Make sure you have Python installed
2. Install Pygame:
```
pip install pygame
```

## Running the Game

```
python blockblast.py
```

## Controls

- Left Mouse Button: Select and remove matching blocks
- ESC: Pause/unpause the game
- Close window to exit the game

## Sound Effects

The game supports sound effects. To enable them, place the following WAV files in a "sounds" folder:
- click.wav: Block selection sound
- match.wav: Sound when blocks are matched and removed
- levelup.wav: Sound when advancing to the next level
- gameover.wav: Sound when the game ends

The game will run fine without these files, but adding them enhances the experience.

## Future Enhancements

- Power-ups and special blocks
- Multiple game modes
- Persistent high scores
- Customizable themes and visual styles
- Online leaderboards

Enjoy playing Block Blast!