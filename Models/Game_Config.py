import pygame
import random
import sys
from pygame.locals import *
from GUI.player_gui import Player
from GUI.obstacle_gui import Obstacle
from Models.Score_manager import ScoreManager
from Models.Utils.game_over import draw_game_over, reset_game

def run_game(difficulty):
    # Definir constantes dentro de la función
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCORE_UPDATE_INTERVAL = 1000  # Intervalo de actualización de la puntuación en milisegundos

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

    # Inicializar el administrador de puntuación
    score_manager = ScoreManager()

    # Bucle principal del juego
    running = True
    game_over = False
    last_score_update_time = pygame.time.get_ticks()  # Tiempo de la última actualización de la puntuación
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    game_over = False
                    reset_game(player, all_sprites, obstacle_group, score_manager)
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        if not game_over:
            # Generar un nuevo obstáculo cada cierto intervalo de tiempo, dependiendo de la dificultad
            if random.randrange(100) < difficulty:
                new_obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT)
                all_sprites.add(new_obstacle)
                obstacle_group.add(new_obstacle)

            # Verificar colisiones entre el jugador y los obstáculos
            if pygame.sprite.spritecollide(player, obstacle_group, False):
                game_over = True  # Cambiar estado del juego a "Game Over"
            else:
                # Comprobar si es momento de actualizar la puntuación
                current_time = pygame.time.get_ticks()
                if current_time - last_score_update_time >= SCORE_UPDATE_INTERVAL:
                    score_manager.increment_score(1)  # Aumentar la puntuación en 1 punto
                    last_score_update_time = current_time  # Actualizar el tiempo de la última actualización de la puntuación

            # Actualizar la posición y el dibujo de los sprites
            all_sprites.update()

            # Dibujar los sprites en la pantalla
            screen.fill((255, 255, 255))
            all_sprites.draw(screen)

            # Mostrar puntaje en pantalla
            score_text = score_manager.get_score_text()
            screen.blit(score_text, (10, 10))
        else:
            # Mostrar ventana de Game Over
            draw_game_over(screen)

        pygame.display.flip()
        clock.tick(30)
