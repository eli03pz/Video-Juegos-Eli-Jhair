import pygame
import time

pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Tamaño de cada celda del laberinto
CELL_SIZE = 40

# Definir laberintos para cada dificultad
facil_mazes = [
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ],
    # Agrega más laberintos para la dificultad fácil si lo deseas
]

medio_mazes = [
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ],
    # Agrega más laberintos para la dificultad media si lo deseas
]

dificil_mazes = [
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ],
    # Agrega más laberintos para la dificultad difícil si lo deseas
]

# Tiempo para cada dificultad (en segundos)
tiempo_facil = 180  # 3 minutos
tiempo_medio = 360  # 6 minutos
tiempo_dificil = 840  # 14 minutos

def draw_maze(screen, maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_player(screen, player_pos):
    pygame.draw.circle(screen, RED, (player_pos[0] * CELL_SIZE + CELL_SIZE // 2, player_pos[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

def game_over_screen(screen):
    # Mostrar pantalla de Game Over
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over", True, RED)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))

    # Opciones de volver a intentar o salir
    volver_a_intentar_text = font.render("Volver a Intentar", True, BLACK)
    salir_text = font.render("Salir", True, BLACK)
    screen.blit(volver_a_intentar_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20))
    screen.blit(salir_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 70))

    pygame.display.flip()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Laberinto Game")

    # Pantalla de selección de dificultad
    font = pygame.font.Font(None, 36)
    facil_text = font.render("Fácil", True, BLACK)
    medio_text = font.render("Medio", True, BLACK)
    dificil_text = font.render("Difícil", True, BLACK)
    salir_text = font.render("Salir", True, BLACK)

    screen.fill(WHITE)
    screen.blit(facil_text, (SCREEN_WIDTH // 2 - 50, 100))
    screen.blit(medio_text, (SCREEN_WIDTH // 2 - 50, 200))
    screen.blit(dificil_text, (SCREEN_WIDTH // 2 - 50, 300))
    screen.blit(salir_text, (SCREEN_WIDTH // 2 - 50, 400))
    pygame.display.flip()

    seleccionando_dificultad = True
    while seleccionando_dificultad:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 350 <= mouse_pos[0] <= 450:
                    if 100 <= mouse_pos[1] <= 150:
                        # Empezar juego en dificultad Fácil
                        jugar_laberinto(screen, facil_mazes, tiempo_facil)
                    elif 200 <= mouse_pos[1] <= 250:
                        # Empezar juego en dificultad Medio
                        jugar_laberinto(screen, medio_mazes, tiempo_medio)
                    elif 300 <= mouse_pos[1] <= 350:
                        # Empezar juego en dificultad Difícil
                        jugar_laberinto(screen, dificil_mazes, tiempo_dificil)
                    elif 400 <= mouse_pos[1] <= 450:
                        # Salir del juego
                        pygame.quit()
                        return

def jugar_laberinto(screen, mazes, tiempo_limite):
    for maze in mazes:
        jugador_pos = [1, 1]  # Posición inicial del jugador
        inicio = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if maze[jugador_pos[1] - 1][jugador_pos[0]] != 1:
                            jugador_pos[1] -= 1
                    elif event.key == pygame.K_DOWN:
                        if maze[jugador_pos[1] + 1][jugador_pos[0]] != 1:
                            jugador_pos[1] += 1
                    elif event.key == pygame.K_LEFT:
                        if maze[jugador_pos[1]][jugador_pos[0] - 1] != 1:
                            jugador_pos[0] -= 1
                    elif event.key == pygame.K_RIGHT:
                        if maze[jugador_pos[1]][jugador_pos[0] + 1] != 1:
                            jugador_pos[0] += 1

            screen.fill(WHITE)
            draw_maze(screen, maze)
            draw_player(screen, jugador_pos)

            pygame.display.flip()

            if jugador_pos == [len(maze[0]) - 2, len(maze) - 2]:
                # El jugador llegó a la salida
                break

            if time.time() - inicio > tiempo_limite:
                # Se acabó el tiempo, mostrar pantalla de Game Over
                game_over_screen(screen)
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if 350 <= mouse_pos[0] <= 450:
                                if 100 <= mouse_pos[1] <= 150 or 200 <= mouse_pos[1] <= 250:
                                    # Volver a intentar o salir
                                    jugar_laberinto(screen, mazes, tiempo_limite)
                                elif 300 <= mouse_pos[1] <= 350:
                                    # Salir del juego
                                    pygame.quit()
                                    return

    # Si el jugador completa todos los niveles
    print("¡Felicidades! Has completado todos los niveles.")

main()
