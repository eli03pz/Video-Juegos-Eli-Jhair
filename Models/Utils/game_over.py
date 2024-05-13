import pygame

def draw_game_over_screen(screen):
    screen.fill((255, 255, 255))  # Llenar la pantalla de blanco

    # Definir constantes de posición y tamaño de la ventana de Game Over
    game_over_width = 400
    game_over_height = 200
    game_over_x = (screen.get_width() - game_over_width) // 2
    game_over_y = (screen.get_height() - game_over_height) // 2

    # Dibujar el rectángulo de la ventana de Game Over
    pygame.draw.rect(screen, (200, 200, 200), (game_over_x, game_over_y, game_over_width, game_over_height))

    # Dibujar el texto de "Game Over"
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text, (game_over_x + (game_over_width - game_over_text.get_width()) // 2, game_over_y + 20))

    # Dibujar el texto de instrucciones
    font = pygame.font.Font(None, 24)
    prompt_text = font.render("Presiona 'R' para jugar de nuevo o 'Q' para salir", True, (0, 0, 0))
    screen.blit(prompt_text, (game_over_x + (game_over_width - prompt_text.get_width()) // 2, game_over_y + 100))

    pygame.display.flip()  # Actualizar la pantalla

def handle_game_over_input():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 'restart'
                elif event.key == pygame.K_q:
                    return 'quit'

def reset_game(player, all_sprites, obstacle_group, score_manager, SCREEN_WIDTH, SCREEN_HEIGHT):
    player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    all_sprites.empty()
    obstacle_group.empty()
    all_sprites.add(player)
    score_manager.reset_score()


def show_game_over_screen(screen):
    draw_game_over_screen(screen)
    return handle_game_over_input()