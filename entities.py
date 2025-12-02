# entities.py
import pygame
import os
from config import *
from utils import resource_path

game_images = {}


def load_images():
    """Load ảnh, nếu không có thì vẽ hình học vector thay thế."""
    img_mapping = {
        "player": ("player.png", GREEN, (50, 40)),
        "enemy": ("enemy.png", RED, (40, 40)),
        "bullet": ("bullet.png", YELLOW, (10, 20))
    }

    for key, (filename, color, size) in img_mapping.items():
        path = resource_path(os.path.join("assets", filename))

        # Tạo surface hỗ trợ trong suốt (Alpha channel)
        img = pygame.Surface(size, pygame.SRCALPHA)

        if os.path.exists(path):
            try:
                loaded_img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.scale(loaded_img, size)
            except pygame.error:
                pass  # Nếu lỗi load ảnh thật thì dùng hình vẽ bên dưới

        # Logic vẽ hình thay thế (Fallback Graphics)
        # Nếu chưa load được ảnh thật vào img, vẽ hình lên img
        if img.get_at((0, 0)) == (0, 0, 0, 0):  # Kiểm tra nếu ảnh vẫn đang trống
            if key == "player":
                # Vẽ tam giác
                points = [(size[0] // 2, 0), (size[0], size[1]), (0, size[1])]
                pygame.draw.polygon(img, color, points)
            elif key == "enemy":
                # Vẽ hình tròn
                pygame.draw.circle(img, color, (size[0] // 2, size[1] // 2), size[0] // 2)
                # Mắt kẻ địch
                pygame.draw.circle(img, BLACK, (size[0] // 2, size[1] // 2), size[0] // 4)
            elif key == "bullet":
                # Vẽ hình oval
                pygame.draw.ellipse(img, color, [0, 0, size[0], size[1]])

        game_images[key] = img


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game_images["player"]
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.last_shot_time = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += PLAYER_SPEED

    def shoot(self, current_time, all_sprites, bullets_group):
        if current_time - self.last_shot_time > PLAYER_SHOOT_DELAY:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets_group.add(bullet)
            self.last_shot_time = current_time


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = game_images["enemy"]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = game_images["bullet"]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()