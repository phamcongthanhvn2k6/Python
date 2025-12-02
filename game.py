# game.py
import pygame
import random
from config import *
from menu import Menu
from entities import Player, Enemy, load_images


class Game:
    def __init__(self):
        # 1. Khởi tạo Pygame
        pygame.init()
        pygame.mixer.init()  # Chuẩn bị cho âm thanh

        # 2. Tạo cửa sổ game
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

        # 3. Load tài nguyên và Menu
        load_images()
        self.menu = Menu(self.screen)

        self.running = True

    def new_game(self):
        """Reset lại toàn bộ thông số để bắt đầu màn chơi mới"""
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.score = 0
        self.lives = 3
        self.last_enemy_spawn = pygame.time.get_ticks()

        # Bắt đầu vòng lặp chơi game
        self.run()

    def run(self):
        """Game Loop: Events -> Update -> Draw"""
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)  # Giữ game chạy ở FPS ổn định
            self.events()
            self.update()
            self.draw()

    def events(self):
        """Xử lý sự kiện đầu vào (bàn phím, chuột)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                # Bắn đạn
                if event.key == pygame.K_SPACE:
                    self.player.shoot(pygame.time.get_ticks(), self.all_sprites, self.bullets)
                # Tạm dừng
                if event.key == pygame.K_ESCAPE:
                    action = self.menu.show_pause_screen()
                    if action == "quit":
                        self.playing = False
                        self.running = False

    def update(self):
        """Cập nhật logic game"""
        self.all_sprites.update()

        # 1. Sinh kẻ địch
        now = pygame.time.get_ticks()
        if now - self.last_enemy_spawn > ENEMY_SPAWN_INTERVAL:
            self.last_enemy_spawn = now
            # Random vị trí X ngẫu nhiên
            x = random.randrange(0, SCREEN_WIDTH - 50)
            enemy = Enemy(x, -50)  # Sinh ra ở trên cùng màn hình
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

        # 2. Va chạm: Đạn trúng Địch
        # groupcollide(group1, group2, dokill1, dokill2)
        # dokill=True nghĩa là xóa sprite khỏi group khi va chạm
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        for hit in hits:
            self.score += 10
            # (Tại đây có thể thêm code nổ hoặc âm thanh)

        # 3. Va chạm: Địch trúng Player
        hits = pygame.sprite.spritecollide(self.player, self.enemies, True)
        for hit in hits:
            self.lives -= 1
            if self.lives <= 0:
                self.playing = False  # Game Over

    def draw(self):
        """Vẽ mọi thứ lên màn hình"""
        self.screen.fill(BLACK)  # Xóa màn hình cũ

        self.all_sprites.draw(self.screen)  # Vẽ tất cả sprite

        # Vẽ HUD (Điểm và Mạng)
        self.menu.draw_text(f"Score: {self.score}", self.menu.font_ui, WHITE, 10, 10, center=False)
        self.menu.draw_text(f"Lives: {self.lives}", self.menu.font_ui, RED, SCREEN_WIDTH - 100, 10, center=False)

        pygame.display.flip()  # Lật buffer hiển thị (quan trọng)

    def main_loop(self):
        """Vòng lặp điều hướng cấp cao nhất"""
        while self.running:
            # 1. Hiện Start Screen
            action = self.menu.show_start_screen()

            if action == "quit":
                self.running = False
            elif action == "play":
                # 2. Vào Game chính
                self.new_game()

                # 3. Khi chết -> Hiện Game Over
                if self.running:  # Kiểm tra lại phòng khi user tắt đột ngột
                    action = self.menu.show_game_over(self.score)
                    if action == "quit":
                        self.running = False

        pygame.quit()