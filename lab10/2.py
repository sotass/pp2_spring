import pygame
import psycopg2
import json
import sys
from random import randint

DB_NAME = "snake_db"
DB_USER = "postgres"
DB_PASSWORD = "sotasakurai12859"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS "user" (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES "user"(id),
            score INTEGER,
            level INTEGER,
            saved_state TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_or_create_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM "user" WHERE username = %s', (username,))
    result = cursor.fetchone()
    if result:
        user_id = result[0]
    else:
        cursor.execute('INSERT INTO "user" (username) VALUES (%s) RETURNING id', (username,))
        user_id = cursor.fetchone()[0]
        conn.commit()
    conn.close()
    return user_id

def get_user_score(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result if result else (0, 1)

def save_game_state(user_id, score, level, snake, direction, food):
    state = {
        'snake': snake,
        'direction': direction,
        'food': food
    }
    state_json = json.dumps(state)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_score (user_id, score, level, saved_state)
        VALUES (%s, %s, %s, %s)
    """, (user_id, score, level, state_json))
    conn.commit()
    conn.close()

create_tables()

username = input("Введите имя пользователя: ")
user_id = get_or_create_user(username)
score, level = get_user_score(user_id)

pygame.init()
CELL_SIZE = 20
WIDTH, HEIGHT = 640, 480
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

base_fps = 10
FPS = base_fps + level * 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

snake = [(CELL_SIZE * 5, CELL_SIZE * 5)]
direction = (CELL_SIZE, 0)
food = None

paused = False
running = True

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def draw_walls():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.rect(screen, BLUE, (x, 0, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, BLUE, (x, HEIGHT - CELL_SIZE, CELL_SIZE, CELL_SIZE))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.rect(screen, BLUE, (0, y, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, BLUE, (WIDTH - CELL_SIZE, y, CELL_SIZE, CELL_SIZE))

def draw_score():
    font = pygame.font.SysFont("Arial", 28, bold=True)
    text = font.render(f"СЧЁТ: {score}    УРОВЕНЬ: {level}", True, WHITE)
    screen.blit(text, (10, 10))

def move_snake():
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    snake.insert(0, new_head)
    if new_head == food:
        return True
    else:
        snake.pop()
        return False

def check_collision():
    head = snake[0]
    if (
        head in snake[1:] or
        head[0] < CELL_SIZE or head[0] >= WIDTH - CELL_SIZE or
        head[1] < CELL_SIZE or head[1] >= HEIGHT - CELL_SIZE
    ):
        return True
    return False

def update_level():
    global level, FPS
    level = score // 50 + 1
    FPS = base_fps + level * 2

def spawn_food():
    while True:
        f = (randint(1, COLS - 2) * CELL_SIZE, randint(1, ROWS - 2) * CELL_SIZE)
        if f not in snake:
            return f

food = spawn_food()

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game_state(user_id, score, level, snake, direction, food)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
            elif event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_s:
                save_game_state(user_id, score, level, snake, direction, food)

    if not paused:
        if move_snake():
            score += 10
            update_level()
            food = spawn_food()

        if check_collision():
            save_game_state(user_id, score, level, snake, direction, food)
            pygame.time.wait(2000)
            running = False

    draw_walls()
    draw_snake()
    draw_food()
    draw_score()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()