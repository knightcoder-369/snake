from settings import *
from random import choice
from math import sin  # Import sin from math
import pygame


class Apple:
    def __init__(self, snake):
        self.pos = pygame.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.snake = snake  # Reference to snake object
        self.surf = pygame.image.load('fruit12.png').convert_alpha()
        self.set_pos()  # Initialize the apple position

    def set_pos(self):
        # Filter out positions occupied by the snake's body
        available_pos = [
            pygame.Vector2(x, y)
            for x in range(COLS)
            for y in range(ROWS)
            if pygame.Vector2(x, y) not in self.snake.body
        ]

        # Choose a random position from available positions
        if available_pos:
            self.pos = choice(available_pos)
        else:
            print("Warning: No available positions for the apple!")

    def draw(self):
        scale = 1 + sin(pygame.time.get_ticks() / 600) / 3
        scaled_surf = pygame.transform.smoothscale(self.surf, (
        int(self.surf.get_width() * scale), int(self.surf.get_height() * scale)))
        scaled_rect = scaled_surf.get_rect(
            center=(self.pos.x * CELL_SIZE + CELL_SIZE / 2, self.pos.y * CELL_SIZE + CELL_SIZE / 2))
        self.display_surface.blit(scaled_surf, scaled_rect)