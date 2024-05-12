import pygame

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
