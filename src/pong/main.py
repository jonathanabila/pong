from abc import ABC, abstractmethod

import pygame

# Window
HEIGHT = 600
WIDTH = 800

# Game Speed
FPS = 240

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
    def draw(self):
        pass


class Component(BaseComponent):
    def __init__(self, x, y):
        self.x, self.y = x, y


class Ball(Component):
    def __init__(self):
        x, y = get_middle_screen()
        super().__init__(x, y)

    def draw(self):
        x, y = get_middle_screen()
        center_x, center_y = x - BALL_SIZE // 2, y - BALL_SIZE // 2

        pygame.draw.rect(screen, WHITE, (center_x, center_y, BALL_SIZE, BALL_SIZE))


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


class Player(Component):
    def __init__(self, right_side=False):
        self.right_side = right_side

        x, y = self._get_start_position()

        super().__init__(x, y)

    def _get_player_side(self):
        if self.right_side:
            return screen.get_width() - FIELD_PADDING
        else:
            return FIELD_PADDING

    def _get_start_position(self):
        x = self._get_player_side()
        _, center_y = get_middle_screen()

        return x, center_y - PLAYER_HEIGHT // 2

    def _get_player_position(self):
        return (self.x, self.y), (self.x, self.y + PLAYER_HEIGHT)

    def draw(self):
        start, end = self._get_player_position()
        pygame.draw.line(screen, WHITE, start, end, PLAYER_WIDTH)


class Game(BaseComponent):
    def __init__(self):
        # Field
        self.field = Field()
        self.ball = Ball()

        # Players
        self.player_1 = Player()
        self.player_2 = Player(right_side=True)

    def draw(self):
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
