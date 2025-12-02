# visuals.py
import pygame
import random
from config import *


class Star:
    """Lớp đại diện cho một ngôi sao trong background"""

    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.speed = random.uniform(0.5, 3.0)  # Tốc độ ngẫu nhiên tạo độ sâu
        self.size = random.randint(1, 3)
        # Màu trắng hoặc hơi xanh/vàng nhẹ
        self.color = random.choice([WHITE, (200, 200, 255), (255, 255, 200)])

    def update(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = 0
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)


class StarField:
    """Quản lý toàn bộ bầu trời sao"""

    def __init__(self, count=100):
        self.stars = [Star() for _ in range(count)]

    def update(self):
        for star in self.stars:
            star.update()

    def draw(self, surface):
        for star in self.stars:
            star.draw(surface)


class Explosion(pygame.sprite.Sprite):
    """Hiệu ứng nổ hạt (Particle System)"""

    def __init__(self, center, color):
        super().__init__()
        self.size = random.randint(4, 10)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Vật lý của hạt nổ
        self.vel_x = random.uniform(-5, 5)
        self.vel_y = random.uniform(-5, 5)
        self.life = 255  # Độ trong suốt (Alpha) bắt đầu từ 255

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.life -= 10  # Giảm dần độ đậm

        if self.life <= 0:
            self.kill()
        else:
            self.image.set_alpha(self.life)  # Cập nhật độ mờ