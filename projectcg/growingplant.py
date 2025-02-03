import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 60
icon = pygame.image.load('pine.png')
pygame.display.set_icon(icon)

# Load Images
seed_img = pygame.image.load("seed.png")
growing_plant_img1 = pygame.image.load("growing_plant1.png")
growing_plant_img2 = pygame.image.load("growing_plant2.png")
growing_plant_img3 = pygame.image.load("growing_plant3.png")
fully_grown_plant_img = pygame.image.load("grown.png")
water_img = pygame.image.load("water.png")
nutrient_img = pygame.image.load("nutrient.png")
background_img = pygame.image.load("background.png")
rock_img = pygame.image.load("rocks.png")
drought_img = pygame.image.load("drought.png")

# Resize Images
seed_img = pygame.transform.scale(seed_img, (40, 40))
growing_plant_img1 = pygame.transform.scale(growing_plant_img1, (40, 40))
growing_plant_img2 = pygame.transform.scale(growing_plant_img2, (45, 45))
growing_plant_img3 = pygame.transform.scale(growing_plant_img3, (50, 50))
fully_grown_plant_img = pygame.transform.scale(fully_grown_plant_img, (50, 50))
water_img = pygame.transform.scale(water_img, (30, 30))
nutrient_img = pygame.transform.scale(nutrient_img, (30, 30))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
rock_img = pygame.transform.scale(rock_img, (40, 40))
drought_img = pygame.transform.scale(drought_img, (50, 30))

# Game Elements
seed = pygame.Rect(WIDTH // 2, HEIGHT - 100, 40, 40)
resources = []  # Water and nutrients
obstacles = []  # Rocks and drought

# Game Variables
score = 20
speed = 5
obstacle_speed = 3
win_threshold = 100  # Winning score threshold

# Screen Setup
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("growing plant game")
clock = pygame.time.Clock()

def spawn_resources():
    """Spawns water or nutrients at a random position"""
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 200)
    type_ = random.choice(['water', 'nutrient'])
    resources.append({'rect': pygame.Rect(x, y, 20, 20), 'type': type_})

def spawn_obstacles():
    """Spawns either rocks or drought patches at the top of the screen and moves downward"""
    x = random.randint(50, WIDTH - 50)
    y = 0  # Start from the top
    obstacle_type = random.choice(['rock', 'drought'])
    obstacle_rect = pygame.Rect(x, y, 40, 40) if obstacle_type == 'rock' else pygame.Rect(x, y, 50, 30)
    obstacles.append({'rect': obstacle_rect, 'type': obstacle_type})

# Spawn Initial Resources and Obstacles
for _ in range(5):
    spawn_resources()
    spawn_obstacles()

# Main Loop
running = True
while running:
    clock.tick(FPS)
    game_screen.blit(background_img, (0, 0))
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and seed.x > 0:
        seed.x -= speed
    if keys[pygame.K_RIGHT] and seed.x < WIDTH - seed.width:
        seed.x += speed
    if keys[pygame.K_UP] and seed.y > 0:
        seed.y -= speed
    if keys[pygame.K_DOWN] and seed.y < HEIGHT - seed.height:
        seed.y += speed
    
    # Resource Collection
    for resource in resources[:]:
        if seed.colliderect(resource['rect']):
            score += 5 if resource['type'] == 'nutrient' else 3
            resources.remove(resource)
            spawn_resources()
    
    # Move Obstacles
    for obstacle in obstacles[:]:
        obstacle['rect'].y += obstacle_speed
        if obstacle['rect'].y > HEIGHT:
            obstacles.remove(obstacle)
            spawn_obstacles()
    
    # Obstacle Collision
    for obstacle in obstacles[:]:
        if seed.colliderect(obstacle['rect']):
            if obstacle['type'] == 'rock':
                score -= 10  # Penalty for hitting rocks
            elif obstacle['type'] == 'drought':
                speed = max(2, speed - 1)  # Slows player down
            obstacles.remove(obstacle)
            spawn_obstacles()
    
    # Game Over Condition
    if score <= 0:
        font = pygame.font.Font(None, 50)
        game_over_text = font.render("Game Over!!!", True, "RED")
        game_screen.blit(game_over_text, ( 250, 250))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
    
    # Winning Condition
    if score >= win_threshold:
        font = pygame.font.Font(None, 50)
        win_text = font.render("You have won! Your plant has fully grown!", True, "BLACK")
        game_screen.blit(win_text, ( 70, 250))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False
    
    # Set Plant Growth Stage
    if score >= 81:
        current_seed_img = fully_grown_plant_img
    elif score >= 61:
        current_seed_img = growing_plant_img3
    elif score >= 41:
        current_seed_img = growing_plant_img2
    elif score >= 21:
        current_seed_img = growing_plant_img1
    else:
        current_seed_img = seed_img
    
    # Draw Elements
    game_screen.blit(current_seed_img, (seed.x, seed.y))
    for resource in resources:
        img = nutrient_img if resource['type'] == 'nutrient' else water_img
        game_screen.blit(img, (resource['rect'].x, resource['rect'].y))
    for obstacle in obstacles:
        img = rock_img if obstacle['type'] == 'rock' else drought_img
        game_screen.blit(img, (obstacle['rect'].x, obstacle['rect'].y))
    
    # Display Score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    game_screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

pygame.quit()
