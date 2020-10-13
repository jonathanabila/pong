import random
from abc import ABC, abstractmethod

import pygame

# Window
HEIGHT = 600
WIDTH = 800

# Game Speed
FPS = 144

# Components
LINE_WIDTH = 3
FIELD_PADDING = 20
BALL_SIZE = 15

PLAYER_WIDTH = 12
PLAYER_HEIGHT = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")


def handle_quit(event):
    pressed_keys = pygame.key.get_pressed()

    alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
    alt_f4 = alt_pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_F4

    escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE

    x_button = event.type == pygame.QUIT

    return x_button or alt_f4 or escape


def get_middle_screen():
    return screen.get_width() // 2, screen.get_height() // 2


class BaseComponent(ABC):
    @abstractmethod
    def draw(self, *args, **kwargs):
        pass


class Rect(BaseComponent):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, value):
        self.rect.x = value

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, value):
        self.rect.y = value

    def draw(self, color):
        pygame.draw.rect(screen, color, self.rect)


class Ball(Rect):
    def __init__(self, direction=(None, None)):
        self.direction = direction

        x, y = self._start_position()
        super().__init__(x, y, BALL_SIZE, BALL_SIZE)

    @staticmethod
    def _start_position():
        x, y = get_middle_screen()
        center_x, center_y = x - BALL_SIZE // 2, y - BALL_SIZE // 2
        return center_x, center_y

    def move(self):
        d_choices = [-1, 1]
        if self.direction == (None, None):
            self.direction = (random.choice(d_choices), random.choice(d_choices))
        else:
            d_x, d_y = self.direction
            self.x, self.y = self.x + d_x, self.y + d_y

    def draw(self, *args, **kwargs):
        if not self.x and not self.y:
            self.x, self.y = self._start_position
        super().draw(WHITE)


class Field(BaseComponent):
    @staticmethod
    def _draw_field():
        pygame.draw.rect(screen, WHITE, ((0, 0), (WIDTH, HEIGHT)), LINE_WIDTH)

    @staticmethod
    def _draw_mid_line():
        start = ((WIDTH // 2), 0)
        end = ((WIDTH // 2), HEIGHT)

        pygame.draw.line(screen, WHITE, start, end, LINE_WIDTH)

    def draw(self):
        self._draw_mid_line()


class Player(Rect):
    def __init__(self, right_side=False):
        self.right_side = right_side

        x, y = self._get_start_position()
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

    def _get_player_side(self):
        if self.right_side:
            return screen.get_width() - FIELD_PADDING
        else:
            return FIELD_PADDING

    def _get_start_position(self):
        x = self._get_player_side()
        _, center_y = get_middle_screen()

        return x, center_y - PLAYER_HEIGHT // 2

    def draw(self, *args, **kwargs):
        super().draw(WHITE)


class Game(BaseComponent):
    def __init__(self):
        # Field
        self.field = Field()
        self.ball = Ball()

        # Players
        self.player_1 = Player()
        self.player_2 = Player(right_side=True)

    def draw(self):
        self.ball.move()

        self.field.draw()
        self.player_1.draw()
        self.player_2.draw()
        self.ball.draw()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    game = Game()

    while True:
        event = pygame.event.poll()
        if handle_quit(event):
            break

        screen.fill(BLACK)
        game.draw()
        pygame.display.update()
        clock.tick(FPS)

    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
