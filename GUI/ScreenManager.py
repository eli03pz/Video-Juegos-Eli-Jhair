import pygame
import sys

# Definir constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Esquiva y avanza")

# Cargar la imagen de fondo
try:
    background = pygame.image.load("assets/fondojuego.jpg") 
except pygame.error as e:
    print(f"Error al cargar la imagen de fondo: {e}")
    sys.exit()

clock = pygame.time.Clock()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar la imagen de fondo
    screen.blit(background, (0, 0))

    pygame.display.flip()
    clock.tick(60)
