import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Endless Runner")

# Player properties
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]
player_speed = 10

# Obstacle properties
obstacle_size = 50
obstacle_pos = [random.randint(0, SCREEN_WIDTH - obstacle_size), 0]
obstacle_speed = 10

# Game variables
clock = pygame.time.Clock()
game_over = False
score = 0

# Font
font = pygame.font.SysFont("monospace", 35)

# Function to detect collision
def detect_collision(player_pos, obstacle_pos):
    px, py = player_pos
    ox, oy = obstacle_pos

    if (ox >= px and ox < (px + player_size)) or (px >= ox and px < (ox + obstacle_size)):
        if (oy >= py and oy < (py + player_size)) or (py >= oy and py < (oy + obstacle_size)):
            return True
    return False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x -= player_speed
            elif event.key == pygame.K_RIGHT:
                x += player_speed
            player_pos[0] = x

    screen.fill(BLACK)

    # Update obstacle position
    if obstacle_pos[1] >= 0 and obstacle_pos[1] < SCREEN_HEIGHT:
        obstacle_pos[1] += obstacle_speed
    else:
        obstacle_pos[1] = 0
        obstacle_pos[0] = random.randint(0, SCREEN_WIDTH - obstacle_size)
        score += 1

    if detect_collision(player_pos, obstacle_pos):
        game_over = True

    # Draw player
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))

    # Draw obstacle
    pygame.draw.rect(screen, RED, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))

    # Display score
    text = font.render("Score: {}".format(score), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

    clock.tick(30)

pygame.quit()
