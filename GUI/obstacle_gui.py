import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        # Cargar la imagen del obstáculo y redimensionarla
        self.image = pygame.image.load("assets/aguilapreciosa.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))  # Redimensionar al tamaño deseado
        self.rect = self.image.get_rect()
        self.rect.x = screen_width  # Aparece al lado derecho de la pantalla
        self.rect.y = random.randint(0, screen_height - self.rect.height)  # Posición aleatoria en altura
        self.speed = 5  # Velocidad de movimiento del obstáculo

    def update(self):
        # Método para actualizar la posición del obstáculo en cada frame
        self.rect.x -= self.speed
