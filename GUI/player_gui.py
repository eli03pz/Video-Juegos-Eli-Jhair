import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        # Cargar la imagen del jugador y redimensionarla si es necesario
        self.image = pygame.image.load("assets/pollitobonito.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Redimensionar al tamaño deseado
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
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
        if self.rect.top > 0:  # Verifica que el jugador no esté en el borde superior
            self.rect.y -= self.speed

    def move_down(self):
        # Método para mover el jugador hacia abajo
        if self.rect.bottom < self.screen_height:  # Verifica que el jugador no esté en el borde inferior
            self.rect.y += self.speed

    def move_left(self):
        # Método para mover el jugador hacia la izquierda
        if self.rect.left > 0:  # Verifica que el jugador no esté en el borde izquierdo
            self.rect.x -= self.speed

    def move_right(self):
        # Método para mover el jugador hacia la derecha
        if self.rect.right < self.screen_width:  # Verifica que el jugador no esté en el borde derecho
            self.rect.x += self.speed
