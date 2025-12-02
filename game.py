# game.py
import pygame
import random
from config import *
from menu import Menu
from entities import Player, Enemy, load_images
from visuals import StarField, Explosion


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

        load_images()
        self.menu = Menu(self.screen)

        # [Visuals] Khởi tạo nền sao
        self.starfield = StarField(count=150)

        self.running = True

    def new_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.score = 0
        self.lives = 3
        self.last_enemy_spawn = pygame.time.get_ticks()

        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot(pygame.time.get_ticks(), self.all_sprites, self.bullets)
                if event.key == pygame.K_ESCAPE:
                    action = self.menu.show_pause_screen()
                    if action == "quit":
                        self.playing = False
                        self.running = False

    def update(self):
        self.all_sprites.update()

        # Cập nhật background sao
        self.starfield.update()

        # Sinh kẻ địch
        now = pygame.time.get_ticks()
        if now - self.last_enemy_spawn > ENEMY_SPAWN_INTERVAL:
            self.last_enemy_spawn = now
            x = random.randrange(0, SCREEN_WIDTH - 50)
            enemy = Enemy(x, -50)
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

        # Va chạm: Đạn trúng Địch
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        for hit in hits:
            self.score += 10

            # [Visuals] Tạo hiệu ứng nổ
            for _ in range(12):  # Sinh ra 12 mảnh vỡ
                particle = Explosion(hit.rect.center, RED)
                self.all_sprites.add(particle)  # Thêm vào group để tự động vẽ & update

        # Va chạm: Địch trúng Player
        hits = pygame.sprite.spritecollide(self.player, self.enemies, True)
        for hit in hits:
            self.lives -= 1
            # Hiệu ứng nổ tại người chơi
            for _ in range(20):
                particle = Explosion(hit.rect.center, GREEN)
                self.all_sprites.add(particle)

            if self.lives <= 0:
                self.playing = False

    def draw(self):
        self.screen.fill(BLACK)

        # [Visuals] Vẽ sao trước (lớp nền)
        self.starfield.draw(self.screen)

        # Vẽ các sprite (Player, Enemy, Bullet, Explosion)
        self.all_sprites.draw(self.screen)

        # Vẽ điểm số
        self.menu.draw_text(f"Score: {self.score}", self.menu.font_ui, WHITE, 10, 10, center=False)
        self.menu.draw_text(f"Lives: {self.lives}", self.menu.font_ui, RED, SCREEN_WIDTH - 100, 10, center=False)

        pygame.display.flip()

    def main_loop(self):
        while self.running:
            action = self.menu.show_start_screen()
            if action == "quit":
                self.running = False
            elif action == "play":
                self.new_game()
                if self.running:
                    action = self.menu.show_game_over(self.score)
                    if action == "quit":
                        self.running = False
        pygame.quit()