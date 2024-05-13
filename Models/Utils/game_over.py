import pygame

def draw_game_over(screen):
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2 - 50))

    font = pygame.font.Font(None, 24)
    prompt_text = font.render("Presiona 'R' para jugar de nuevo o 'Q' para salir", True, (0, 0, 0))
    screen.blit(prompt_text, (screen.get_width() // 2 - prompt_text.get_width() // 2, screen.get_height() // 2 + 20))

def reset_game(player, all_sprites, obstacle_group, score_manager):
    # Definir constantes dentro de la función
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    all_sprites.empty()
    obstacle_group.empty()
    all_sprites.add(player)
    score_manager.reset_score()

