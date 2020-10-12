import time

import pygame

HEIGHT = 600
WIDTH = 800

MID_POINT_SCREEN = (int(WIDTH / 2), int(HEIGHT / 2))

# Colors
RED = (255, 0, 0)
BLACK = (255, 255, 255)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Questão 11")


class Circle(object):
    def __init__(self):
        self.circle = None
        self.x, self.y = list(MID_POINT_SCREEN)

    def draw(self):
        if self.x + 100 == WIDTH:
            self.x = -100

        self.circle = pygame.draw.circle(screen, BLUE, (self.x, self.y), 100)

    def handle_movement(self):
        self.x += 1


def main():
    circle = Circle()
    pygame.init()

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                break

        screen.fill(BLACK)

        circle.draw()
        circle.handle_movement()
        pygame.display.update()

        time.sleep(0.002)

    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
