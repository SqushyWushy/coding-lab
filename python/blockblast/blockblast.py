import pygame
import random
import sys
import os
import math
from enum import Enum

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Game states
class GameState(Enum):
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2
    PAUSED = 3

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
BLOCK_SIZE = 40  # Slightly larger blocks for the smaller grid
GRID_WIDTH = 10  # Larger grid to make placement easier
GRID_HEIGHT = 10
GRID_OFFSET_X = (SCREEN_WIDTH - GRID_WIDTH * BLOCK_SIZE) // 2
GRID_OFFSET_Y = 100  # More space at the top
COLORS = [
    (255, 89, 94),   # Bright coral red
    (138, 201, 38),  # Lime green
    (25, 130, 196),  # Ocean blue
    (255, 202, 58),  # Sunny yellow
    (255, 125, 0),   # Orange
    (106, 76, 147),  # Purple
    (138, 201, 38),  # Lime green
    (45, 226, 230),  # Turquoise
    (232, 93, 117),  # Bright pink
    (255, 180, 235), # Light pink
    (255, 145, 77),  # Mango orange
    (0, 214, 132),   # Emerald
]
FPS = 60
INITIAL_SCORE_TARGET = 500  # Lower score target to make it easier

# Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Blast")
clock = pygame.time.Clock()

# Load sounds
try:
    sound_dir = os.path.join(os.path.dirname(__file__), 'sounds')
    if not os.path.exists(sound_dir):
        os.makedirs(sound_dir)
    
    # Placeholder for sound files
    click_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'click.wav')) if os.path.exists(os.path.join(sound_dir, 'click.wav')) else None
    place_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'place.wav')) if os.path.exists(os.path.join(sound_dir, 'place.wav')) else None
    clear_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'clear.wav')) if os.path.exists(os.path.join(sound_dir, 'clear.wav')) else None
    level_up_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'levelup.wav')) if os.path.exists(os.path.join(sound_dir, 'levelup.wav')) else None
    game_over_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'gameover.wav')) if os.path.exists(os.path.join(sound_dir, 'gameover.wav')) else None
except:
    # Fallback if sounds can't be loaded
    click_sound = None
    place_sound = None
    clear_sound = None
    level_up_sound = None
    game_over_sound = None

# Load fonts
pygame.font.init()
title_font = pygame.font.SysFont('Arial', 64, bold=True)
menu_font = pygame.font.SysFont('Arial', 36)
game_font = pygame.font.SysFont('Arial', 24)
score_font = pygame.font.SysFont('Arial', 36, bold=True)

