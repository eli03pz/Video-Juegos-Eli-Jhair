import pygame
import sys
import random
from pygame.locals import *

# Definir constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Esquiva y avanza")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Placeholder image
        self.image.fill((255, 0, 0))  # Placeholder color (red)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 5  # Velocidad de movimiento del jugador

    def update(self):
        # Método para actualizar la posición del jugador en cada frame
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_DOWN]:
            self.move_down()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()

    def move_up(self):
        # Método para mover el jugador hacia arriba
        self.rect.y -= self.speed

    def move_down(self):
        # Método para mover el jugador hacia abajo
        self.rect.y += self.speed

    def move_left(self):
        # Método para mover el jugador hacia la izquierda
        self.rect.x -= self.speed

    def move_right(self):
        # Método para mover el jugador hacia la derecha
        self.rect.x += self.speed

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((30, 30))  # Placeholder image
        self.image.fill((0, 0, 255))  # Placeholder color (blue)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width  # Aparece al lado derecho de la pantalla
        self.rect.y = random.randint(0, screen_height - self.rect.height)  # Posición aleatoria en altura
        self.speed = 5  # Velocidad de movimiento del obstáculo

    def update(self):
        # Método para actualizar la posición del obstáculo en cada frame
        self.rect.x -= self.speed

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
