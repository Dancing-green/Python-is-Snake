import pygame
import time
import random

# Initialisieren von Pygame
pygame.init()

# Fenstergröße und Titel
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Spielvariablen
snake = [(105, 45), (90, 45), (75, 45)]  # Starten Sie die Schlange mit 3 Blöcken
snake_speed = 15
snake_direction = (1, 0)

# Zeitvariablen
initial_delay = 500
reduction_factor = 30

food = (90, 90)  # Zufälliges Essen
score = 0

# Create a font object to display the score
font = pygame.font.Font(None, 36)

def generate_food():
    x = random.randint(0, (width - 10) // 15) * 15
    y = random.randint(0, (height - 10) // 15) * 15
    return x, y

def check_collision():
    # Überprüfen, ob die Schlange mit sich selbst kollidiert
    head = snake[0]
    if head in snake[1:]:
        return True

    # Überprüfen, ob die Schlange gegen die Wände kollidiert
    if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
        return True

    return False

def check_meal():
    print("Checking if snake is eating..")
    head = snake[0]
    print(f"Snake Head Pos: ", head)
    print(f"Food Pos ", food)
    eaten = head == food
    print(f"Eaten: ", eaten)
    return eaten

def calculate_delay():
    return max(initial_delay - score * reduction_factor, 0)


# Schleife, um das Spiel zu aktualisieren und darzustellen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spiellogik
    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_LEFT] and snake_direction != (1, 0):
            snake_direction = (-1, 0)
        if keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
            snake_direction = (1, 0)
        if keys[pygame.K_UP] and snake_direction != (0, 1):
            snake_direction = (0, -1)
        if keys[pygame.K_DOWN] and snake_direction != (0, -1):
            snake_direction = (0, 1)

    # Aktualisieren der Schlange
    x, y = snake[0]
    x += snake_direction[0] * snake_speed
    y += snake_direction[1] * snake_speed
    snake.insert(0, (x, y))

    # Kollisionserkennung
    if check_collision():
        running = False

    # Essen fressen
    if check_meal():
        food = generate_food()
        score += 1
    else:
        snake.pop()

    # Zeichnen der Schlange und des Essens
    window.fill((0, 0, 0))  # Hintergrund löschen
    for segment in snake:
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(food[0], food[1], 10, 10))

    # Render and display the score
    score_text = font.render("Score: " + str(score), True, green)
    window.blit(score_text, (width - 150, 10))

    pygame.display.update()
    pygame.time.delay(calculate_delay())

# Pygame beenden
pygame.quit()