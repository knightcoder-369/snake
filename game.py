# import pygame.event

from settings import *
from snake import Snake
from apple import Apple


class Main:
    def __init__(self):
        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # created window
        pygame.display.set_caption('snake')
        # gaem object in the below the first arg is left side and the second arg is the TOP ,widht,height
        # we are also using list comprehension
        self.bg_rects = [pygame.Rect((COL + int(row % 2 == 0)) * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE) for
                         COL in range(0, COLS, 2)
                         for row in range(ROWS)]
        # LET ME explain the above lsit comprehension we have two for loop one for the colums nad other for the row
        self.snake = Snake()
        self.apple = Apple(self.snake)
        # timer
        self.update_event = pygame.event.custom_type()
        pygame.time.set_timer(self.update_event, 200)
        self.game_active = False
        self.draw_data = []

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.snake.direction = pygame.Vector2(1, 0) if self.snake.direction.x != -1 else self.snake.direction
        if keys[pygame.K_LEFT]:
            self.snake.direction = pygame.Vector2(-1, 0) if self.snake.direction.x != 1 else self.snake.direction
        if keys[pygame.K_UP]:
            self.snake.direction = pygame.Vector2(0, -1) if self.snake.direction.y != 1 else self.snake.direction
        if keys[pygame.K_DOWN]:
            self.snake.direction = pygame.Vector2(0, 1) if self.snake.direction.y != --1 else self.snake.direction

    def draw_bg(self):
        self.display_surface.fill('#a2d149')  # adds green colur in the background

        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, '#a2d149', rect)

    def collision(self):
        # apple
        if self.snake.body[0] == self.apple.pos:
            # print("munch")
            self.snake.has_eaten = True
            self.apple.set_pos()
        # game over
        if self.snake.body[0] in self.snake.body[1:] or \
                not 0 <= self.snake.body[0].x < COLS or not 0 <= self.snake.body[0].y < ROWS:
            self.snake.reset()
            self.game_active = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    exit()
                if (event.type == self.update_event and self.game_active):
                    # updates
                    self.snake.update()
                if event.type == pygame.KEYDOWN and not self.game_active:
                    self.game_active = True

            # updates
            self.input()
            self.collision()
            # drawing
            self.draw_bg()
            self.snake.draw()
            self.apple.draw()
            pygame.display.update()

            pygame.display.update()


main = Main()
main.run()
    
    
