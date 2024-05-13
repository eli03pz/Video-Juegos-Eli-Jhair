import pygame

class ScoreManager:
    def __init__(self):
        self.score = 0

    def increment_score(self, increment):
        self.score += increment

    def reset_score(self):
        self.score = 0

    def get_score_text(self):
        font = pygame.font.Font(None, 24)
        text_surface = font.render(f"Score: {self.score}", True, (0, 0, 0))
        return text_surface
