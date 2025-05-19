import pygame
import sys
import random
import math
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Game constants
SCREEN_WIDTH = 800  # Wider screen for the whimsical, airy feeling
SCREEN_HEIGHT = 600
GRAVITY = 0.25
JUMP_HEIGHT = 5
OBSTACLE_GAP = 200  # Wider gap between obstacles
OBSTACLE_VELOCITY = 2.5  # Slightly slower for a dreamier pace
OBSTACLE_FREQUENCY = 2000  # milliseconds

# Colors (Labubu storybook aesthetic)
PASTEL_GREEN = (183, 234, 176)
PASTEL_PINK = (255, 209, 220)
PASTEL_BLUE = (173, 216, 255)
WARM_BROWN = (210, 180, 140)
SKY_BLUE = (135, 206, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game assets directory
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

# Ensure the assets directory exists
if not os.path.exists(ASSETS_DIR):
    try:
        os.makedirs(ASSETS_DIR)
        os.makedirs(os.path.join(ASSETS_DIR, "images"), exist_ok=True)
        os.makedirs(os.path.join(ASSETS_DIR, "sounds"), exist_ok=True)
        print(f"Created assets directories at {ASSETS_DIR}")
    except Exception as e:
        print(f"Could not create assets directory: {e}")

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Labubu")
icon = pygame.Surface((32, 32), pygame.SRCALPHA)
pygame.draw.circle(icon, PASTEL_PINK, (16, 16), 16)
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Create storybook-themed assets
def create_labubu_character():
    """Create a Labubu character in a bunny onesie"""
    img = pygame.Surface((80, 80), pygame.SRCALPHA)
    
    # Body - round and plush
    pygame.draw.circle(img, PASTEL_PINK, (40, 45), 30)
    
    # Bunny hood (top of head)
    pygame.draw.circle(img, PASTEL_PINK, (40, 25), 25)
    
    # Bunny ears - positioned above the head
    pygame.draw.ellipse(img, PASTEL_PINK, (15, -25, 20, 40))
    pygame.draw.ellipse(img, PASTEL_PINK, (45, -25, 20, 40))
    
    # Inner ears
    pygame.draw.ellipse(img, WHITE, (20, -20, 10, 25))
    pygame.draw.ellipse(img, WHITE, (50, -20, 10, 25))
    
    # Eyes - big and expressive
    pygame.draw.circle(img, WHITE, (30, 30), 10)
    pygame.draw.circle(img, WHITE, (50, 30), 10)
    pygame.draw.circle(img, BLACK, (32, 30), 5)
    pygame.draw.circle(img, BLACK, (48, 30), 5)
    
    # Reflection in eyes
    pygame.draw.circle(img, WHITE, (34, 28), 2)
    pygame.draw.circle(img, WHITE, (50, 28), 2)
    
    # Cute smile with teeth
    pygame.draw.arc(img, BLACK, (25, 35, 30, 20), 0, math.pi, 2)
    
    # Little teeth
    pygame.draw.rect(img, WHITE, (35, 45, 5, 5))
    pygame.draw.rect(img, WHITE, (42, 45, 5, 5))
    
    # Tiny arms
    pygame.draw.ellipse(img, PASTEL_PINK, (15, 40, 15, 10))
    pygame.draw.ellipse(img, PASTEL_PINK, (50, 40, 15, 10))
    
    # Tiny feet
    pygame.draw.ellipse(img, PASTEL_PINK, (30, 65, 10, 15))
    pygame.draw.ellipse(img, PASTEL_PINK, (45, 65, 10, 15))
    
    return img

def create_cloud_obstacle():
    """Create a fluffy cloud obstacle instead of a pipe"""
    img = pygame.Surface((120, 300), pygame.SRCALPHA)
    
    # Main cloud body
    pygame.draw.ellipse(img, WHITE, (0, 100, 120, 100))
    pygame.draw.ellipse(img, WHITE, (20, 80, 80, 140))
    pygame.draw.ellipse(img, WHITE, (10, 60, 100, 120))
    
    # Add some shading for dimension
    for i in range(3):
        x = random.randint(20, 100)
        y = random.randint(100, 180)
        size = random.randint(20, 40)
        pygame.draw.circle(img, PASTEL_BLUE, (x, y), size)
    
    return img

def create_background():
    """Create a whimsical storybook background"""
    img = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Gradient sky - soft, dreamy atmosphere
    for y in range(SCREEN_HEIGHT):
        # Transition from sky blue at top to pastel pink near bottom
        ratio = y / SCREEN_HEIGHT
        r = int(SKY_BLUE[0] * (1 - ratio) + PASTEL_PINK[0] * ratio * 0.7)
        g = int(SKY_BLUE[1] * (1 - ratio) + PASTEL_PINK[1] * ratio * 0.7)
        b = int(SKY_BLUE[2] * (1 - ratio) + PASTEL_PINK[2] * ratio * 0.7)
        pygame.draw.line(img, (r, g, b), (0, y), (SCREEN_WIDTH, y))
    
    # Add distant hills (rounded shapes)
    for i in range(5):
        width = random.randint(200, 400)
        height = random.randint(100, 150)
        x = random.randint(-100, SCREEN_WIDTH)
        y = SCREEN_HEIGHT - height//2
        
        # Draw hills with varying shades of green
        green_shade = (
            PASTEL_GREEN[0] - random.randint(-20, 20),
            PASTEL_GREEN[1] - random.randint(-20, 20),
            PASTEL_GREEN[2] - random.randint(-20, 20)
        )
        pygame.draw.ellipse(img, green_shade, (x, y, width, height))
    
    # Add some distant cottages
    for i in range(3):
        x = random.randint(50, SCREEN_WIDTH - 100)
        house_width = random.randint(60, 100)
        house_height = random.randint(40, 70)
        y = SCREEN_HEIGHT - house_height - random.randint(30, 60)
        
        # House body
        pygame.draw.rect(img, WARM_BROWN, (x, y, house_width, house_height))
        
        # Roof
        roof_points = [
            (x - 10, y),
            (x + house_width + 10, y),
            (x + house_width//2, y - 30)
        ]
        pygame.draw.polygon(img, PASTEL_PINK, roof_points)
        
        # Window
        window_size = house_width // 4
        window_x = x + (house_width - window_size) // 2
        window_y = y + (house_height - window_size) // 2
        pygame.draw.rect(img, PASTEL_BLUE, (window_x, window_y, window_size, window_size))
        pygame.draw.line(img, WHITE, (window_x, window_y + window_size//2), 
                        (window_x + window_size, window_y + window_size//2), 2)
        pygame.draw.line(img, WHITE, (window_x + window_size//2, window_y), 
                        (window_x + window_size//2, window_y + window_size), 2)
    
    return img

def create_ground():
    """Create a soft, grassy ground"""
    img = pygame.Surface((SCREEN_WIDTH, 100), pygame.SRCALPHA)
    
    # Main ground
    pygame.draw.rect(img, PASTEL_GREEN, (0, 0, SCREEN_WIDTH, 100))
    
    # Add some texture with little grass tufts
    for i in range(100):
        x = random.randint(0, SCREEN_WIDTH)
        height = random.randint(5, 15)
        width = random.randint(3, 8)
        green_shade = (
            PASTEL_GREEN[0] - random.randint(0, 30),
            PASTEL_GREEN[1] - random.randint(0, 30),
            PASTEL_GREEN[2] - random.randint(0, 30)
        )
        pygame.draw.ellipse(img, green_shade, (x, 0, width, height))
    
    # Add some flowers
    for i in range(20):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(10, 70)
        size = random.randint(5, 10)
        
        # Flower color varies between pink and white
        if random.random() > 0.5:
            color = PASTEL_PINK
        else:
            color = WHITE
            
        pygame.draw.circle(img, color, (x, y), size)
        pygame.draw.circle(img, (255, 255, 150), (x, y), size//2)  # Yellow center
    
    return img

def create_butterfly():
    """Create a cute butterfly decoration"""
    img = pygame.Surface((30, 30), pygame.SRCALPHA)
    
    # Wings
    colors = [PASTEL_PINK, PASTEL_BLUE, (255, 255, 150)]
    color = random.choice(colors)
    
    pygame.draw.circle(img, color, (8, 10), 10)
    pygame.draw.circle(img, color, (22, 10), 10)
    pygame.draw.circle(img, color, (8, 20), 10)
    pygame.draw.circle(img, color, (22, 20), 10)
    
    # Body
    pygame.draw.line(img, BLACK, (15, 5), (15, 25), 3)
    
    # Antennae
    pygame.draw.line(img, BLACK, (15, 5), (10, 0), 2)
    pygame.draw.line(img, BLACK, (15, 5), (20, 0), 2)
    
    return img

# Load/create assets
try:
    # Create background
    bg_img = create_background()
    
    # Create Labubu character
    labubu_img = create_labubu_character()
    labubu_rect = labubu_img.get_rect(center=(200, SCREEN_HEIGHT/2))
    
    # Create cloud obstacle
    cloud_obstacle_img = create_cloud_obstacle()
    
    # Create ground
    ground_img = create_ground()
    ground_rect = ground_img.get_rect(topleft=(0, SCREEN_HEIGHT - 100))
    
    # Create butterfly
    butterfly_img = create_butterfly()
    
    # Fonts - try to use a cute, playful font
    try:
        # Look for fun, playful fonts that might be available on the system
        font_options = ['comicsansms', 'chalkduster', 'marker felt', 'papyrus', 'fantasy']
        
        # Try each font option
        for font_name in font_options:
            try:
                game_font = pygame.font.SysFont(font_name, 40)
                title_font = pygame.font.SysFont(font_name, 60)
                print(f"Using font: {font_name}")
                break
            except:
                continue
        else:
            # If no fun fonts available, fall back to default
            game_font = pygame.font.Font(None, 40)
            title_font = pygame.font.Font(None, 60)
    except:
        game_font = pygame.font.SysFont('arial', 40)
        title_font = pygame.font.SysFont('arial', 60)
    
    # Sound effects
    jump_sound = None
    score_sound = None
    hit_sound = None
    
    # Try to create simple sound effects if mixer is initialized
    try:
        if pygame.mixer.get_init():
            # Create simple placeholder sounds
            empty_buffer = bytes([128] * 1000)  # Small buffer for minimal sounds
            
            jump_sound = pygame.mixer.Sound(buffer=empty_buffer)
            jump_sound.set_volume(0.3)
            
            score_sound = pygame.mixer.Sound(buffer=empty_buffer)
            score_sound.set_volume(0.3)
            
            hit_sound = pygame.mixer.Sound(buffer=empty_buffer)
            hit_sound.set_volume(0.5)
            
            print("Sound effects enabled!")
    except Exception as sound_error:
        print(f"Could not create sound effects: {sound_error}")
        jump_sound = None
        score_sound = None
        hit_sound = None

except Exception as e:
    print(f"Error loading assets: {e}")
    pygame.quit()
    sys.exit()

class Labubu:
    def __init__(self):
        self.x = 200
        self.y = SCREEN_HEIGHT / 2
        self.velocity = 0
        self.rect = labubu_img.get_rect(center=(self.x, self.y))
        self.angle = 0
        
        # Animation variables
        self.animation_frames = []
        self.current_frame = 0
        self.animation_speed = 0.1
        self.animation_time = 0
        
        # Create a simple bouncing animation by scaling
        self.scale_factor = 1.0
        self.scale_direction = 0.005
    
    def jump(self):
        self.velocity = -JUMP_HEIGHT
        # Play jump sound if available
        if jump_sound:
            jump_sound.play()
    
    def update(self, dt):
        # Apply gravity
        self.velocity += GRAVITY
        self.y += self.velocity
        
        # Update rectangle position
        self.rect.centery = self.y
        
        # Simple squash and stretch animation
        self.scale_factor += self.scale_direction
        if self.scale_factor > 1.05 or self.scale_factor < 0.95:
            self.scale_direction *= -1
        
        # Tilt Labubu based on velocity for flying effect
        self.angle = -self.velocity * 2
        if self.angle < -20:
            self.angle = -20
        if self.angle > 20:
            self.angle = 20
        
        # Keep Labubu above ground
        if self.rect.bottom >= SCREEN_HEIGHT - 100:
            self.rect.bottom = SCREEN_HEIGHT - 100
            self.velocity = 0
            
        # Keep Labubu below top of screen
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = 0
    
    def draw(self, surface):
        # Create squashed/stretched version for bouncy effect
        w = labubu_img.get_width()
        h = labubu_img.get_height()
        
        # Inverse relationship between x and y scaling
        scaled_w = int(w * (2 - self.scale_factor))
        scaled_h = int(h * self.scale_factor)
        
        scaled_labubu = pygame.transform.scale(labubu_img, (scaled_w, scaled_h))
        
        # Rotate Labubu image based on velocity
        rotated_labubu = pygame.transform.rotate(scaled_labubu, self.angle)
        rotated_rect = rotated_labubu.get_rect(center=self.rect.center)
        surface.blit(rotated_labubu, rotated_rect)

class CloudObstacle:
    def __init__(self):
        # Random gap position
        gap_y = random.randint(200, SCREEN_HEIGHT - 250)
        
        # Top cloud
        self.top_cloud = cloud_obstacle_img.get_rect(midbottom=(SCREEN_WIDTH + 80, gap_y - OBSTACLE_GAP//2))
        
        # Bottom cloud
        self.bottom_cloud = cloud_obstacle_img.get_rect(midtop=(SCREEN_WIDTH + 80, gap_y + OBSTACLE_GAP//2))
        
        # Flag to track if this obstacle has been passed
        self.scored = False
        
        # Variation in cloud appearance
        self.scale_top = random.uniform(0.9, 1.1)
        self.scale_bottom = random.uniform(0.9, 1.1)
        
    def update(self):
        # Move obstacles to the left
        self.top_cloud.x -= OBSTACLE_VELOCITY
        self.bottom_cloud.x -= OBSTACLE_VELOCITY
        
    def draw(self, surface):
        # Scale the cloud images slightly differently for variety
        top_cloud_img = pygame.transform.scale(
            cloud_obstacle_img, 
            (int(cloud_obstacle_img.get_width() * self.scale_top), 
             int(cloud_obstacle_img.get_height() * self.scale_top))
        )
        
        bottom_cloud_img = pygame.transform.scale(
            cloud_obstacle_img, 
            (int(cloud_obstacle_img.get_width() * self.scale_bottom), 
             int(cloud_obstacle_img.get_height() * self.scale_bottom))
        )
        
        # Draw top cloud (flipped)
        flipped_cloud = pygame.transform.flip(top_cloud_img, False, True)
        top_rect = flipped_cloud.get_rect(midbottom=self.top_cloud.midbottom)
        surface.blit(flipped_cloud, top_rect)
        
        # Draw bottom cloud
        bottom_rect = bottom_cloud_img.get_rect(midtop=self.bottom_cloud.midtop)
        surface.blit(bottom_cloud_img, bottom_rect)
        
    def is_offscreen(self):
        return self.top_cloud.right < 0

class FloatingCloud:
    def __init__(self):
        self.size = random.randint(60, 120)
        self.x = SCREEN_WIDTH + self.size
        self.y = random.randint(50, SCREEN_HEIGHT - 200)
        self.speed = random.uniform(0.5, 1.5)
        
        # Cloud parts positioning
        self.parts = []
        for _ in range(random.randint(3, 6)):
            x_offset = random.randint(-self.size//2, self.size//2)
            y_offset = random.randint(-self.size//4, self.size//4)
            size_factor = random.uniform(0.5, 1.0)
            self.parts.append((x_offset, y_offset, size_factor))
        
    def update(self):
        self.x -= self.speed
        
    def draw(self, surface):
        # Use a slightly different shade for background clouds to visually distinguish them
        # from obstacle clouds (WHITE). This makes it clear these won't hurt the player
        soft_cloud_color = (240, 248, 255)  # Very light blue tint
        
        for x_offset, y_offset, size_factor in self.parts:
            part_size = int(self.size * size_factor)
            pygame.draw.circle(
                surface, 
                soft_cloud_color, 
                (int(self.x + x_offset), int(self.y + y_offset)), 
                part_size
            )
        
    def is_offscreen(self):
        return self.x < -self.size * 2

class Butterfly:
    def __init__(self):
        self.x = SCREEN_WIDTH + 30
        self.y = random.randint(100, SCREEN_HEIGHT - 200)
        self.speed = random.uniform(1.0, 2.0)
        self.amplitude = random.randint(20, 50)
        self.frequency = random.uniform(0.05, 0.1)
        self.time = random.uniform(0, 100)  # Random starting phase
        
    def update(self):
        self.x -= self.speed
        self.time += 0.1
        self.y += math.sin(self.time * self.frequency) * self.amplitude * 0.05
        
    def draw(self, surface):
        # Gently rotate the butterfly based on its vertical movement
        angle = math.sin(self.time * self.frequency) * 15
        rotated_butterfly = pygame.transform.rotate(butterfly_img, angle)
        butterfly_rect = rotated_butterfly.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(rotated_butterfly, butterfly_rect)
        
    def is_offscreen(self):
        return self.x < -30

def check_collision(labubu, obstacles, clouds):
    # Check collision with obstacle clouds only (not background clouds)
    for obstacle in obstacles:
        # Using a more precise collision detection for obstacles
        # Shrink the collision rectangles by 10 pixels on each side to make the hitboxes
        # more forgiving and match the visual appearance better
        top_cloud_hitbox = obstacle.top_cloud.inflate(-20, -20)
        bottom_cloud_hitbox = obstacle.bottom_cloud.inflate(-20, -20)
        
        if labubu.rect.colliderect(top_cloud_hitbox) or labubu.rect.colliderect(bottom_cloud_hitbox):
            if hit_sound:
                hit_sound.play()
            return True
    
    # Check if Labubu hits the ground
    if labubu.rect.bottom >= SCREEN_HEIGHT - 100:
        if hit_sound:
            hit_sound.play()
        return True
    
    # Check if Labubu hits the sky
    if labubu.rect.top <= 0:
        if hit_sound:
            hit_sound.play()
        return True
    
    # Background clouds are purely decorative and should not trigger collision
    # No need to check collisions with floating clouds
    
    return False

def display_score(score):
    # Create gradient shadow effect for score
    shadow_layers = 3
    for i in range(shadow_layers, 0, -1):
        score_shadow = game_font.render(f'Score: {score}', True, (0, 0, 0, 128//i))
        shadow_offset = i
        screen.blit(score_shadow, (SCREEN_WIDTH // 2 - score_shadow.get_width() // 2 + shadow_offset, 
                                 50 + shadow_offset))
    
    # Draw actual score text
    score_text = game_font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 50))

def display_game_over(score):
    # Semi-transparent overlay
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))
    screen.blit(overlay, (0, 0))
    
    # Game over text
    game_over_text = title_font.render('Game Over!', True, WHITE)
    final_score_text = game_font.render(f'Final Score: {score}', True, WHITE)
    restart_text = game_font.render('Press SPACE to restart', True, WHITE)
    
    # Drop shadows for better visibility
    shadow_offset = 3
    game_over_shadow = title_font.render('Game Over!', True, BLACK)
    final_score_shadow = game_font.render(f'Final Score: {score}', True, BLACK)
    restart_shadow = game_font.render('Press SPACE to restart', True, BLACK)
    
    # Draw shadows
    screen.blit(game_over_shadow, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2 + shadow_offset, 
                                  SCREEN_HEIGHT // 3 + shadow_offset))
    screen.blit(final_score_shadow, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2 + shadow_offset, 
                                    SCREEN_HEIGHT // 2 + shadow_offset))
    screen.blit(restart_shadow, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2 + shadow_offset, 
                                SCREEN_HEIGHT // 1.5 + shadow_offset))
    
    # Draw text
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 1.5))
    
    # Draw sad Labubu
    scaled_labubu = pygame.transform.scale(labubu_img, (120, 120))
    screen.blit(scaled_labubu, scaled_labubu.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.2)))

def display_start_screen():
    current_time = pygame.time.get_ticks()
    pulse_scale = 1.0 + 0.05 * math.sin(current_time * 0.005)  # Gentle pulse effect
    bob_offset = 5 * math.sin(current_time * 0.003)  # Gentle bobbing effect
    
    # Title with colorful, fun effect
    rainbow_colors = [
        (255, 100, 100),  # Red
        (255, 150, 100),  # Orange
        (255, 255, 100),  # Yellow
        (100, 255, 100),  # Green
        (100, 100, 255),  # Blue
        (200, 100, 255),  # Purple
    ]
    
    # Use current time to cycle through colors
    color_index = (current_time // 500) % len(rainbow_colors)
    title_color = rainbow_colors[color_index]
    
    # Title with dreamy effect
    title_text = title_font.render('Flappy Labubu!', True, title_color)
    
    # Subtitle
    subtitle_text = game_font.render('A Whimsical Adventure', True, PASTEL_PINK)
    
    # Instructions with animation
    space_color = (255, 255, 255, int(255 * (0.7 + 0.3 * math.sin(current_time * 0.01))))
    start_text = game_font.render('Press SPACE to start', True, space_color)
    controls_text = pygame.font.SysFont('arial', 18).render('SPACE to jump | F2 for screenshot | ESC to quit', True, WHITE)
    credit_text = pygame.font.SysFont('arial', 16).render('Inspired by Kasing Lung\'s Labubu', True, WHITE)
    
    # Draw title with shadow
    shadow_offset = 3
    title_shadow = title_font.render('Flappy Labubu!', True, BLACK)
    subtitle_shadow = game_font.render('A Whimsical Adventure', True, BLACK)
    start_shadow = game_font.render('Press SPACE to start', True, BLACK)
    
    # Draw bouncing title
    title_y = SCREEN_HEIGHT // 4 + int(bob_offset)
    
    screen.blit(title_shadow, (SCREEN_WIDTH // 2 - title_text.get_width() // 2 + shadow_offset, 
                              title_y + shadow_offset))
    screen.blit(subtitle_shadow, (SCREEN_WIDTH // 2 - subtitle_text.get_width() // 2 + shadow_offset, 
                                 title_y + 70 + shadow_offset))
    screen.blit(start_shadow, (SCREEN_WIDTH // 2 - start_text.get_width() // 2 + shadow_offset, 
                              SCREEN_HEIGHT // 2 + shadow_offset))
    
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, title_y))
    screen.blit(subtitle_text, (SCREEN_WIDTH // 2 - subtitle_text.get_width() // 2, title_y + 70))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(controls_text, (SCREEN_WIDTH // 2 - controls_text.get_width() // 2, SCREEN_HEIGHT - 60))
    screen.blit(credit_text, (SCREEN_WIDTH // 2 - credit_text.get_width() // 2, SCREEN_HEIGHT - 30))
    
    # Draw animated instruction arrow
    arrow_y = SCREEN_HEIGHT // 2 + 60 + int(5 * math.sin(current_time * 0.01))
    arrow_points = [
        (SCREEN_WIDTH // 2, arrow_y),
        (SCREEN_WIDTH // 2 - 15, arrow_y - 20),
        (SCREEN_WIDTH // 2 + 15, arrow_y - 20)
    ]
    pygame.draw.polygon(screen, PASTEL_PINK, arrow_points)
    
    # Draw large Labubu bouncing in the middle
    scaled_size = int(160 * pulse_scale)
    scaled_labubu = pygame.transform.scale(labubu_img, (scaled_size, scaled_size))
    labubu_rect = scaled_labubu.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + int(bob_offset * 2)))
    
    # Add a gentle rotation to the Labubu for fun
    angle = 5 * math.sin(current_time * 0.002)
    rotated_labubu = pygame.transform.rotate(scaled_labubu, angle)
    rotated_rect = rotated_labubu.get_rect(center=labubu_rect.center)
    
    # Draw with glow effect (multiple layers with decreasing opacity)
    glow_size = int(scaled_size * 1.1)
    glow_surf = pygame.Surface((glow_size, glow_size), pygame.SRCALPHA)
    pygame.draw.circle(glow_surf, (255, 255, 255, 50), (glow_size//2, glow_size//2), glow_size//2)
    glow_rect = glow_surf.get_rect(center=rotated_rect.center)
    screen.blit(glow_surf, glow_rect)
    
    screen.blit(rotated_labubu, rotated_rect)

def game_loop():
    labubu = Labubu()
    obstacles = []
    clouds = []
    butterflies = []
    score = 0
    
    # Game states
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2
    game_state = MENU
    
    last_obstacle_time = pygame.time.get_ticks()
    last_cloud_time = pygame.time.get_ticks()
    last_butterfly_time = pygame.time.get_ticks()
    
    while True:
        # Calculate delta time for smoother animations
        dt = clock.tick(60) / 1000.0  # Time in seconds since last frame
        current_time = pygame.time.get_ticks()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_state == MENU:
                        game_state = PLAYING
                    elif game_state == PLAYING:
                        labubu.jump()
                    elif game_state == GAME_OVER:
                        # Restart game
                        labubu = Labubu()
                        obstacles = []
                        clouds = []
                        butterflies = []
                        score = 0
                        game_state = PLAYING
                        last_obstacle_time = current_time
                        last_cloud_time = current_time
                        last_butterfly_time = current_time
                
                # Screenshot feature with F2 key
                if event.key == pygame.K_F2:
                    try:
                        # Create a timestamp for the filename
                        timestamp = pygame.time.get_ticks()
                        screenshot_path = os.path.join(ASSETS_DIR, "images", f"flappy_labubu_screenshot_{timestamp}.png")
                        pygame.image.save(screen, screenshot_path)
                        
                        # Show a quick notification that fades out
                        print(f"Screenshot saved to {screenshot_path}")
                        
                        # Visual feedback for screenshot
                        flash_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                        flash_surface.fill((255, 255, 255, 50))  # Semi-transparent white
                        screen.blit(flash_surface, (0, 0))
                        pygame.display.update()
                    except Exception as screenshot_error:
                        print(f"Could not save screenshot: {screenshot_error}")
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        # Draw background
        screen.blit(bg_img, (0, 0))
        
        # Update and draw background clouds in all game states
        if current_time - last_cloud_time > 3000:  # Add new cloud every 3 seconds
            clouds.append(FloatingCloud())
            last_cloud_time = current_time
            
        for cloud in clouds:
            cloud.update()
            cloud.draw(screen)
            
        # Update and draw butterflies in all game states
        if current_time - last_butterfly_time > 5000:  # Add new butterfly every 5 seconds
            butterflies.append(Butterfly())
            last_butterfly_time = current_time
            
        for butterfly in butterflies:
            butterfly.update()
            butterfly.draw(screen)
            
        # Remove offscreen clouds and butterflies
        clouds = [cloud for cloud in clouds if not cloud.is_offscreen()]
        butterflies = [butterfly for butterfly in butterflies if not butterfly.is_offscreen()]
        
        if game_state == MENU:
            display_start_screen()
            
        elif game_state == PLAYING:
            # Update Labubu
            labubu.update(dt)
            labubu.draw(screen)
            
            # Obstacle management
            if current_time - last_obstacle_time > OBSTACLE_FREQUENCY:
                obstacles.append(CloudObstacle())
                last_obstacle_time = current_time
            
            # Update and draw obstacles
            for obstacle in obstacles:
                obstacle.update()
                obstacle.draw(screen)
                
                # Score when passing obstacles
                if obstacle.top_cloud.right < labubu.rect.left and not obstacle.scored:
                    score += 1
                    obstacle.scored = True
                    if score_sound:
                        score_sound.play()
                    
                    # Create visual feedback for scoring
                    # Add a little celebration particle effect
                    for _ in range(15):
                        particle_size = random.randint(3, 8)
                        particle_color = random.choice([PASTEL_PINK, PASTEL_BLUE, (255, 255, 150)])
                        particle_x = labubu.rect.centerx + random.randint(-20, 20)
                        particle_y = labubu.rect.centery + random.randint(-20, 20)
                        pygame.draw.circle(screen, particle_color, (particle_x, particle_y), particle_size)
                    
                    # Flash the score display
                    large_score = title_font.render(f"+1", True, (255, 255, 150))
                    screen.blit(large_score, large_score.get_rect(center=(SCREEN_WIDTH // 2, 120)))
            
            # Remove offscreen obstacles
            obstacles = [obstacle for obstacle in obstacles if not obstacle.is_offscreen()]
            
            # Check for collisions
            if check_collision(labubu, obstacles, clouds):
                game_state = GAME_OVER
            
            # Display score
            display_score(score)
            
            # Display controls hint that fades out after a few seconds
            if current_time < last_obstacle_time + 5000:  # Show for 5 seconds from game start
                hint_opacity = min(255, max(0, 255 - (current_time - last_obstacle_time) // 20))
                hint_color = (255, 255, 255, hint_opacity)
                hint_text = pygame.font.SysFont('arial', 20).render('Press SPACE to flap wings', True, hint_color)
                screen.blit(hint_text, (SCREEN_WIDTH // 2 - hint_text.get_width() // 2, SCREEN_HEIGHT - 150))
            
        elif game_state == GAME_OVER:
            # Draw game elements in frozen state
            for obstacle in obstacles:
                obstacle.draw(screen)
                
            labubu.draw(screen)
            display_game_over(score)
        
        # Always draw ground
        screen.blit(ground_img, ground_rect)
        
        # Update display
        pygame.display.update()

if __name__ == "__main__":
    game_loop()