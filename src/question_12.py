import time

import pygame

HEIGHT = 600
WIDTH = 800
RADIUS = 100

MID_POINT_SCREEN = (int(WIDTH / 2), int(HEIGHT / 2))

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Questão 12")


class Circle(object):
    def __init__(self):
        self.circle = None
        self.x, self.y = list(MID_POINT_SCREEN)

    def draw(self):
        self.circle = pygame.draw.circle(screen, YELLOW, (self.x, self.y), RADIUS)

    def handle_border(self):
        if self.x - RADIUS == 0:
            self.x = WIDTH - RADIUS
        elif self.x + RADIUS == WIDTH:
            self.x = 0 + RADIUS

        if self.y - RADIUS == 0:
            self.y = HEIGHT - RADIUS
        elif self.y + RADIUS == HEIGHT:
            self.y = 0 + RADIUS

    def handle_event(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.x -= 1
        elif key[pygame.K_d]:
            self.x += 1
        elif key[pygame.K_w]:
            self.y -= 1
        elif key[pygame.K_s]:
            self.y += 1


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
        circle.handle_border()
        circle.handle_event()
        pygame.display.update()

        time.sleep(0.002)

    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
