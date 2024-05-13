import pygame

# Función para el lobby
def lobby(screen):
    # Dibujar texto en la pantalla
    font = pygame.font.Font(None, 36)
    text_easy = font.render("1 - Fácil", True, (0, 0, 0))
    text_medium = font.render("2 - Medio", True, (0, 0, 0))
    text_hard = font.render("3 - Difícil", True, (0, 0, 0))

    # Centrar texto en la pantalla
    text_easy_rect = text_easy.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))
    text_medium_rect = text_medium.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    text_hard_rect = text_hard.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.5))

    screen.fill((255, 255, 255))
    screen.blit(text_easy, text_easy_rect)
    screen.blit(text_medium, text_medium_rect)
    screen.blit(text_hard, text_hard_rect)
    pygame.display.flip()

    valid_options = {pygame.K_1: 5, pygame.K_2: 10, pygame.K_3: 15}
    selected_option = None

    # Esperar la entrada del usuario
    while selected_option is None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in valid_options:
                    selected_option = valid_options[event.key]
                else:
                    # Mostrar mensaje de error en la pantalla
                    error_font = pygame.font.Font(None, 24)
                    error_text = error_font.render("Por favor, selecciona una opción válida (1, 2 o 3).", True, (255, 0, 0))
                    error_text_rect = error_text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 50))
                    screen.blit(error_text, error_text_rect)
                    pygame.display.flip()

                if event.key == pygame.K_ESCAPE:  # Salir si se presiona Esc
                    pygame.quit()
                    return

    return selected_option