import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Frog")

# Colors
WHITE = (255, 255, 255)

# Load frog image
try:
    frog_img = pygame.image.load("frog.png").convert_alpha()
except pygame.error as e:
    print(f"Unable to load image: frog.png")
    pygame.quit()
    sys.exit()

# Scale the image
frog_width = 100
frog_height = int(frog_img.get_height() * (frog_width / frog_img.get_width()))
frog_img = pygame.transform.scale(frog_img, (frog_width, frog_height))

frog_rect = frog_img.get_rect()
frog_rect.x = (WIDTH - frog_width) // 2
frog_rect.y = HEIGHT - frog_height - 10


# Frog properties
frog_y_velocity = 0
jump_strength = -20
gravity = 1

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Jump
                if frog_rect.y == HEIGHT - frog_height - 10: # Allow jumping only from the ground
                    frog_y_velocity = jump_strength

    # Apply gravity
    frog_y_velocity += gravity
    frog_rect.y += frog_y_velocity

    # Keep frog on the ground
    if frog_rect.y >= HEIGHT - frog_height - 10:
        frog_rect.y = HEIGHT - frog_height - 10
        frog_y_velocity = 0

    # Drawing
    screen.fill(WHITE)
    screen.blit(frog_img, frog_rect)
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
