import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Car settings
CAR_WIDTH = 60
CAR_HEIGHT = 30

# Terrain settings
TERRAIN_HEIGHT = 100
HILL_FREQUENCY = 100

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hill Climb Racing")

# Load car image (you need to have a car.png image in the same directory)
car_image = pygame.image.load("car.png")
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

# Car properties
car_x = 100
car_y = SCREEN_HEIGHT - TERRAIN_HEIGHT - CAR_HEIGHT
car_speed = 0
car_acceleration = 0.2
car_deceleration = 0.1
max_speed = 5

# Function to draw the terrain
def draw_terrain():
    for x in range(0, SCREEN_WIDTH, 1):
        y = SCREEN_HEIGHT - (TERRAIN_HEIGHT + math.sin(x / HILL_FREQUENCY) * 50)
        pygame.draw.line(screen, BLACK, (x, SCREEN_HEIGHT), (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_speed -= car_acceleration
    if keys[pygame.K_RIGHT]:
        car_speed += car_acceleration

    car_speed = max(-max_speed, min(max_speed, car_speed))

    car_x += car_speed
    if car_speed > 0:
        car_speed -= car_deceleration
    elif car_speed < 0:
        car_speed += car_deceleration

    # Update car position based on the terrain
    car_y = SCREEN_HEIGHT - (TERRAIN_HEIGHT + math.sin(car_x / HILL_FREQUENCY) * 50 + CAR_HEIGHT)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the terrain
    draw_terrain()

    # Draw the car
    screen.blit(car_image, (car_x, car_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
