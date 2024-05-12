from Player import Player
from Maze import Maze

class Game:
    def __init__(self):
        self.player = Player(100, 100)
        self.maze = Maze()

    def handle_input(self, key):
        if key == 'UP':
            self.player.move_up()
        elif key == 'DOWN':
            self.player.move_down()
        elif key == 'LEFT':
            self.player.move_left()
        elif key == 'RIGHT':
            self.player.move_right()

    def update(self):
        # Actualizar la lógica del juego
        pass

    def draw(self, screen):
        # Dibujar el juego en la pantalla
        pass

    def iniciar_juego(self, dificultad):
        if dificultad == 'facil':
            # Lógica para iniciar el juego en dificultad fácil
            print("Iniciando juego en dificultad Fácil...")
            self.player = Player(100, 100)  # Reinicio del jugador
            self.maze = Maze()  # Reinicio del laberinto
            self.maze.generate_maze(5, 5)  # Generar un laberinto de tamaño 5x5
        elif dificultad == 'medio':
            # Lógica para iniciar el juego en dificultad media
            print("Iniciando juego en dificultad Media...")
            self.player = Player(100, 100)  # Reinicio del jugador
            self.maze = Maze()  # Reinicio del laberinto
            self.maze.generate_maze(10, 10)  # Generar un laberinto de tamaño 10x10
        elif dificultad == 'dificil':
            # Lógica para iniciar el juego en dificultad difícil
            print("Iniciando juego en dificultad Difícil...")
            self.player = Player(100, 100)  # Reinicio del jugador
            self.maze = Maze()  # Reinicio del laberinto
            self.maze.generate_maze(15, 15)  # Generar un laberinto de tamaño 15x15
        else:
            print("Dificultad no válida. Por favor, elige una dificultad válida.")
