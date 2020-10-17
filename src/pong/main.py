import random
from abc import ABC, abstractmethod

import pygame

# Window
HEIGHT = 600
WIDTH = 800

X_START = 0

# Font Configuration
FONT_SIZE = 20
FONT_STYLE = "freesansbold.ttf"

# Game Speed
FPS = 144
HITS_TO_INCREASE_SPEED = 10

SPEED_INCREASE = 1

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

    @property
    def left(self):
        return self.rect.left

    @property
    def right(self):
        return self.rect.right

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom

    @property
    def center_y(self):
        return self.rect.centery

    @center_y.setter
    def center_y(self, value):
        self.rect.centery = value

    @property
    def center_x(self):
        return self.rect.centerx

    @center_x.setter
    def center_x(self, value):
        self.rect.centerx = value

    @property
    def center(self):
        return self.rect.center

    @center.setter
    def center(self, value):
        self.rect.center = value

    def draw(self, color):
        pygame.draw.rect(screen, color, self.rect)

    @abstractmethod
    def move(self):
        pass


class ScoreBoard(BaseComponent):
    def __init__(self):
        self.font = pygame.font.Font(FONT_STYLE, FONT_SIZE)

    @staticmethod
    def _get_score_position():
        center_x, _ = get_middle_screen()
        x = (center_x + WIDTH) // 2
        return x, FIELD_PADDING

    def draw(self, score):
        text = self.font.render(f"Placar = {score}", True, WHITE)

        score_pos = self._get_score_position()
        text_rect = text.get_rect(center=score_pos)
        screen.blit(text, text_rect)


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

    def change_y_direction(self):
        d_x, d_y = self.direction
        self.direction = (d_x, d_y * -1)

    def change_x_direction(self):
        d_x, d_y = self.direction
        self.direction = (d_x * -1, d_y)

    def move(self):
        d_choices = [-1, 1]
        if set(self.direction) == {None}:
            self.direction = (random.choice(d_choices), random.choice(d_choices))
        else:
            d_x, d_y = self.direction
            self.x, self.y = self.x + d_x, self.y + d_y

    def draw(self, *args, **kwargs):
        if not self.x and not self.y:
            self.x, self.y = self._start_position
        super().draw(WHITE)

    def check_collision(self):
        if self.top == 0:
            self.change_y_direction()
        elif self.bottom == HEIGHT:
            self.change_y_direction()


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
        self.score = 0
        self.hits = 0

        self.sound = None

        x, y = self._get_start_position()
        self._load_sound()
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

    def _load_sound(self):
        if pygame.mixer.get_init():
            self.sound = pygame.mixer.Sound("./pong/sounds/player.mp3")

    def score_point(self):
        self.score += 1

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

    def move(self, up=False):
        if up:
            direction = -1
            if self.top == 0:
                return
        else:
            direction = 1
            if self.bottom == HEIGHT:
                return

        self.y += direction

    def play_sound(self):
        if self.sound:
            self.sound.play()


class Game(BaseComponent):
    def __init__(self):
        # Settings
        self.speed = FPS
        self.score_board = ScoreBoard()

        # Field
        self.field = Field()
        self.ball = Ball()

        # Players
        self.player_1 = Player()
        self.player_2 = Player(right_side=True)

    def reset(self):
        center_x, center_y = get_middle_screen()

        self.player_1.center_y = center_y
        self.player_1.hits = 0

        self.player_2.center_y = center_y

        self.ball.direction = (None, None)
        self.ball.center = center_x, center_y

        self.speed = FPS

    def score_hit_hall(self, player, points=1):
        player.score += points
        self.reset()

    def hit_player(self, player, left_player=False):
        if (
            left_player
            and player.right == self.ball.left
            and player.bottom >= self.ball.center_y >= player.top
        ):
            player.play_sound()
            return True
        elif (
            not left_player
            and player.left == self.ball.right
            and player.bottom >= self.ball.center_y >= player.top
        ):
            player.play_sound()
            return True

        return False

    def hit_border(self, x_border):
        return self.ball.left == x_border or self.ball.right == x_border

    def _check_player_collisions(self):
        if self.hit_player(self.player_1, left_player=True):
            self.player_1.hits += 1
            self.player_1.score_point()
            self.ball.change_x_direction()
        elif self.hit_player(self.player_2):
            self.ball.change_x_direction()

    def _check_field_collisions(self):
        self.ball.check_collision()

        if self.hit_border(X_START):
            self.score_hit_hall(self.player_2)
        elif self.hit_border(WIDTH):
            self.score_hit_hall(self.player_1, 10)

    def _check_collisions(self):
        self._check_field_collisions()
        self._check_player_collisions()

    def ai_player(self):
        d_x, _ = self.ball.direction
        _, center_y = get_middle_screen()

        if center_y == self.player_2.center_y and d_x != 1:
            return

        if d_x == 1:
            if self.ball.center_y > self.player_2.bottom:
                self.player_2.move(up=False)
            else:
                self.player_2.move(up=True)
        else:

            if self.player_2.center_y > center_y:
                self.player_2.move(up=True)
            else:
                self.player_2.move(up=False)

    def _check_speed_increase_score(self):
        if self.speed > FPS and self.speed % 2 == 0:
            self.player_1.score_point()

    def _check_speed_increase(self):
        if self.player_1.hits > 0 and self.player_1.hits % HITS_TO_INCREASE_SPEED == 0:
            self.speed += SPEED_INCREASE
            self.player_1.hits = 0

            self._check_speed_increase_score()

    def draw(self):
        # Draw ScoreBoard
        self.score_board.draw(self.player_1.score)

        # Check collisions before making any movement
        self._check_collisions()
        self._check_speed_increase()

        # Moves the ball
        self.ball.move()

        # Draw items on the the screen
        self.field.draw()
        self.player_1.draw()
        self.player_2.draw()
        self.ball.draw()

        # Make AI player with player 2
        self.ai_player()

    def handle_event(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.player_1.move(up=True)
        elif key[pygame.K_s]:
            self.player_1.move(up=False)


def _load_mixer():
    try:
        pygame.mixer.pre_init()
        pygame.mixer.init()
    except pygame.error:
        print("Starting without sounds")


def main():
    pygame.init()
    _load_mixer()
    clock = pygame.time.Clock()
    game = Game()

    while True:
        event = pygame.event.poll()
        if handle_quit(event):
            break

        screen.fill(BLACK)
        game.draw()
        game.handle_event()
        pygame.display.update()
        clock.tick(game.speed)

    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
