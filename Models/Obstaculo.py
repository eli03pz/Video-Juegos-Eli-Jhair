import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))  # Placeholder image
        self.image.fill((0, 0, 255))  # Placeholder color (blue)
        self.rect = self.image.get_rect()
        # Aquí puedes definir la posición inicial y la velocidad del obstáculo

    def update(self):
        # Aquí puedes agregar la lógica de movimiento del obstáculo
        pass
