import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.25
JUMP_HEIGHT = 5
PIPE_GAP = 150
PIPE_VELOCITY = 3
PIPE_FREQUENCY = 1500  # milliseconds

# Colors
PINK = (255, 192, 203)
DARK_PINK = (219, 112, 147)
LIGHT_BLUE = (173, 216, 230)
WHITE = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Labubu")
clock = pygame.time.Clock()

# Load images (placeholder logic - will need actual images)
try:
    # Load background
    bg_img = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_img.fill(LIGHT_BLUE)
    
    # Create Labubu placeholder
    labubu_img = pygame.Surface((50, 50))
    labubu_img.fill(PINK)
    pygame.draw.circle(labubu_img, DARK_PINK, (25, 25), 20)
    labubu_rect = labubu_img.get_rect(center=(100, SCREEN_HEIGHT/2))
    
    # Create pipe placeholder
    pipe_img = pygame.Surface((70, 500))
    pipe_img.fill(DARK_PINK)
    
    # Fonts
    game_font = pygame.font.SysFont('comicsansms', 40)
except Exception as e:
    print(f"Error loading assets: {e}")
    pygame.quit()
    sys.exit()

class Labubu:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT / 2
        self.velocity = 0
        self.rect = labubu_img.get_rect(center=(self.x, self.y))
    
    def jump(self):
        self.velocity = -JUMP_HEIGHT
    
    def update(self):
        # Apply gravity
        self.velocity += GRAVITY
        self.y += self.velocity
        
        # Update rectangle position
        self.rect.centery = self.y
        
        # Keep Labubu on screen
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = 0
            
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity = 0

class Pipe:
    def __init__(self):
        # Random gap position
        gap_y = random.randint(150, SCREEN_HEIGHT - 150)
        
        # Top pipe
        self.top_pipe = pipe_img.get_rect(midbottom=(SCREEN_WIDTH + 80, gap_y - PIPE_GAP//2))
        
        # Bottom pipe
        self.bottom_pipe = pipe_img.get_rect(midtop=(SCREEN_WIDTH + 80, gap_y + PIPE_GAP//2))
        
    def update(self):
        # Move pipes to the left
        self.top_pipe.x -= PIPE_VELOCITY
        self.bottom_pipe.x -= PIPE_VELOCITY
        
    def is_offscreen(self):
        return self.top_pipe.right < 0

def check_collision(labubu, pipes):
    for pipe in pipes:
        if labubu.rect.colliderect(pipe.top_pipe) or labubu.rect.colliderect(pipe.bottom_pipe):
            return True
    
    # Check if Labubu hits the ground or sky
    if labubu.rect.top <= 0 or labubu.rect.bottom >= SCREEN_HEIGHT:
        return True
    
    return False

def display_score(score):
    score_text = game_font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 50))

def display_game_over(score):
    game_over_text = game_font.render('Game Over!', True, WHITE)
    final_score_text = game_font.render(f'Final Score: {score}', True, WHITE)
    restart_text = game_font.render('Press SPACE to restart', True, WHITE)
    
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 1.5))

def game_loop():
    labubu = Labubu()
    pipes = []
    score = 0
    game_active = True
    last_pipe_time = pygame.time.get_ticks()
    passed_pipes = set()
    
    while True:
        current_time = pygame.time.get_ticks()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_active:
                        labubu.jump()
                    else:
                        # Restart game
                        labubu = Labubu()
                        pipes = []
                        score = 0
                        game_active = True
                        last_pipe_time = current_time
                        passed_pipes = set()
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        # Draw background
        screen.blit(bg_img, (0, 0))
        
        if game_active:
            # Update Labubu
            labubu.update()
            screen.blit(labubu_img, labubu.rect)
            
            # Pipe management
            if current_time - last_pipe_time > PIPE_FREQUENCY:
                pipes.append(Pipe())
                last_pipe_time = current_time
            
            # Update and draw pipes
            for pipe in pipes:
                pipe.update()
                screen.blit(pipe_img, pipe.top_pipe)
                screen.blit(pipe_img, pipe.bottom_pipe)
                
                # Score when passing pipes
                if pipe.top_pipe.right < labubu.x and pipe not in passed_pipes:
                    score += 1
                    passed_pipes.add(pipe)
            
            # Remove offscreen pipes
            pipes = [pipe for pipe in pipes if not pipe.is_offscreen()]
            
            # Check for collisions
            if check_collision(labubu, pipes):
                game_active = False
            
            # Display score
            display_score(score)
        else:
            # Game over screen
            display_game_over(score)
        
        # Update display
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()