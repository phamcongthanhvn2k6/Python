# menu.py
import pygame
import os
from config import *


class Menu:
    def __init__(self, screen):
        self.screen = screen
        # Khởi tạo font chữ mặc định của hệ thống
        self.font_title = pygame.font.SysFont("Arial", 48, bold=True)
        self.font_text = pygame.font.SysFont("Arial", 24)
        self.font_ui = pygame.font.SysFont("Consolas", 20)

    def draw_text(self, text, font, color, x, y, center=True):
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        if center:
            rect.center = (x, y)
        else:
            rect.topleft = (x, y)
        self.screen.blit(surface, rect)

    def get_high_score(self):
        if not os.path.exists(SCORE_FILE):
            return 0
        try:
            with open(SCORE_FILE, "r") as f:
                content = f.read().strip()
                return int(content) if content else 0
        except ValueError:
            return 0

    def save_high_score(self, current_score):
        high_score = self.get_high_score()
        if current_score > high_score:
            with open(SCORE_FILE, "w") as f:
                f.write(str(current_score))
            return True  # Có kỷ lục mới
        return False

    def show_start_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("SPACE SHOOTER", self.font_title, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        self.draw_text("Press SPACE to Start", self.font_text, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.draw_text("Press ESC to Quit", self.font_text, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)

        high_score = self.get_high_score()
        self.draw_text(f"High Score: {high_score}", self.font_text, YELLOW, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

        pygame.display.flip()
        return self._wait_for_key()

    def show_game_over(self, score):
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", self.font_title, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        self.draw_text(f"Your Score: {score}", self.font_text, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        is_new_record = self.save_high_score(score)
        if is_new_record:
            self.draw_text("NEW HIGH SCORE!", self.font_text, YELLOW, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

        self.draw_text("Press SPACE to Restart", self.font_text, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
        self.draw_text("Press ESC to Quit", self.font_text, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)

        pygame.display.flip()
        return self._wait_for_key()

    def show_pause_screen(self):
        # Vẽ lớp phủ mờ (semi-transparent)
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        self.draw_text("PAUSED", self.font_title, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.draw_text("Press ESC to Resume", self.font_text, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        pygame.display.flip()

        # Loop riêng cho pause
        waiting = True
        while waiting:
            self.screen.fill(BLACK)  # Vẽ lại để tránh bị chồng hình
            self.draw_text("PAUSED", self.font_title, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "resume"

    def _wait_for_key(self):
        """Hàm phụ trợ để đợi người dùng bấm phím"""
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return "play"
                    if event.key == pygame.K_ESCAPE:
                        return "quit"