# Particle effect class
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(5, 12)
        
        # More varied and dynamic movement
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(1, 5)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
        self.gravity = random.uniform(0.05, 0.15)
        self.life = random.randint(30, 60)
        self.max_life = self.life
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-5, 5)
        self.shape_type = random.choice(['circle', 'square', 'star', 'diamond'])
        
    def update(self):
        # Update position
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity
        
        # Add some sideways drift
        self.vx *= 0.98
        
        # Update rotation
        self.rotation += self.rotation_speed
        
        # Decrease life
        self.life -= 1
        
        # Calculate size based on life (shrink as it fades)
        life_ratio = self.life / self.max_life
        self.size = max(0, self.size * 0.97)
        
        return self.life > 0 and self.size > 0.5
    
    def draw(self, surface):
        if self.life <= 0 or self.size <= 0.5:
            return False
        
        # Calculate alpha (fade out)
        life_ratio = self.life / self.max_life
        alpha = int(255 * life_ratio)
        
        # Create a surface for this particle with transparency
        particle_surface = pygame.Surface((int(self.size * 2) + 2, int(self.size * 2) + 2), pygame.SRCALPHA)
        center = (int(self.size) + 1, int(self.size) + 1)
        
        # Determine color with alpha
        color_with_alpha = self.color + (alpha,)
        
        # Draw different shapes based on particle type
        if self.shape_type == 'circle':
            pygame.draw.circle(particle_surface, color_with_alpha, center, int(self.size))
        elif self.shape_type == 'square':
            rect = pygame.Rect(center[0] - self.size/2, center[1] - self.size/2, self.size, self.size)
            pygame.draw.rect(particle_surface, color_with_alpha, rect)
        elif self.shape_type == 'diamond':
            points = [
                (center[0], center[1] - self.size),
                (center[0] + self.size, center[1]),
                (center[0], center[1] + self.size),
                (center[0] - self.size, center[1])
            ]
            pygame.draw.polygon(particle_surface, color_with_alpha, points)
        elif self.shape_type == 'star':
            # Simple 4-point star
            inner_size = self.size * 0.4
            points = []
            for i in range(8):
                angle = math.pi * i / 4 + math.radians(self.rotation)
                radius = self.size if i % 2 == 0 else inner_size
                points.append((
                    center[0] + math.cos(angle) * radius,
                    center[1] + math.sin(angle) * radius
                ))
            pygame.draw.polygon(particle_surface, color_with_alpha, points)
        
        # Draw a small highlight in the particle for a glossy effect
        highlight_color = (255, 255, 255, alpha // 3)
        highlight_size = max(1, int(self.size / 3))
        highlight_pos = (center[0] - int(self.size/4), center[1] - int(self.size/4))
        pygame.draw.circle(particle_surface, highlight_color, highlight_pos, highlight_size)
        
        # Blit the particle to the screen
        surface.blit(particle_surface, (int(self.x - center[0]), int(self.y - center[1])))
        return True

# Single block in a shape
class Block:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.scale = 1.0
        self.rotation = 0
        self.pulse_dir = 1
        self.pulse_speed = random.uniform(0.005, 0.015)
        self.glow_amount = 0
        
    def update_animation(self):
        # Subtle pulsing animation
        self.scale += self.pulse_dir * self.pulse_speed
        if self.scale > 1.08:
            self.scale = 1.08
            self.pulse_dir = -1
        elif self.scale < 0.94:
            self.scale = 0.94
            self.pulse_dir = 1
            
        # Glow effect
        self.glow_amount = (self.scale - 0.94) / 0.14  # Normalize to 0-1
    
    def draw(self, surface, x_offset, y_offset, alpha=255, highlight=False):
        x = x_offset + self.col * BLOCK_SIZE
        y = y_offset + self.row * BLOCK_SIZE
        
        # Update animation
        self.update_animation()
        
        # Calculate scaled size
        scaled_size = int(BLOCK_SIZE * self.scale)
        x_adjust = (BLOCK_SIZE - scaled_size) // 2
        y_adjust = (BLOCK_SIZE - scaled_size) // 2
        
        # Create a bright 3D effect
        highlight_color = tuple(min(c + 90, 255) for c in self.color)
        shadow_color = tuple(max(c - 60, 0) for c in self.color)
        
        # Main block with transparency
        s = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE), pygame.SRCALPHA)
        
        # Draw glow effect for dragging
        if highlight or self.glow_amount > 0.5:
            glow_intensity = 150 if highlight else int(100 * self.glow_amount)
            glow_radius = 8 if highlight else int(4 * self.glow_amount)
            glow_color = (255, 255, 255, glow_intensity)
            pygame.draw.rect(s, glow_color, 
                         (x_adjust - glow_radius, y_adjust - glow_radius, 
                          scaled_size + glow_radius*2, scaled_size + glow_radius*2), 
                         border_radius=8)
        
        # Draw main block
        block_rect = pygame.Rect(x_adjust, y_adjust, scaled_size, scaled_size)
        pygame.draw.rect(s, self.color + (alpha,), block_rect, border_radius=5)
        
        # Create a glossy effect - diagonal gradient
        gloss = pygame.Surface((scaled_size, scaled_size), pygame.SRCALPHA)
        for i in range(scaled_size // 2):
            # Draw decreasing opacity diagonal lines 
            pygame.draw.line(gloss, (255, 255, 255, 70 - i*2), 
                            (i, i), (scaled_size//2, i), 2)
        
        s.blit(gloss, (x_adjust, y_adjust))
        
        # Highlight (top and left edges)
        pygame.draw.line(s, highlight_color + (alpha,), 
                       (x_adjust, y_adjust), 
                       (x_adjust + scaled_size, y_adjust), 3)
        pygame.draw.line(s, highlight_color + (alpha,), 
                       (x_adjust, y_adjust), 
                       (x_adjust, y_adjust + scaled_size), 3)
        
        # Shadow (bottom and right edges)
        pygame.draw.line(s, shadow_color + (alpha,), 
                       (x_adjust, y_adjust + scaled_size - 1), 
                       (x_adjust + scaled_size, y_adjust + scaled_size - 1), 2)
        pygame.draw.line(s, shadow_color + (alpha,), 
                       (x_adjust + scaled_size - 1, y_adjust), 
                       (x_adjust + scaled_size - 1, y_adjust + scaled_size), 2)
        
        # Draw highlight if drag selected
        if highlight:
            pygame.draw.rect(s, (255, 255, 255, min(alpha, 180)), 
                          block_rect, 3, border_radius=5)
        
        surface.blit(s, (x, y))
    
    def copy(self):
        return Block(self.row, self.col, self.color)

# Advanced shape generation system
class ShapeFactory:
    """Advanced factory for generating diverse, playable game shapes"""
    
    @staticmethod
    def ensure_connected(blocks):
        """Ensures all blocks in a shape are connected (no floating parts)"""
        if not blocks:
            return [(0, 0)]
            
        # Use BFS to find all connected blocks from the first block
        start = blocks[0]
        queue = [start]
        connected = {start}
        
        while queue:
            current = queue.pop(0)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if neighbor in blocks and neighbor not in connected:
                    connected.add(neighbor)
                    queue.append(neighbor)
        
        # Return only the connected blocks
        return list(connected) if connected else [(0, 0)]
    
    @staticmethod
    def normalize_shape(blocks):
        """Normalize shape coordinates to start at (0,0)"""
        if not blocks:
            return [(0, 0)]
            
        min_row = min(b[0] for b in blocks)
        min_col = min(b[1] for b in blocks)
        
        # Shift all blocks so minimal row and col are 0
        return [(r - min_row, c - min_col) for r, c in blocks]
    
    @staticmethod
    def validate_shape(blocks, max_size=4):  # Even smaller max size for easier play
        """Ensures shape is valid for gameplay"""
        if not blocks:
            return [(0, 0)]
            
        # Ensure connected
        blocks = ShapeFactory.ensure_connected(blocks)
        
        # Normalize coordinates
        blocks = ShapeFactory.normalize_shape(blocks)
        
        # Limit size (both dimensions)
        max_row = max(b[0] for b in blocks)
        max_col = max(b[1] for b in blocks)
        
        # Ensure shapes aren't too large for our grid
        if max_row >= max_size or max_col >= max_size or len(blocks) > 4:  # Limit to 4 blocks max
            # If too large, create a smaller shape
            return ShapeFactory.create_small_shape()
            
        # Ensure minimum size
        if len(blocks) < 1:
            return [(0, 0)]
            
        return blocks
    
    @staticmethod
    def create_small_shape():
        """Creates a small, simple shape when needed - perfect for 8x8 grid"""
        shapes = [
            [(0,0)],  # Single
            [(0,0), (0,1)],  # Horizontal duo
            [(0,0), (1,0)],  # Vertical duo
            [(0,0), (0,1), (1,0)],  # L corner
            [(0,0), (0,1), (1,1)],  # Square corner
            [(0,0), (0,1), (1,0), (1,1)],  # 2x2 square
            [(0,0), (0,1), (0,2)],  # Horizontal trio
            [(0,0), (1,0), (2,0)]   # Vertical trio
        ]
        return random.choice(shapes)
    
    # CLASSIC GAME SHAPES - SCALED DOWN FOR 8x8 GRID
    
    @staticmethod
    def create_tetromino():
        """Creates classic Tetris-style shapes - modified to fit 8x8 grid"""
        tetrominos = [
            [(0,0), (0,1), (0,2)],  # I (shortened)
            [(0,0), (1,0), (1,1)],  # L (smaller)
            [(0,1), (1,0), (1,1)],  # J (smaller)
            [(0,0), (0,1), (1,0), (1,1)],  # O (unchanged)
            [(0,0), (0,1), (0,2), (1,1)],  # T (unchanged)
            [(0,1), (0,2), (1,0), (1,1)],  # S (unchanged)
            [(0,0), (0,1), (1,1), (1,2)]   # Z (unchanged)
        ]
        return random.choice(tetrominos)
    
    @staticmethod
    def create_pentomino():
        """Creates smaller pentomino shapes (maximum 5 connected blocks) for 8x8 grid"""
        # For an 8x8 grid, we want smaller pentominos
        small_pentominos = [
            [(0,0), (0,1), (0,2), (1,0), (1,2)],  # U (smaller)
            [(0,0), (0,1), (1,1), (2,0), (2,1)],  # N shape
            [(0,0), (0,1), (1,1), (1,2), (2,1)],  # + (smaller)
            [(0,0), (0,1), (1,1), (1,2), (2,2)],  # Z (diagonal)
            [(0,0), (1,0), (1,1), (1,2), (2,1)],  # T+ shape
            [(0,1), (1,0), (1,1), (1,2), (2,1)],  # + (cross)
            [(0,0), (0,1), (0,2), (1,1), (2,1)]   # T shape
        ]
        return random.choice(small_pentominos)
    
    # PUZZLE GAME SPECIFIC SHAPES
    
    @staticmethod
    def create_corner_shape():
        """Creates various corner patterns"""
        base = [(0,0), (0,1), (1,0)]
        # Add extensions
        extensions = [
            [],  # No extension
            [(1,1)],  # Make a 2x2 square
            [(0,2)],  # Extend top row
            [(2,0)],  # Extend first column
            [(0,2), (1,1)],  # L shape with extension
            [(1,1), (2,0)]   # Different L shape
        ]
        return base + random.choice(extensions)
    
    @staticmethod
    def create_zigzag_shape():
        """Creates zigzag patterns"""
        zigzags = [
            [(0,0), (0,1), (1,1), (1,2)],  # Small Z
            [(0,1), (0,2), (1,0), (1,1)],  # Small S
            [(0,0), (0,1), (1,1), (1,2), (2,2), (2,3)],  # Longer Z
            [(0,2), (0,3), (1,1), (1,2), (2,0), (2,1)],  # Longer S
            [(0,0), (0,1), (1,1), (1,2), (2,2), (2,3), (3,3), (3,4)]  # Extra long Z
        ]
        return random.choice(zigzags)
    
    @staticmethod
    def create_snaking_shape():
        """Creates snake-like winding patterns"""
        # Start with a straight line
        length = random.randint(3, 6)
        snake = [(0,i) for i in range(length)]
        
        # Add 1-2 turns
        turns = random.randint(1, min(2, length-2))
        current_dir = 0  # 0: right, 1: down, 2: left, 3: up
        current_pos = snake[-1]
        
        for _ in range(turns):
            # Choose turn direction (left or right relative to current)
            turn = random.choice([-1, 1])
            new_dir = (current_dir + turn) % 4
            
            # Add 2-3 segments in the new direction
            segments = random.randint(2, 3)
            for s in range(1, segments+1):
                if new_dir == 0:  # right
                    next_pos = (current_pos[0], current_pos[1] + s)
                elif new_dir == 1:  # down
                    next_pos = (current_pos[0] + s, current_pos[1])
                elif new_dir == 2:  # left
                    next_pos = (current_pos[0], current_pos[1] - s)
                else:  # up
                    next_pos = (current_pos[0] - s, current_pos[1])
                snake.append(next_pos)
            
            current_dir = new_dir
            current_pos = snake[-1]
        
        return ShapeFactory.normalize_shape(snake)
    
    @staticmethod
    def create_letter_shape():
        """Creates smaller letter-shaped patterns for 8x8 grid"""
        small_letters = {
            'T': [(0,0), (0,1), (0,2), (1,1)],  # T (smaller)
            'L': [(0,0), (1,0), (2,0), (2,1)],  # L (unchanged)
            'I': [(0,0), (1,0), (2,0)],  # I (unchanged)
            'C': [(0,0), (0,1), (1,0), (2,0), (2,1)],  # C (smaller)
            'S': [(0,1), (0,2), (1,0), (1,1), (2,0)],  # S (compact)
            'Z': [(0,0), (0,1), (1,1), (1,2)],  # Z (smaller)
            'O': [(0,0), (0,1), (1,0), (1,1)]  # O (smaller square)
        }
        return small_letters[random.choice(list(small_letters.keys()))]
    
    @staticmethod
    def create_geometric_shape():
        """Creates smaller geometric patterns for 8x8 grid"""
        shapes = [
            # Plus sign (smaller)
            [(0,1), (1,0), (1,1), (1,2)],
            
            # Cross (smaller)
            [(0,1), (1,0), (1,1), (1,2), (2,1)],
            
            # Diamond
            [(0,1), (1,0), (1,2), (2,1)],
            
            # 2x2 Square
            [(0,0), (0,1), (1,0), (1,1)],
            
            # 2x3 Rectangle
            [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)],
            
            # Triangle
            [(0,0), (1,0), (1,1), (2,0), (2,1)]
        ]
        return random.choice(shapes)
    
    @staticmethod
    def create_asymmetric_shape():
        """Creates intentionally asymmetric shapes for gameplay challenge"""
        # Start with a basic shape
        base_options = [
            [(0,0), (0,1), (1,0)],  # Corner
            [(0,0), (0,1), (0,2)],  # Line
            [(0,0), (0,1), (1,1)]   # L piece
        ]
        
        shape = random.choice(base_options)
        
        # Add 2-4 random extensions that create asymmetry
        extensions = random.randint(2, 4)
        possible_positions = []
        
        # Find all positions adjacent to existing blocks
        for r, c in shape:
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                new_pos = (r+dr, c+dc)
                if new_pos not in shape:
                    possible_positions.append(new_pos)
        
        # Add random extensions
        for _ in range(extensions):
            if not possible_positions:
                break
                
            # Pick a random position and add it
            new_pos = random.choice(possible_positions)
            shape.append(new_pos)
            possible_positions.remove(new_pos)
            
            # Update possible positions
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                adj_pos = (new_pos[0]+dr, new_pos[1]+dc)
                if adj_pos not in shape and adj_pos not in possible_positions:
                    possible_positions.append(adj_pos)
        
        return ShapeFactory.normalize_shape(shape)
    
    @staticmethod
    def create_spiral_shape():
        """Creates spiral or circular patterns"""
        # Small spiral
        if random.random() < 0.7:
            return [(0,0), (0,1), (0,2), (1,2), (2,2), (2,1), (2,0), (1,0)]
        else:
            # Larger spiral with a hole in the middle
            return [(0,0), (0,1), (0,2), (0,3), (1,3), (2,3), (3,3), (3,2), (3,1), (3,0), (2,0), (1,0)]
    
    @staticmethod  
    def create_snake_shape():
        """Creates a compact snake-like shape"""
        directions = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
        snake = [(0,0)]
        length = random.randint(4, 7)
        
        # Build a tightly packed snake
        current = (0,0)
        for _ in range(length-1):
            random.shuffle(directions)
            for d in directions:
                next_pos = (current[0] + d[0], current[1] + d[1])
                if next_pos not in snake:
                    snake.append(next_pos)
                    current = next_pos
                    break
        
        return ShapeFactory.normalize_shape(snake)
    
    @staticmethod
    def create_random_compact_shape(complexity=None):
        """Creates a random compact shape with controlled complexity"""
        if complexity is None:
            complexity = random.randint(3, 8)
            
        shape = [(0, 0)]
        available_edges = [(0,0)]
        
        # Build shape by adding blocks adjacent to existing ones
        for _ in range(complexity - 1):
            if not available_edges:
                break
                
            # Choose a random position that already has a block
            pos = random.choice(available_edges)
            
            # Find all valid directions to expand
            valid_dirs = []
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                new_pos = (pos[0] + dx, pos[1] + dy)
                if new_pos not in shape:
                    valid_dirs.append((dx, dy))
            
            # If no valid directions, remove this position from available edges
            if not valid_dirs:
                available_edges.remove(pos)
                continue
                
            # Add a block in a random valid direction
            dx, dy = random.choice(valid_dirs)
            new_pos = (pos[0] + dx, pos[1] + dy)
            shape.append(new_pos)
            
            # Add the new position to available edges
            available_edges.append(new_pos)
            
            # Check if original position still has available directions
            still_has_dirs = False
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                check_pos = (pos[0] + dx, pos[1] + dy)
                if check_pos not in shape:
                    still_has_dirs = True
                    break
            
            if not still_has_dirs:
                available_edges.remove(pos)
        
        return ShapeFactory.normalize_shape(shape)
    
    @staticmethod
    def create_shape_with_hole():
        """Creates smaller shapes with interior holes for 8x8 grid"""
        frames = [
            # Small square frame (2x2 with hole)
            [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)],
            
            # Smaller C shape
            [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)],
            
            # O shape
            [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)],
            
            # Small square with corners (windmill)
            [(0,0), (0,2), (1,1), (2,0), (2,2)]
        ]
        
        return random.choice(frames)

