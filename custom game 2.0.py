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
BROWN = (139, 69, 19)  # Wall color
ORANGE = (255, 165, 0)  # Heat Source Color
CYAN = (0, 255, 255)  # Wind Current Color

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Escape Game")

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

    def move(self, keys, obstacles, wind_currents):
        if keys[self.controls['up']] and not self.collides_with_walls(0, -self.speed, obstacles):
            self.y -= self.speed
        if keys[self.controls['down']] and not self.collides_with_walls(0, self.speed, obstacles):
            self.y += self.speed
        if keys[self.controls['left']] and not self.collides_with_walls(-self.speed, 0, obstacles):
            self.x -= self.speed
        if keys[self.controls['right']] and not self.collides_with_walls(self.speed, 0, obstacles):
            self.x += self.speed

        # Apply wind currents
        self.apply_wind(wind_currents)

    def collides_with_walls(self, dx, dy, obstacles):
        for wall in obstacles:
            if (self.x + dx - wall[0] < self.radius and self.x + dx + self.radius > wall[0] and
                self.y + dy - wall[1] < self.radius and self.y + dy + self.radius > wall[1]):
                return True
        return False

    def apply_wind(self, wind_currents):
        for current in wind_currents:
            if (self.x > current[0] and self.x < current[0] + current[2] and
                self.y > current[1] and self.y < current[1] + current[3]):
                self.x += current[4]  # Wind pushes the bubble horizontally
                self.y += current[5]  # Wind pushes the bubble vertically

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

# Hazard Class (Sharp Objects, Heat Sources)
class Hazard:
    def __init__(self, x, y, width, height, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type  # Sharp or Heat

    def draw(self, screen):
        if self.type == "sharp":
            pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        elif self.type == "heat":
            pygame.draw.rect(screen, ORANGE, (self.x, self.y, self.width, self.height))

    def damage(self, bubble):
        if self.type == "sharp" and (bubble.x > self.x and bubble.x < self.x + self.width and
                                     bubble.y > self.y and bubble.y < self.y + self.height):
            bubble.health -= 10  # Sharp object damage
        elif self.type == "heat" and (bubble.x > self.x and bubble.x < self.x + self.width and
                                      bubble.y > self.y and bubble.y < self.y + self.height):
            bubble.health -= 5  # Heat damage

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

# Collision detection function
def is_collision(bubble, collectible):
    # Calculate the distance between the bubble and the collectible
    distance = math.sqrt((bubble.x - collectible.x) ** 2 + (bubble.y - collectible.y) ** 2)
    return distance < bubble.radius + collectible.radius

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

    collectible_bubbles = []
    abilities = ['fireball', 'shockwave', 'speedboost']

    # Spawn collectible bubbles with the same abilities for both players
    for _ in range(5):  # Create 5 collectible bubbles
        ability = random.choice(abilities)
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        color = random.choice([BLUE, GREEN, PURPLE])
        collectible_bubbles.append(CollectibleBubble(x, y, 15, color, ability))

    # Obstacles: Define a list of walls as (x, y, width, height)
    obstacles = [
        (200, 150, 100, 20),  # Wall 1
        (400, 300, 100, 20),  # Wall 2
        (600, 450, 100, 20)   # Wall 3
    ]

    # Hazards: Define sharp objects and heat sources
    hazards = [
        Hazard(100, 100, 50, 50, "sharp"),
        Hazard(500, 200, 50, 50, "heat")
    ]

    # Wind currents: Define wind areas (x, y, width, height, horizontal force, vertical force)
    wind_currents = [
        (300, 100, 200, 50, 2, 0),  # Wind pushing to the right
        (500, 400, 150, 50, 0, -2)  # Wind pushing up
    ]

    while running:
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()

        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move players
        player1.move(keys, obstacles, wind_currents)
        player2.move(keys, obstacles, wind_currents)

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
                collectible_bubbles.remove(bubble)  # Remove the bubble after collection

            if is_collision(player2, bubble):
                player2.abilities.append(bubble.ability)
                collectible_bubbles.remove(bubble)  # Remove the bubble after collection

        # Draw hazards and check for damage
        for hazard in hazards:
            hazard.draw(screen)
            hazard.damage(player1)
            hazard.damage(player2)

        # Draw the collectible bubbles
        for bubble in collectible_bubbles:
            bubble.draw(screen)

        # Draw players
        player1.draw(screen)
        player2.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()

