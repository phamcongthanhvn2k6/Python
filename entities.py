# entities.py
import pygame
import os
from config import *
from utils import resource_path

# Biến toàn cục lưu trữ ảnh đã load để tránh load lại nhiều lần (Performance optimization)
game_images = {}


def load_images():
    """Load ảnh từ folder assets. Nếu không có ảnh thì tạo Surface màu làm placeholder."""
    img_mapping = {
        "player": ("player.png", GREEN, (50, 40)),  # Tên file, Màu fallback, Kích thước fallback
        "enemy": ("enemy.png", RED, (50, 40)),
        "bullet": ("bullet.png", YELLOW, (10, 20))
    }

    for key, (filename, color, size) in img_mapping.items():
        path = resource_path(os.path.join("assets", filename))

        if os.path.exists(path):
            try:
                img = pygame.image.load(path).convert_alpha()
                # Tùy chọn: Scale ảnh nếu cần thiết
                # img = pygame.transform.scale(img, size)
                game_images[key] = img
            except pygame.error:
                # Nếu file tồn tại nhưng lỗi format
                surf = pygame.Surface(size)
                surf.fill(color)
                game_images[key] = surf
        else:
            # Nếu file không tồn tại
            surf = pygame.Surface(size)
            surf.fill(color)
            game_images[key] = surf


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game_images["player"]
        self.rect = self.image.get_rect()
        # Vị trí ban đầu: Giữa, dưới cùng
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.last_shot_time = 0
        self.hp = 100  # Máu (để mở rộng sau này)

    def update(self):
        # Xử lý input bàn phím
        keys = pygame.key.get_pressed()

        # Di chuyển Trái/Phải
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED

        # Di chuyển Lên/Xuống
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += PLAYER_SPEED

    def shoot(self, current_time, all_sprites, bullets_group):
        """Bắn đạn nếu đã qua thời gian delay"""
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
        # Xóa địch nếu đi quá màn hình để giải phóng bộ nhớ
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
        # Xóa đạn nếu bay khỏi màn hình
        if self.rect.bottom < 0:
            self.kill()