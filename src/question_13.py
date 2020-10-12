import pygame

HEIGHT = 600
WIDTH = 800
RADIUS = 100

MID_POINT_SCREEN = (int(WIDTH / 2), int(HEIGHT / 2))

INITIAL_SPEED = 240
SPEED_INCREASE = 1

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Questão 13")


class SpeedControl(object):
    speed = INITIAL_SPEED


class Circle(object):
    def __init__(self, speed_control=None):
        self.circle = None
        self.speed_control = speed_control or SpeedControl()
        self.x, self.y = list(MID_POINT_SCREEN)
        self.direction = 1

    def draw(self):
        self.circle = pygame.draw.circle(screen, GREEN, (self.x, self.y), RADIUS)

    def handle_border(self):
        if self.x - RADIUS == 0:
            self.direction = 1
            self.speed_control.speed += SPEED_INCREASE
        elif self.x + RADIUS == WIDTH:
            self.direction = -1
            self.speed_control.speed += SPEED_INCREASE

    def handle_movement(self):
        self.x += self.direction


def main():
    speed_control = SpeedControl()
    circle = Circle(speed_control)
    pygame.init()
    clock = pygame.time.Clock()

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
        circle.handle_movement()
        pygame.display.update()

        clock.tick(speed_control.speed)

    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
