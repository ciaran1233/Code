import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)  # Define GREEN for health bar

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Combat Arena")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Bubble class
class Bubble:
    def __init__(self, x, y, radius, color, controls):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.controls = controls
        self.speed = 5
        self.health = 100

    def draw(self, screen):
        # Draw the bubble
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Draw health bar (above the bubble)
        pygame.draw.rect(screen, RED, (self.x - 20, self.y - self.radius - 10, 40, 5))
        pygame.draw.rect(screen, GREEN, (self.x - 20, self.y - self.radius - 10, 40 * (self.health / 100), 5))

    def move(self, keys):
        if keys[self.controls['up']] and self.y - self.radius > 0:
            self.y -= self.speed
        if keys[self.controls['down']] and self.y + self.radius < HEIGHT:
            self.y += self.speed
        if keys[self.controls['left']] and self.x - self.radius > 0:
            self.x -= self.speed
        if keys[self.controls['right']] and self.x + self.radius < WIDTH:
            self.x += self.speed

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

# Detect collision between bubbles
def is_collision(bubble1, bubble2):
    distance = math.sqrt((bubble1.x - bubble2.x) ** 2 + (bubble1.y - bubble2.y) ** 2)
    return distance < bubble1.radius + bubble2.radius

# Main game loop
def main():
    running = True

    # Create player bubbles
    player1 = Bubble(200, HEIGHT // 2, 30, BLUE, {
        'up': pygame.K_w,
        'down': pygame.K_s,
        'left': pygame.K_a,
        'right': pygame.K_d
    })
    
    player2 = Bubble(600, HEIGHT // 2, 30, RED, {
        'up': pygame.K_UP,
        'down': pygame.K_DOWN,
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT
    })

    while running:
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()

        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move players
        player1.move(keys)
        player2.move(keys)

        # Check for collisions and apply damage
        if is_collision(player1, player2):
            player1.take_damage(1)
            player2.take_damage(1)

        # Draw players
        player1.draw(screen)
        player2.draw(screen)

        # Check win conditions
        if player1.health <= 0:
            print("Player 2 Wins!")
            running = False
        elif player2.health <= 0:
            print("Player 1 Wins!")
            running = False

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
