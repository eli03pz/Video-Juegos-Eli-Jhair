import pygame

# Función para cargar una imagen de fondo
def cargar_fondo(ruta_imagen, screen):
    background_image = pygame.image.load(ruta_imagen).convert()
    screen.blit(background_image, (0, 0))

# Función para dibujar botones con efecto 3D
def dibujar_boton(screen, texto, posicion, tamano, color_fondo, color_texto):
    font = pygame.font.Font(None, tamano)
    boton_texto = font.render(texto, True, color_texto)
    boton_rect = boton_texto.get_rect(center=posicion)

    # Dibujar el fondo del botón (efecto 3D)
    pygame.draw.rect(screen, (200, 200, 200), (boton_rect.x - 5, boton_rect.y - 5, boton_rect.width + 10, boton_rect.height + 10))
    pygame.draw.rect(screen, color_fondo, boton_rect)

    # Dibujar el texto del botón
    screen.blit(boton_texto, boton_rect.center)
    return boton_rect

# Función para el lobby con botones y fondo
def lobby_con_botones(screen, fondo_imagen):
    cargar_fondo(fondo_imagen, screen)

    # Dibujar botones con efecto 3D y colores especificados
    boton_facil = dibujar_boton(screen, "Fácil", (screen.get_width() // 2, screen.get_height() // 3), 42, (214, 0, 113), (255, 255, 255))
    boton_medio = dibujar_boton(screen, "Medio", (screen.get_width() // 2, screen.get_height() // 2), 42, (255, 58, 150), (255, 255, 255))
    boton_dificil = dibujar_boton(screen, "Difícil", (screen.get_width() // 2, screen.get_height() // 1.5), 42, (0, 221, 103), (255, 255, 255))

    pygame.display.flip()

    # Validar selección del usuario
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if boton_facil.collidepoint(mouse_pos):
                    return 5  # Opción seleccionada para Fácil
                elif boton_medio.collidepoint(mouse_pos):
                    return 10  # Opción seleccionada para Medio
                elif boton_dificil.collidepoint(mouse_pos):
                    return 15  # Opción seleccionada para Difícil
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return

# Ejemplo de uso
pygame.init()
screen = pygame.display.set_mode((800, 600))
fondo_imagen = "assets/lobbyde.jpg"  # Reemplaza con la ruta de tu imagen de fondo
selected_option = lobby_con_botones(screen, fondo_imagen)
print("Opción seleccionada:", selected_option)
pygame.quit()
