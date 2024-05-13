import pygame
import random
import sys
from GUI.player_gui import Player
from GUI.obstacle_gui import Obstacle
from Models.Score_manager import ScoreManager
from Models.Utils.game_over import show_game_over_screen, reset_game

def run_game(difficulty):
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCORE_UPDATE_INTERVAL = 1000  

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Esquiva y avanza")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    obstacle_group = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    all_sprites.add(player)

    score_manager = ScoreManager()

    running = True
    game_over = False
    last_score_update_time = pygame.time.get_ticks()  

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            if random.randrange(100) < difficulty:
                new_obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT)
                all_sprites.add(new_obstacle)
                obstacle_group.add(new_obstacle)

            if pygame.sprite.spritecollide(player, obstacle_group, False):
                game_over = True  
            else:
                current_time = pygame.time.get_ticks()
                if current_time - last_score_update_time >= SCORE_UPDATE_INTERVAL:
                    score_manager.increment_score(1)  
                    last_score_update_time = current_time  

            all_sprites.update()

            screen.fill((255, 255, 255))
            all_sprites.draw(screen)

            score_text = score_manager.get_score_text()
            screen.blit(score_text, (10, 10))
        else:
            action = show_game_over_screen(screen)
            if action == 'restart':
                game_over = False
                reset_game(player, all_sprites, obstacle_group, score_manager, SCREEN_WIDTH, SCREEN_HEIGHT)
            elif action == 'quit':
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(30)
