import math

import pygame

HEIGHT = 600
WIDTH = 800
SIDE_SIZE = 50

INITIAL_SPEED = 240

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Questão 15")


class Polygon(object):
    def __init__(self):
        self.x, self.y = screen.get_width() // 2, screen.get_height() // 2

    def draw(self):
        """
        Based on: https://nerdparadise.com/programming/pygame/part4
        """
        num_points = 5
        angulation_constant = 90

        points = []
        for i in range(num_points * 2):
            radius = 100  # Polygon size
            if (
                i % 2 != 0
            ):  # It would be a normal polygon if the normal radius was applied.
                radius = radius // 2
            ang = (i * math.pi / num_points) + (angulation_constant * math.pi / 60)
            x = self.x + int(math.cos(ang) * radius)
            y = self.y + int(math.sin(ang) * radius)
            points.append((x, y))
        pygame.draw.polygon(screen, YELLOW, points)


def handle_quit(event):
    pressed_keys = pygame.key.get_pressed()

    alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
    alt_f4 = alt_pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_F4

    escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE

    x_button = event.type == pygame.QUIT

    return x_button or alt_f4 or escape


def main():
    polygon = Polygon()
    pygame.init()
    clock = pygame.time.Clock()

    while True:
        event = pygame.event.poll()
        if handle_quit(event):
            break

        screen.fill(BLACK)

        polygon.draw()
        pygame.display.update()

        clock.tick(INITIAL_SPEED)

    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