class Shape:
    """Represents a playable game shape with advanced generation"""
    
    def __init__(self, shape_type=None):
        """Creates a shape using the advanced ShapeFactory"""
        self.blocks = []
        self.original_pos = (0, 0)
        self.pos_x = 0
        self.pos_y = 0
        self.dragging = False
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        
        # Map of generation strategies to factory methods
        strategies = {
            'tetromino': ShapeFactory.create_tetromino,
            'pentomino': ShapeFactory.create_pentomino,
            'corner': ShapeFactory.create_corner_shape,
            'zigzag': ShapeFactory.create_zigzag_shape,
            'snake': ShapeFactory.create_snake_shape,
            'letter': ShapeFactory.create_letter_shape,
            'geometric': ShapeFactory.create_geometric_shape,
            'asymmetric': ShapeFactory.create_asymmetric_shape,
            'spiral': ShapeFactory.create_spiral_shape,
            'random': ShapeFactory.create_random_compact_shape,
            'hole': ShapeFactory.create_shape_with_hole,
            'snaking': ShapeFactory.create_snaking_shape,
        }
        
        # Select generation strategy based on level of complexity
        if shape_type is None:
            # Modified weights to favor simpler shapes
            difficulty_weight = {
                'tetromino': 25,      # Classic tetris pieces (most common)
                'corner': 25,         # Corner pieces (very useful)
                'zigzag': 10,         # Zigzag shapes
                'snake': 10,          # Snake shapes
                'letter': 5,          # Letter shapes
                'geometric': 5,       # Geometric patterns
                'asymmetric': 5,      # Asymmetric shapes
                'pentomino': 5,       # Five-block shapes
                'spiral': 3,          # Spiral shapes
                'random': 3,          # Random compact shapes
                'snaking': 3,         # Snaking shapes  
                'hole': 1,            # Shapes with holes (most challenging)
            }
            
            shape_strategy = random.choices(
                list(difficulty_weight.keys()),
                weights=list(difficulty_weight.values()),
                k=1
            )[0]
            
            # Generate shape using selected strategy
            template = strategies[shape_strategy]()
        else:
            # For specific type requests, still ensure variety
            shape_keys = list(strategies.keys())
            shape_strategy = shape_keys[shape_type % len(shape_keys)]
            template = strategies[shape_strategy]()
        
        # Validate the shape for gameplay
        template = ShapeFactory.validate_shape(template)
        
        # Apply rotation transformation sometimes for extra variety
        if random.random() < 0.7:  # Increased chance of rotation for more variety in 8x8 grid
            rotations = random.randint(1, 3)
            for _ in range(rotations):
                # Rotate 90 degrees clockwise
                template = [(c, -r) for r, c in template]
                template = ShapeFactory.normalize_shape(template)
                
        # Final size check - ensure shape isn't too large for 8x8 grid
        max_row = max(r for r, c in template)
        max_col = max(c for r, c in template)
        if max_row > 4 or max_col > 4 or len(template) > 5:
            # If still too large after all processing, fall back to a small shape
            template = ShapeFactory.create_small_shape()
        
        # Decide on color approach
        color_strategy = random.choice([
            'solid',       # Single color (60% chance)
            'solid',
            'solid',
            'gradient',    # Gradient effect (20% chance)
            'gradient',
            'rainbow'      # Rainbow pattern (20% chance)
        ])
        
        # Apply color to blocks
        base_color = random.choice(COLORS)
        
        for row, col in template:
            if color_strategy == 'solid':
                # Simple solid color
                self.blocks.append(Block(row, col, base_color))
            
            elif color_strategy == 'gradient':
                # Create a subtle gradient effect
                intensity = (row + col) * 15
                r, g, b = base_color
                gradient_color = (
                    max(0, min(255, r + intensity)),
                    max(0, min(255, g + intensity//2)),
                    max(0, min(255, b + intensity//3))
                )
                self.blocks.append(Block(row, col, gradient_color))
            
            elif color_strategy == 'rainbow':
                # Create a rainbow pattern based on position
                hue = (row * 30 + col * 20) % 360
                # Convert HSV to RGB (simplified)
                segment = hue // 60
                val = 255
                c = val * 0.9
                x = c * (1 - abs((hue / 60) % 2 - 1))
                
                if segment == 0:
                    r, g, b = c, x, 0
                elif segment == 1:
                    r, g, b = x, c, 0
                elif segment == 2:
                    r, g, b = 0, c, x
                elif segment == 3:
                    r, g, b = 0, x, c
                elif segment == 4:
                    r, g, b = x, 0, c
                else:
                    r, g, b = c, 0, x
                    
                # Brighten and ensure valid RGB
                rainbow_color = (
                    max(0, min(255, int(r + 100))),
                    max(0, min(255, int(g + 100))),
                    max(0, min(255, int(b + 100)))
                )
                self.blocks.append(Block(row, col, rainbow_color))
        
    def normalize(self):
        """Normalize the shape's coordinates"""
        if not self.blocks:
            return
            
        # Find minimum row and column
        min_row = min(block.row for block in self.blocks)
        min_col = min(block.col for block in self.blocks)
        
        # Normalize positions
        for block in self.blocks:
            block.row -= min_row
            block.col -= min_col
    
    def draw(self, surface, x, y, alpha=255, highlight=False):
        """Draw the shape on the given surface"""
        for block in self.blocks:
            block.draw(surface, x, y, alpha, highlight)
    
    def get_width(self):
        """Get the width of the shape in pixels"""
        if not self.blocks:
            return BLOCK_SIZE
        max_col = max(block.col for block in self.blocks)
        return (max_col + 1) * BLOCK_SIZE
    
    def get_height(self):
        """Get the height of the shape in pixels"""
        if not self.blocks:
            return BLOCK_SIZE
        max_row = max(block.row for block in self.blocks)
        return (max_row + 1) * BLOCK_SIZE
    
    def contains_point(self, x, y):
        """Check if the shape contains the given point"""
        shape_x, shape_y = self.pos_x, self.pos_y
        shape_width = self.get_width()
        shape_height = self.get_height()
        
        return (shape_x <= x <= shape_x + shape_width and 
                shape_y <= y <= shape_y + shape_height)
    
    def start_drag(self, x, y):
        """Start dragging the shape"""
        self.dragging = True
        self.drag_offset_x = self.pos_x - x
        self.drag_offset_y = self.pos_y - y
        self.original_pos = (self.pos_x, self.pos_y)
    
    def drag(self, x, y):
        """Update the shape's position while dragging"""
        if self.dragging:
            self.pos_x = x + self.drag_offset_x
            self.pos_y = y + self.drag_offset_y
    
    def end_drag(self):
        """End dragging the shape"""
        self.dragging = False
    
    def copy(self):
        """Create a copy of this shape"""
        new_shape = Shape()
        new_shape.blocks = [block.copy() for block in self.blocks]
        new_shape.pos_x = self.pos_x
        new_shape.pos_y = self.pos_y
        return new_shape

class Game:
    def __init__(self):
        self.reset_game()
    
    def reset_game(self):
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.score = 0
        self.level = 1
        self.state = GameState.MENU
        self.particles = []
        self.time_left = 300  # 5 minutes timer
        self.last_time_check = pygame.time.get_ticks()
        self.score_target = INITIAL_SCORE_TARGET
        
        # Available shapes to place
        self.available_shapes = [Shape() for _ in range(3)]
        self.position_shapes()
        
        # Track current dragging shape
        self.dragging_shape = None
        self.ghost_shape = None  # Preview of where shape will be placed
        
        # UI elements
        self.btn_play = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2, 200, 50)
        self.btn_quit = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 70, 200, 50)
        self.btn_resume = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 35, 200, 50)
        self.btn_menu = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 35, 200, 50)
    
    def position_shapes(self):
        # Position available shapes below the grid
        available_area_width = SCREEN_WIDTH - 80  # Leave margins on both sides
        shape_spacing = available_area_width // (len(self.available_shapes))
        
        for i, shape in enumerate(self.available_shapes):
            shape.normalize()  # Make sure shape is aligned properly
            shape.pos_x = 40 + i * shape_spacing + (shape_spacing // 2) - shape.get_width() // 2
            shape.pos_y = GRID_OFFSET_Y + GRID_HEIGHT * BLOCK_SIZE + 30
    
    def update(self):
        # Update timer
        current_time = pygame.time.get_ticks()
        if self.state == GameState.PLAYING and current_time - self.last_time_check >= 1000:
            self.time_left -= 1
            self.last_time_check = current_time
            
            if self.time_left <= 0:
                self.game_over()
        
        # Update particles
        self.particles = [p for p in self.particles if p.update() and p.draw(screen)]
        
        # Update ghost shape position if dragging
        if self.dragging_shape:
            grid_x, grid_y = self.get_grid_position(self.dragging_shape)
            if self.can_place_shape_at(self.dragging_shape, grid_x, grid_y):
                if not self.ghost_shape:
                    self.ghost_shape = self.dragging_shape.copy()
                
                self.ghost_shape.pos_x = GRID_OFFSET_X + grid_x * BLOCK_SIZE
                self.ghost_shape.pos_y = GRID_OFFSET_Y + grid_y * BLOCK_SIZE
            else:
                self.ghost_shape = None
    
    def draw(self):
        # Draw background
        screen.fill((25, 25, 50))
        
        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.PLAYING:
            self.draw_game()
        elif self.state == GameState.GAME_OVER:
            self.draw_game()
            self.draw_game_over()
        elif self.state == GameState.PAUSED:
            self.draw_game()
            self.draw_pause_menu()
        
        # Draw particles on top of everything
        for particle in self.particles:
            particle.draw(screen)
        
        pygame.display.flip()
    
    def draw_menu(self):
        # Draw colorful gradient background
        for y in range(0, SCREEN_HEIGHT, 4):
            # Create a gradient from deep blue to purple
            color_val = 40 + int(40 * (y / SCREEN_HEIGHT))
            color = (color_val//2, color_val//4, color_val)
            pygame.draw.line(screen, color, (0, y), (SCREEN_WIDTH, y), 4)
            
        # Add starfield effect
        for _ in range(50):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            size = random.randint(1, 3)
            brightness = random.randint(180, 255)
            pygame.draw.circle(screen, (brightness, brightness, brightness), (x, y), size)
            
        # Draw animated title with glow
        title_glow_size = 20 + int(10 * math.sin(pygame.time.get_ticks() * 0.003))
        title_glow = pygame.Surface((400 + title_glow_size, 100 + title_glow_size), pygame.SRCALPHA)
        pygame.draw.rect(title_glow, (100, 100, 255, 30), 
                       (0, 0, 400 + title_glow_size, 100 + title_glow_size), 
                       border_radius=30)
        screen.blit(title_glow, ((SCREEN_WIDTH - (400 + title_glow_size))//2, 120 - title_glow_size//2))
            
        # Animated title text with color cycling
        t = pygame.time.get_ticks() * 0.001
        title_colors = [
            (255, 
             max(0, min(255, 100 + int(155 * math.sin(t + 0)))), 
             max(0, min(255, 100 + int(155 * math.sin(t + 2))))),
            (max(0, min(255, 100 + int(155 * math.sin(t + 4)))), 
             255, 
             max(0, min(255, 100 + int(155 * math.sin(t + 6))))),
            (max(0, min(255, 100 + int(155 * math.sin(t + 8)))), 
             max(0, min(255, 100 + int(155 * math.sin(t + 10)))), 
             255)
        ]
        
        # Draw "BLOCK" in one color and "BLAST" in another
        block_text = title_font.render("BLOCK", True, title_colors[0])
        blast_text = title_font.render("BLAST", True, title_colors[1])
        
        block_rect = block_text.get_rect(center=(SCREEN_WIDTH//2 - 80, 150))
        blast_rect = blast_text.get_rect(center=(SCREEN_WIDTH//2 + 90, 150))
        
        # Add shadow effect
        shadow_offset = 3
        shadow_color = (0, 0, 0)
        block_shadow = title_font.render("BLOCK", True, shadow_color)
        blast_shadow = title_font.render("BLAST", True, shadow_color)
        screen.blit(block_shadow, (block_rect.x + shadow_offset, block_rect.y + shadow_offset))
        screen.blit(blast_shadow, (blast_rect.x + shadow_offset, blast_rect.y + shadow_offset))
        
        # Draw main text
        screen.blit(block_text, block_rect)
        screen.blit(blast_text, blast_rect)
        
        # Draw animated buttons
        btn_glow = math.sin(pygame.time.get_ticks() * 0.005) * 0.5 + 0.5
        
        # Play button with glow
        play_glow = pygame.Surface((220, 70), pygame.SRCALPHA)
        play_glow_color = (100, 150, 255, int(100 * btn_glow))
        pygame.draw.rect(play_glow, play_glow_color, (0, 0, 220, 70), border_radius=15)
        screen.blit(play_glow, (self.btn_play.x - 10, self.btn_play.y - 10))
        
        # Quit button with glow
        quit_glow = pygame.Surface((220, 70), pygame.SRCALPHA)
        quit_glow_color = (255, 100, 100, int(100 * btn_glow))
        pygame.draw.rect(quit_glow, quit_glow_color, (0, 0, 220, 70), border_radius=15)
        screen.blit(quit_glow, (self.btn_quit.x - 10, self.btn_quit.y - 10))
        
        # Draw button backgrounds with gradient
        play_grad_top = (80, 100, 230)
        play_grad_bottom = (60, 80, 180)
        for y in range(self.btn_play.height):
            ratio = y / self.btn_play.height
            r = int(play_grad_top[0] * (1-ratio) + play_grad_bottom[0] * ratio)
            g = int(play_grad_top[1] * (1-ratio) + play_grad_bottom[1] * ratio)
            b = int(play_grad_top[2] * (1-ratio) + play_grad_bottom[2] * ratio)
            pygame.draw.line(screen, (r, g, b), 
                           (self.btn_play.left, self.btn_play.top + y),
                           (self.btn_play.right, self.btn_play.top + y), 1)
            
        quit_grad_top = (230, 80, 80)
        quit_grad_bottom = (180, 60, 60)
        for y in range(self.btn_quit.height):
            ratio = y / self.btn_quit.height
            r = int(quit_grad_top[0] * (1-ratio) + quit_grad_bottom[0] * ratio)
            g = int(quit_grad_top[1] * (1-ratio) + quit_grad_bottom[1] * ratio)
            b = int(quit_grad_top[2] * (1-ratio) + quit_grad_bottom[2] * ratio)
            pygame.draw.line(screen, (r, g, b), 
                           (self.btn_quit.left, self.btn_quit.top + y),
                           (self.btn_quit.right, self.btn_quit.top + y), 1)
            
        # Add button outlines
        pygame.draw.rect(screen, (170, 180, 255), self.btn_play, 3, border_radius=10)
        pygame.draw.rect(screen, (255, 170, 170), self.btn_quit, 3, border_radius=10)
        
        play_text = menu_font.render("PLAY", True, (255, 255, 255))
        quit_text = menu_font.render("QUIT", True, (255, 255, 255))
        
        play_rect = play_text.get_rect(center=self.btn_play.center)
        quit_rect = quit_text.get_rect(center=self.btn_quit.center)
        
        # Add text glow/shadow
        play_shadow = menu_font.render("PLAY", True, (40, 40, 120))
        quit_shadow = menu_font.render("QUIT", True, (120, 40, 40))
        screen.blit(play_shadow, (play_rect.x + 2, play_rect.y + 2))
        screen.blit(quit_shadow, (quit_rect.x + 2, quit_rect.y + 2))
        
        screen.blit(play_text, play_rect)
        screen.blit(quit_text, quit_rect)
        
        # Draw instructions with animated highlight
        instruction_highlight = int(25 * math.sin(pygame.time.get_ticks() * 0.003) + 25)
        instructions = [
            "Drag and drop shapes onto the grid",
            "Clear rows or columns to score points",
            "You must use ALL THREE shapes before getting new ones",
            "Use shapes strategically to keep the grid from filling up!"
        ]
        
        # Instruction box
        instr_box = pygame.Rect(SCREEN_WIDTH//2 - 300, 290, 600, 160)
        instr_surface = pygame.Surface((instr_box.width, instr_box.height), pygame.SRCALPHA)
        instr_surface.fill((30, 40, 80, 180))
        pygame.draw.rect(instr_surface, (100, 120, 200, 200), (0, 0, instr_box.width, instr_box.height), 2, border_radius=15)
        screen.blit(instr_surface, instr_box)
        
        # Instruction title
        instr_title = menu_font.render("HOW TO PLAY", True, (180, 200, 255))
        instr_title_rect = instr_title.get_rect(center=(SCREEN_WIDTH//2, 305))
        screen.blit(instr_title, instr_title_rect)
        
        # Instructions with color highlights
        for i, instruction in enumerate(instructions):
            text_color = (200, 200, 200)
            if i == int(pygame.time.get_ticks() / 3000) % 4:  # Cycle through highlights
                text_color = (255, 255, min(255, max(0, 150 + instruction_highlight)))
            text = game_font.render(instruction, True, text_color)
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, 335 + i*30))
            
        # Display sample shapes at the bottom
        sample_text = game_font.render("Example Shapes:", True, (180, 180, 255))
        screen.blit(sample_text, (SCREEN_WIDTH//2 - sample_text.get_width()//2, 470))
        
        # Show sample shapes
        samples = [Shape(i) for i in range(5)]
        spacing = SCREEN_WIDTH // (len(samples) + 1)
        
        for i, shape in enumerate(samples):
            shape.normalize()
            x = (i + 1) * spacing - shape.get_width() // 2
            y = 500 + math.sin(pygame.time.get_ticks() * 0.003 + i) * 5  # Floating animation
            shape.draw(screen, x, y)
    
    def draw_game(self):
        # Draw colorful gradient background
        for y in range(0, SCREEN_HEIGHT, 4):
            # Create a gradient from dark purple to deep blue
            color_val = 40 + int(30 * (y / SCREEN_HEIGHT))
            color = (color_val//2, color_val//3, color_val)
            pygame.draw.line(screen, color, (0, y), (SCREEN_WIDTH, y), 4)
            
        # Add a small visual indicator of how many shapes need to be used
        if len(self.available_shapes) > 0:
            # Progress bar showing shapes remaining
            progress_rect = pygame.Rect(
                SCREEN_WIDTH - 120, 
                GRID_OFFSET_Y + GRID_HEIGHT * BLOCK_SIZE + 80,
                90,
                8
            )
            # Background bar
            pygame.draw.rect(screen, (60, 60, 90), progress_rect, border_radius=4)
            
            # Progress indicator - shows how many shapes have been used
            filled_width = int(90 * ((3 - len(self.available_shapes)) / 3))
            if filled_width > 0:
                filled_rect = pygame.Rect(
                    progress_rect.x, 
                    progress_rect.y,
                    filled_width,
                    8
                )
                pygame.draw.rect(screen, (100, 200, 255), filled_rect, border_radius=4)
                
            # Label
            remaining_text = game_font.render(f"Shapes: {len(self.available_shapes)}/3", True, (180, 200, 255))
            screen.blit(remaining_text, (SCREEN_WIDTH - 120, GRID_OFFSET_Y + GRID_HEIGHT * BLOCK_SIZE + 60))
        
        # Add some star-like particles in the background
        for _ in range(20):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            size = random.randint(1, 3)
            brightness = random.randint(100, 220)
            pygame.draw.circle(screen, (brightness, brightness, brightness), (x, y), size)
        
        # Draw shapes area background with glow effect
        shapes_area_rect = pygame.Rect(
            20, 
            GRID_OFFSET_Y + GRID_HEIGHT * BLOCK_SIZE + 20,
            SCREEN_WIDTH - 40,
            80
        )
        
        # Draw glow behind shapes area
        glow_rect = shapes_area_rect.inflate(20, 20)
        glow_surface = pygame.Surface((glow_rect.width, glow_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(glow_surface, (120, 140, 255, 40), 
                       (0, 0, glow_rect.width, glow_rect.height), 
                       border_radius=15)
        screen.blit(glow_surface, glow_rect.topleft)
        
        # Draw main shapes area
        pygame.draw.rect(screen, (50, 50, 85), shapes_area_rect, border_radius=10)
        pygame.draw.rect(screen, (130, 140, 220), shapes_area_rect, 2, border_radius=10)
        
        # Add a label for the shapes area
        shapes_label = game_font.render("Available Shapes", True, (200, 210, 255))
        screen.blit(shapes_label, (SCREEN_WIDTH//2 - shapes_label.get_width()//2, 
                                 GRID_OFFSET_Y + GRID_HEIGHT * BLOCK_SIZE + 25))
        
        # Draw grid background with glossy effect
        grid_rect = pygame.Rect(
            GRID_OFFSET_X - 15, 
            GRID_OFFSET_Y - 15,
            GRID_WIDTH * BLOCK_SIZE + 30,
            GRID_HEIGHT * BLOCK_SIZE + 30
        )
        
        # Draw glow behind grid
        grid_glow_rect = grid_rect.inflate(30, 30)
        grid_glow_surface = pygame.Surface((grid_glow_rect.width, grid_glow_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(grid_glow_surface, (100, 150, 255, 30), 
                       (0, 0, grid_glow_rect.width, grid_glow_rect.height), 
                       border_radius=20)
        screen.blit(grid_glow_surface, grid_glow_rect.topleft)
        
        # Main grid background
        pygame.draw.rect(screen, (45, 45, 75), grid_rect, border_radius=10)
        
        # Grid border with gradient effect
        border_colors = [
            (130, 140, 230),  # Top
            (120, 130, 220),  # Right
            (110, 120, 210),  # Bottom
            (100, 110, 200)   # Left
        ]
        
        # Draw each side of border with slightly different color
        # Top
        pygame.draw.line(screen, border_colors[0], 
                       (grid_rect.left, grid_rect.top), 
                       (grid_rect.right, grid_rect.top), 3)
        # Right
        pygame.draw.line(screen, border_colors[1], 
                       (grid_rect.right, grid_rect.top), 
                       (grid_rect.right, grid_rect.bottom), 3)
        # Bottom
        pygame.draw.line(screen, border_colors[2], 
                       (grid_rect.left, grid_rect.bottom), 
                       (grid_rect.right, grid_rect.bottom), 3)
        # Left
        pygame.draw.line(screen, border_colors[3], 
                       (grid_rect.left, grid_rect.top), 
                       (grid_rect.left, grid_rect.bottom), 3)
        
        # Draw grid lines
        for x in range(GRID_WIDTH + 1):
            pygame.draw.line(
                screen, 
                (70, 70, 90), 
                (GRID_OFFSET_X + x * BLOCK_SIZE, GRID_OFFSET_Y),
                (GRID_OFFSET_X + x * BLOCK_SIZE, GRID_OFFSET_Y + GRID_HEIGHT * BLOCK_SIZE),
                1
            )
        
        for y in range(GRID_HEIGHT + 1):
            pygame.draw.line(
                screen, 
                (70, 70, 90), 
                (GRID_OFFSET_X, GRID_OFFSET_Y + y * BLOCK_SIZE),
                (GRID_OFFSET_X + GRID_WIDTH * BLOCK_SIZE, GRID_OFFSET_Y + y * BLOCK_SIZE),
                1
            )
        
        # Draw placed blocks
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if self.grid[row][col]:
                    self.grid[row][col].draw(
                        screen, 
                        GRID_OFFSET_X, 
                        GRID_OFFSET_Y
                    )
        
        # Draw ghost shape (placement preview)
        if self.ghost_shape:
            for block in self.ghost_shape.blocks:
                block.draw(
                    screen, 
                    self.ghost_shape.pos_x, 
                    self.ghost_shape.pos_y, 
                    alpha=128
                )
        
        # Draw available shapes
        for shape in self.available_shapes:
            if shape != self.dragging_shape:
                shape.draw(screen, shape.pos_x, shape.pos_y)
        
        # Draw shape being dragged (on top)
        if self.dragging_shape:
            self.dragging_shape.draw(screen, self.dragging_shape.pos_x, self.dragging_shape.pos_y, highlight=True)
        
        # Draw UI frame at the top
        ui_rect = pygame.Rect(10, 10, SCREEN_WIDTH - 20, 40)
        pygame.draw.rect(screen, (40, 40, 70), ui_rect, border_radius=10)
        pygame.draw.rect(screen, (100, 100, 150), ui_rect, 2, border_radius=10)
        
        # Draw score with glowing effect
        score_glow = pygame.Surface((120, 40), pygame.SRCALPHA)
        pygame.draw.rect(score_glow, (255, 255, 100, 40), (0, 0, 120, 40), border_radius=10)
        screen.blit(score_glow, (20, 10))
        
        score_text = game_font.render(f"Score: {self.score}", True, (255, 255, 150))
        screen.blit(score_text, (30, 20))
        
        # Draw level with pulse effect
        pulse = 0.2 * math.sin(pygame.time.get_ticks() * 0.005) + 1.0
        level_color = (min(255, max(0, int(200 + 55*pulse))), 
                      min(255, max(0, int(200 + 55*pulse))), 
                      255)
        level_text = game_font.render(f"Level: {self.level}", True, level_color)
        level_rect = level_text.get_rect()
        screen.blit(level_text, (SCREEN_WIDTH//2 - level_rect.width//2, 20))
        
        # Draw target score with gradient
        target_color = (150, 180, 255)
        target_text = game_font.render(f"Target: {self.score_target}", True, target_color)
        target_rect = target_text.get_rect()
        screen.blit(target_text, (200, 20))
        
        # Draw time
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        time_color = (255, 255, 255) if self.time_left > 30 else (255, 100, 100)
        time_text = game_font.render(f"Time: {minutes}:{seconds:02d}", True, time_color)
        screen.blit(time_text, (SCREEN_WIDTH - time_text.get_width() - 30, 20))
        
        # Draw pause button
        pause_btn = pygame.Rect(SCREEN_WIDTH - 50, 15, 30, 30)
        pygame.draw.rect(screen, (150, 150, 200), pause_btn, 2, border_radius=5)
        pygame.draw.rect(screen, (70, 70, 100), pause_btn, 0, border_radius=5)
        pygame.draw.line(screen, (200, 200, 255), (pause_btn.x + 10, pause_btn.y + 8), 
                        (pause_btn.x + 10, pause_btn.y + 22), 4)
        pygame.draw.line(screen, (200, 200, 255), (pause_btn.x + 20, pause_btn.y + 8), 
                        (pause_btn.x + 20, pause_btn.y + 22), 4)
    
    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))
        
        # Game over text
        gameover_text = title_font.render("GAME OVER", True, (255, 100, 100))
        gameover_rect = gameover_text.get_rect(center=(SCREEN_WIDTH//2, 180))
        screen.blit(gameover_text, gameover_rect)
        
        # Final score
        score_text = menu_font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, 250))
        screen.blit(score_text, score_rect)
        
        # Level reached
        level_text = menu_font.render(f"Level Reached: {self.level}", True, (255, 255, 255))
        level_rect = level_text.get_rect(center=(SCREEN_WIDTH//2, 300))
        screen.blit(level_text, level_rect)
        
        # Draw buttons
        pygame.draw.rect(screen, (80, 80, 200), self.btn_play, border_radius=10)
        pygame.draw.rect(screen, (200, 80, 80), self.btn_quit, border_radius=10)
        
        retry_text = menu_font.render("RETRY", True, (255, 255, 255))
        quit_text = menu_font.render("QUIT", True, (255, 255, 255))
        
        retry_rect = retry_text.get_rect(center=self.btn_play.center)
        quit_rect = quit_text.get_rect(center=self.btn_quit.center)
        
        screen.blit(retry_text, retry_rect)
        screen.blit(quit_text, quit_rect)
    
    def draw_pause_menu(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = title_font.render("PAUSED", True, (200, 200, 255))
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH//2, 180))
        screen.blit(pause_text, pause_rect)
        
        # Draw buttons
        pygame.draw.rect(screen, (80, 80, 200), self.btn_resume, border_radius=10)
        pygame.draw.rect(screen, (80, 150, 80), self.btn_menu, border_radius=10)
        
        resume_text = menu_font.render("RESUME", True, (255, 255, 255))
        menu_text = menu_font.render("MENU", True, (255, 255, 255))
        
        resume_rect = resume_text.get_rect(center=self.btn_resume.center)
        menu_rect = menu_text.get_rect(center=self.btn_menu.center)
        
        screen.blit(resume_text, resume_rect)
        screen.blit(menu_text, menu_rect)
    
    def get_shape_at_pos(self, pos):
        # Check if position is over one of the available shapes
        for shape in self.available_shapes:
            if shape.contains_point(*pos):
                return shape
        return None
    
    def get_grid_position(self, shape):
        # Convert screen position to grid position
        grid_x = round((shape.pos_x - GRID_OFFSET_X) / BLOCK_SIZE)
        grid_y = round((shape.pos_y - GRID_OFFSET_Y) / BLOCK_SIZE)
        return grid_x, grid_y
    
    def can_place_shape_at(self, shape, grid_x, grid_y):
        for block in shape.blocks:
            # Calculate grid position
            block_x = grid_x + block.col
            block_y = grid_y + block.row
            
            # Check boundaries
            if not (0 <= block_x < GRID_WIDTH and 0 <= block_y < GRID_HEIGHT):
                return False
            
            # Check if position is already occupied
            if self.grid[block_y][block_x]:
                return False
        
        return True
    
    def place_shape(self, shape):
        grid_x, grid_y = self.get_grid_position(shape)
        
        if self.can_place_shape_at(shape, grid_x, grid_y):
            # Place blocks on grid
            for block in shape.blocks:
                block_x = grid_x + block.col
                block_y = grid_y + block.row
                self.grid[block_y][block_x] = Block(block_y, block_x, block.color)
            
            # Play sound
            if place_sound:
                place_sound.play()
            
            # Generate particles for visual feedback
            for block in shape.blocks:
                x = GRID_OFFSET_X + (grid_x + block.col + 0.5) * BLOCK_SIZE
                y = GRID_OFFSET_Y + (grid_y + block.row + 0.5) * BLOCK_SIZE
                
                # Create a burst of colorful particles
                for _ in range(15):
                    # Add some color variation from the base block color
                    r, g, b = block.color
                    color_variation = random.randint(-30, 30)
                    new_color = (
                        max(0, min(255, r + color_variation)),
                        max(0, min(255, g + color_variation)),
                        max(0, min(255, b + color_variation))
                    )
                    self.particles.append(Particle(x, y, new_color))
                    
                # Add a few white sparkle particles
                for _ in range(3):
                    brightness = random.randint(200, 255)
                    sparkle_color = (brightness, brightness, brightness)
                    self.particles.append(Particle(x, y, sparkle_color))
            
            # Remove shape from available shapes
            if shape in self.available_shapes:
                self.available_shapes.remove(shape)
                
                # Check if all three shapes have been used
                if len(self.available_shapes) == 0:
                    # Generate 3 new shapes only when all previous shapes are used
                    self.available_shapes = [
                        Shape(shape_type=self.level),
                        Shape(shape_type=self.level),
                        Shape(shape_type=self.level)
                    ]
                    self.position_shapes()
                    
                    # Play a special sound for new shapes
                    if level_up_sound:  # Reuse level up sound for now
                        level_up_sound.play()
                        
                    # Visual feedback - particle burst across the shapes area
                    shapes_area_y = GRID_OFFSET_Y + GRID_HEIGHT * BLOCK_SIZE + 50
                    for x in range(100, SCREEN_WIDTH-100, 50):
                        for _ in range(10):
                            color = random.choice(COLORS)
                            self.particles.append(Particle(x, shapes_area_y, color))
            
            # Check for and clear completed rows and columns
            self.check_lines()
            
            # Check if game over (no more valid moves)
            if len(self.available_shapes) == 0 or not self.has_valid_moves():
                self.game_over()
            
            return True
        
        return False
    
    def check_lines(self):
        lines_cleared = 0
        
        # Check rows
        rows_to_clear = []
        for row in range(GRID_HEIGHT):
            if all(self.grid[row][col] for col in range(GRID_WIDTH)):
                rows_to_clear.append(row)
                lines_cleared += 1
        
        # Check columns
        cols_to_clear = []
        for col in range(GRID_WIDTH):
            if all(self.grid[row][col] for row in range(GRID_HEIGHT)):
                cols_to_clear.append(col)
                lines_cleared += 1
        
        # Clear rows
        for row in rows_to_clear:
            for col in range(GRID_WIDTH):
                if self.grid[row][col]:
                    x = GRID_OFFSET_X + (col + 0.5) * BLOCK_SIZE
                    y = GRID_OFFSET_Y + (row + 0.5) * BLOCK_SIZE
                    for _ in range(10):
                        self.particles.append(Particle(x, y, self.grid[row][col].color))
                    self.grid[row][col] = None
        
        # Clear columns
        for col in cols_to_clear:
            for row in range(GRID_HEIGHT):
                if self.grid[row][col]:
                    x = GRID_OFFSET_X + (col + 0.5) * BLOCK_SIZE
                    y = GRID_OFFSET_Y + (row + 0.5) * BLOCK_SIZE
                    for _ in range(10):
                        self.particles.append(Particle(x, y, self.grid[row][col].color))
                    self.grid[row][col] = None
        
        # Calculate score - more lines = higher score
        if lines_cleared > 0:
            points = lines_cleared * 150 * self.level  # Increased base points
            
            # Bonus for multiple lines
            if lines_cleared > 1:
                points += (lines_cleared - 1) * 100 * self.level  # Increased bonus
            
            self.score += points
            
            # Play sound
            if clear_sound:
                clear_sound.play()
            
            # Check for level up
            if self.score >= self.score_target:
                self.level_up()
    
    def has_valid_moves(self):
        # Check if any available shape can be placed on the grid
        if not self.available_shapes:
            return False
            
        # Track shapes that can be placed
        placeable_shapes = 0
        
        for shape in self.available_shapes:
            can_place = False
            for grid_y in range(GRID_HEIGHT):
                for grid_x in range(GRID_WIDTH):
                    if self.can_place_shape_at(shape, grid_x, grid_y):
                        can_place = True
                        placeable_shapes += 1
                        break
                if can_place:
                    break
        
        # Game is not over if at least one shape can be placed
        return placeable_shapes > 0
    
    def level_up(self):
        self.level += 1
        self.score_target += self.level * 750  # Reduced score requirement
        self.time_left += 90  # Add 1.5 minutes instead of 1
        
        # Play sound
        if level_up_sound:
            level_up_sound.play()
        
        # Add more particles for celebration
        for _ in range(50):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT // 3)
            color = random.choice(COLORS)
            self.particles.append(Particle(x, y, color))
    
    def game_over(self):
        self.state = GameState.GAME_OVER
        
        # Play sound
        if game_over_sound:
            game_over_sound.play()
    
    def handle_mouse_down(self, pos):
        x, y = pos
        
        # Check for pause button
        pause_btn = pygame.Rect(SCREEN_WIDTH - 50, 15, 30, 30)
        if pause_btn.collidepoint(pos):
            self.state = GameState.PAUSED
            return
        
        # Start dragging
        shape = self.get_shape_at_pos(pos)
        if shape:
            if click_sound:
                click_sound.play()
            
            self.dragging_shape = shape
            shape.start_drag(x, y)
    
    def handle_mouse_move(self, pos):
        if self.dragging_shape:
            self.dragging_shape.drag(*pos)
    
    def handle_mouse_up(self):
        if self.dragging_shape:
            # Try to place the shape
            if self.ghost_shape:
                # Use ghost shape position for placement
                self.dragging_shape.pos_x = self.ghost_shape.pos_x
                self.dragging_shape.pos_y = self.ghost_shape.pos_y
                placed = self.place_shape(self.dragging_shape)
                
                if not placed:
                    # Return to original position if can't place
                    self.dragging_shape.pos_x, self.dragging_shape.pos_y = self.dragging_shape.original_pos
            else:
                # Return to original position
                self.dragging_shape.pos_x, self.dragging_shape.pos_y = self.dragging_shape.original_pos
            
            self.dragging_shape.end_drag()
            self.dragging_shape = None
            self.ghost_shape = None
    
    def handle_menu_click(self, pos):
        if self.state == GameState.MENU:
            if self.btn_play.collidepoint(pos):
                self.state = GameState.PLAYING
                if click_sound:
                    click_sound.play()
            elif self.btn_quit.collidepoint(pos):
                return False  # Exit game
                
        elif self.state == GameState.GAME_OVER:
            if self.btn_play.collidepoint(pos):
                self.reset_game()
                self.state = GameState.PLAYING
                if click_sound:
                    click_sound.play()
            elif self.btn_quit.collidepoint(pos):
                return False  # Exit game
                
        elif self.state == GameState.PAUSED:
            if self.btn_resume.collidepoint(pos):
                self.state = GameState.PLAYING
                if click_sound:
                    click_sound.play()
            elif self.btn_menu.collidepoint(pos):
                self.reset_game()
                self.state = GameState.MENU
                if click_sound:
                    click_sound.play()
                
        return True  # Continue game

def main():
    game = Game()
    
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    pos = pygame.mouse.get_pos()
                    
                    if game.state == GameState.PLAYING:
                        game.handle_mouse_down(pos)
                    else:
                        running = game.handle_menu_click(pos)
            elif event.type == pygame.MOUSEMOTION:
                if game.state == GameState.PLAYING:
                    game.handle_mouse_move(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and game.state == GameState.PLAYING:
                    game.handle_mouse_up()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game.state == GameState.PLAYING:
                        game.state = GameState.PAUSED
                    elif game.state == GameState.PAUSED:
                        game.state = GameState.PLAYING
        
        game.update()
        game.draw()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()