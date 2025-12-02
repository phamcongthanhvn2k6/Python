# config.py
import os

# --- Cấu hình Màn hình ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
CAPTION = "Space Shooter - Student Project"

# --- Màu sắc (RGB) ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

# --- Gameplay settings ---
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 3

# Thời gian (milliseconds)
PLAYER_SHOOT_DELAY = 250
ENEMY_SPAWN_INTERVAL = 1000  # Cứ 1 giây ra 1 địch

# --- File paths ---
SCORE_FILE = "scores.txt"