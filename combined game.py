import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 50, 255)
GREEN = (50, 255, 50)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 50)
PURPLE = (128, 0, 128)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Bubble Game")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Projectile Class
class Projectile:
    def __init__(self, x, y, angle, speed, color):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.color = color
        self.radius = 5

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Bubble Class
class Bubble:
    def __init__(self, x, y, radius, color, controls):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.controls = controls
        self.speed = 5
        self.health = 100
        self.energy = 100  # Energy for using abilities
        self.abilities = []  # Unlocked abilities
        self.projectiles = []  # List to store projectiles

    def draw(self, screen):
        # Draw the bubble
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Draw health bar
        pygame.draw.rect(screen, RED, (self.x - 30, self.y - self.radius - 15, 60, 5))
        pygame.draw.rect(screen, GREEN, (self.x - 30, self.y - self.radius - 15, 60 * (self.health / 100), 5))
        
        # Draw energy bar
        pygame.draw.rect(screen, BLACK, (self.x - 30, self.y - self.radius - 25, 60, 5))
        pygame.draw.rect(screen, YELLOW, (self.x - 30, self.y - self.radius - 25, 60 * (self.energy / 100), 5))

    def move(self, keys):
        if keys[self.controls['up']] and self.y - self.radius > 0:
            self.y -= self.speed
        if keys[self.controls['down']] and self.y + self.radius < HEIGHT:
            self.y += self.speed
        if keys[self.controls['left']] and self.x - self.radius > 0:
            self.x -= self.speed
        if keys[self.controls['right']] and self.x + self.radius < WIDTH:
            self.x += self.speed

    def shoot(self):
        # Shoot projectiles in the direction the player is facing (angle)
        if len(self.projectiles) < 10:  # Limit the number of projectiles
            angle = random.uniform(-math.pi/4, math.pi/4)  # Shoots randomly in a direction
            speed = 10  # Projectile speed
            projectile = Projectile(self.x, self.y, angle, speed, self.color)
            self.projectiles.append(projectile)

    def update_projectiles(self):
        # Update the position of all projectiles
        for projectile in self.projectiles[:]:
            projectile.move()
            if projectile.x < 0 or projectile.x > WIDTH or projectile.y < 0 or projectile.y > HEIGHT:
                self.projectiles.remove(projectile)  # Remove projectiles that go off-screen

# Create a collectible bubble
class CollectibleBubble:
    def __init__(self, x, y, radius, color, ability):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.ability = ability  # Ability that this bubble grants

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Detect collision
def is_collision(bubble1, bubble2):
    distance = math.sqrt((bubble1.x - bubble2.x) ** 2 + (bubble1.y - bubble2.y) ** 2)
    return distance < bubble1.radius + bubble2.radius

# Detect projectile collision
def is_projectile_collision(projectile, bubble):
    distance = math.sqrt((projectile.x - bubble.x) ** 2 + (projectile.y - bubble.y) ** 2)
    return distance < projectile.radius + bubble.radius

# Display winner message
def display_winner(winner):
    font = pygame.font.SysFont("Arial", 50)
    text = font.render(f"{winner} Wins!", True, (0, 255, 0))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Show the winner for 2 seconds

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

    # List of abilities that both players will share
    abilities = ['fireball', 'shockwave', 'speedboost']

    collectible_bubbles = []

    # Spawn collectible bubbles with the same abilities for both players
    for _ in range(5):  # Create 5 collectible bubbles
        ability = random.choice(abilities)
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        color = random.choice([BLUE, GREEN, PURPLE])
        collectible_bubbles.append(CollectibleBubble(x, y, 15, color, ability))

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

        # Shoot projectiles
        if keys[pygame.K_SPACE]:
            player1.shoot()
        if keys[pygame.K_RETURN]:
            player2.shoot()

        # Update and draw projectiles
        player1.update_projectiles()
        player2.update_projectiles()

        # Check for collisions with collectible bubbles
        for bubble in collectible_bubbles[:]:
            if is_collision(player1, bubble):
                player1.abilities.append(bubble.ability)
                print(f"Player 1 unlocked {bubble.ability}!")
                collectible_bubbles.remove(bubble)  # Remove the bubble after collection

            if is_collision(player2, bubble):
                player2.abilities.append(bubble.ability)
                print(f"Player 2 unlocked {bubble.ability}!")
                collectible_bubbles.remove(bubble)  # Remove the bubble after collection

        # Draw the collectible bubbles
        for bubble in collectible_bubbles:
            bubble.draw(screen)

        # Draw projectiles
        for projectile in player1.projectiles:
            projectile.draw(screen)

        for projectile in player2.projectiles:
            projectile.draw(screen)

        # Check for projectile collisions
        for projectile in player1.projectiles:
            if is_projectile_collision(projectile, player2):
                print("Player 2 hit by Player 1's projectile!")
                player2.health -= 10  # Player 2 takes damage

        for projectile in player2.projectiles:
            if is_projectile_collision(projectile, player1):
                print("Player 1 hit by Player 2's projectile!")
                player1.health -= 10  # Player 1 takes damage

        # Draw players
        player1.draw(screen)
        player2.draw(screen)

        # Check if someone wins
        if player1.health <= 0:
            display_winner("Player 2")
            break  # Exit the game loop
        elif player2.health <= 0:
            display_winner("Player 1")
            break  # Exit the game loop

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
