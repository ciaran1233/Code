import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Evolution")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Bubble class
class Bubble:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 3
        self.abilities = []

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self, keys):
        if keys[pygame.K_UP] and self.y - self.radius > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.radius < HEIGHT:
            self.y += self.speed
        if keys[pygame.K_LEFT] and self.x - self.radius > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.radius < WIDTH:
            self.x += self.speed

    def grow(self, amount):
        self.radius += amount
        if self.radius > 50 and "fire" not in self.abilities:
            self.abilities.append("fire")  # Unlock fire ability
        if self.radius > 80 and "shockwave" not in self.abilities:
            self.abilities.append("shockwave")  # Unlock shockwave ability

    def use_ability(self):
        if "fire" in self.abilities:
            print("Fire ability activated!")
        if "shockwave" in self.abilities:
            print("Shockwave ability activated!")

# Generate random bubbles
def create_bubbles(num):
    bubbles = []
    for _ in range(num):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        radius = random.randint(5, 20)
        color = random.choice([BLUE, GREEN, RED])
        bubbles.append(Bubble(x, y, radius, color))
    return bubbles

# Detect collision
def is_collision(bubble1, bubble2):
    distance = math.sqrt((bubble1.x - bubble2.x)**2 + (bubble1.y - bubble2.y)**2)
    return distance < bubble1.radius + bubble2.radius

# Main game loop
def main():
    running = True
    player = Bubble(WIDTH // 2, HEIGHT // 2, 20, BLUE)
    bubbles = create_bubbles(20)
    score = 0

    while running:
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the player
        player.move(keys)

        # Check collisions and absorb smaller bubbles
        for bubble in bubbles[:]:
            if is_collision(player, bubble):
                if player.radius > bubble.radius:
                    player.grow(1)  # Grow the player bubble
                    bubbles.remove(bubble)  # Remove the absorbed bubble
                    score += 1

        # Draw the bubbles and player
        player.draw(screen)
        for bubble in bubbles:
            bubble.draw(screen)

        # Display score
        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the screen
        pygame.display.update()

        # Frame rate
        clock.tick(FPS)

# Run the game
if __name__ == "__main__":
    main()
