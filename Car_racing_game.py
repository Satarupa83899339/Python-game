import pygame
import random
import sys

# Initialize
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏎️ Car Racing Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (200, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
speed = 5

# Player car
player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 80, 50, 80)

# Enemy cars
enemy = pygame.Rect(random.randint(50, WIDTH-100), -100, 50, 80)

font = pygame.font.SysFont("Arial", 24)
score = 0

def draw_window():
    win.fill(GRAY)

    # Road lines
    for i in range(20, HEIGHT, 40):
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, 20))

    # Draw player and enemy
    pygame.draw.rect(win, BLUE, player)
    pygame.draw.rect(win, RED, enemy)

    # Score
    text = font.render(f"Score: {score}", True, WHITE)
    win.blit(text, (10, 10))

    pygame.display.update()

def game_over():
    text = font.render("GAME OVER!", True, WHITE)
    win.blit(text, (WIDTH//2 - 70, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    draw_window()

    # Move enemy car
    enemy.y += speed
    if enemy.y > HEIGHT:
        enemy.y = -100
        enemy.x = random.randint(50, WIDTH - 100)
        score += 1
        speed += 0.2

    # Check collision
    if player.colliderect(enemy):
        game_over()

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += 5

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
