import pygame
import sys
import random
from pygame.locals import *
from Models.Player import Player
from Models.Obstacle import Obstacle

# Definir constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Esquiva y avanza")
clock = pygame.time.Clock()

# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()

# Crear jugador
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites.add(player)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generar un nuevo obstáculo cada cierto intervalo de tiempo
    if random.randrange(100) < 2:
        new_obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT)
        all_sprites.add(new_obstacle)
        obstacle_group.add(new_obstacle)

    # Verificar colisiones entre el jugador y los obstáculos
    if pygame.sprite.spritecollide(player, obstacle_group, False):
        running = False  # Otra lógica de juego, como perder o restar vidas

    # Actualizar la posición y el dibujo de los sprites
    all_sprites.update()

    # Dibujar los sprites en la pantalla
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
