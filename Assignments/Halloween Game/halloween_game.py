import pygame
import random
import math
import datetime
import os
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)

# ============================================
# CUSTOMIZATION: Add your own image paths here
# ============================================
PLAYER_IMAGE_PATH = "Halloween Game/me.png"
GAME_OBJECT_IMAGE_PATH = "Halloween Game/scary_thing.png"
# ============================================

class Player(pygame.sprite.Sprite):
    """Player object controlled by WASD keys"""
    def __init__(self, x, y):
        super().__init__()
        self.size = 30
        
        # Load custom image or use default
        if os.path.exists(PLAYER_IMAGE_PATH):
            self.image = pygame.image.load(PLAYER_IMAGE_PATH)
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        else:
            self.image = pygame.Surface((self.size, self.size))
            self.image.fill(BLUE)
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self, keys):
        """Update player position based on key input"""
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed


class GameObject(pygame.sprite.Sprite):
    """Bouncing object that replicates on wall collision"""
    def __init__(self, x, y, vx=None, vy=None):
        super().__init__()
        self.size = 50
        
        # Load custom image or use default
        if os.path.exists(GAME_OBJECT_IMAGE_PATH):
            self.image = pygame.image.load(GAME_OBJECT_IMAGE_PATH)
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        else:
            self.image = pygame.Surface((self.size, self.size))
            self.image.fill(RED)
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # Set velocity
        if vx is None or vy is None:
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(3, 6)
            self.vx = math.cos(angle) * speed
            self.vy = math.sin(angle) * speed
        else:
            self.vx = vx
            self.vy = vy
        
        self.has_replicated = False

    def update(self):
        """Update position and handle wall collisions"""
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        # Check wall collisions and replicate
        replicated = False
        
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.vx = -self.vx
            self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.size))
            replicated = True
        
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.vy = -self.vy
            self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.size))
            replicated = True
        
        return replicated

    def create_offspring(self):
        """Create a new game object moving away from wall"""
        # Create velocity perpendicular to current direction
        angle = math.atan2(self.vy, self.vx) + random.uniform(-math.pi/4, math.pi/4)
        speed = random.uniform(3, 6)
        new_vx = math.cos(angle) * speed
        new_vy = math.sin(angle) * speed
        
        return GameObject(self.rect.centerx, self.rect.centery, new_vx, new_vy)


class Game:
    """Main game class"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Dodge Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.running = True
        self.game_active = False
        self.start_time = 0
        self.survival_time = 0
        self.high_scores = []
        self.load_high_scores()

    def load_high_scores(self):
        """Load high scores from file"""
        if os.path.exists("high_scores.txt"):
            with open("high_scores.txt", "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        self.high_scores.append({
                            "time": float(parts[0]),
                            "date": parts[1],
                            "username": parts[2]
                        })
            self.high_scores.sort(key=lambda x: x["time"], reverse=True)

    def save_high_score(self, survival_time, username):
        """Save a new high score to file"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("high_scores.txt", "a") as f:
            f.write(f"{survival_time}|{timestamp}|{username}\n")
        
        self.high_scores.append({
            "time": survival_time,
            "date": timestamp,
            "username": username
        })
        self.high_scores.sort(key=lambda x: x["time"], reverse=True)

    def start_game(self):
        """Initialize a new game"""
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.player_group = pygame.sprite.GroupSingle(self.player)
        
        self.game_objects = pygame.sprite.Group()
        initial_obj = GameObject(
            random.randint(50, SCREEN_WIDTH - 50),
            random.randint(50, SCREEN_HEIGHT - 50)
        )
        self.game_objects.add(initial_obj)
        
        self.start_time = pygame.time.get_ticks()
        self.game_active = True

    def display_timer(self):
        """Display survival timer"""
        if self.game_active:
            elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
            self.survival_time = elapsed
        
        timer_text = self.font.render(f"Time: {self.survival_time:.2f}s", True, BLACK)
        self.screen.blit(timer_text, (SCREEN_WIDTH - 200, 10))

    def display_high_scores(self):
        """Display top 10 high scores"""
        title = self.font.render("TOP 10 HIGH SCORES", True, BLACK)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        y_offset = 150
        for i, score in enumerate(self.high_scores[:10]):
            score_text = self.small_font.render(
                f"{i+1}. {score['time']:.2f}s - {score['username']} ({score['date']})",
                True, BLACK
            )
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            self.screen.blit(score_text, score_rect)
            y_offset += 30

    def get_username(self):
        """Get username from player"""
        username = ""
        input_active = True
        
        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and username:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    elif len(username) < 20 and event.unicode.isprintable():
                        username += event.unicode
            
            self.screen.fill(WHITE)
            prompt = self.font.render("Enter your name:", True, BLACK)
            prompt_rect = prompt.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            self.screen.blit(prompt, prompt_rect)
            
            name_text = self.font.render(username + "_", True, BLUE)
            name_rect = name_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(name_text, name_rect)
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        return username

    def run(self):
        """Main game loop"""
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.game_active:
                        self.start_game()

            if self.game_active:
                # Get keys
                keys = pygame.key.get_pressed()
                
                # Update player
                self.player.update(keys)
                
                # Update game objects and handle replication
                new_objects = []
                for obj in self.game_objects:
                    if obj.update() and not obj.has_replicated:
                        obj.has_replicated = True
                        new_objects.append(obj.create_offspring())
                
                # Add new objects
                for new_obj in new_objects:
                    self.game_objects.add(new_obj)
                
                # Check collision
                if pygame.sprite.spritecollide(self.player, self.game_objects, False):
                    self.game_active = False
                    username = self.get_username()
                    if username:
                        self.save_high_score(self.survival_time, username)
                    else:
                        self.running = False
                
                # Draw everything
                self.screen.fill(WHITE)
                self.player_group.draw(self.screen)
                self.game_objects.draw(self.screen)
                self.display_timer()
                
            else:
                # Game over screen
                
                self.image = pygame.image.load(PLAYER_IMAGE_PATH)
                self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH,SCREEN_HEIGHT))

                time.sleep(5)
                
                self.screen.fill(WHITE)
                
                game_over = self.font.render("GAME OVER", True, RED)
                game_over_rect = game_over.get_rect(center=(SCREEN_WIDTH // 2, 50))
                self.screen.blit(game_over, game_over_rect)
                
                self.display_high_scores()
                
                restart = self.small_font.render("Press SPACE to play again", True, GRAY)
                restart_rect = restart.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
                self.screen.blit(restart, restart_rect)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()