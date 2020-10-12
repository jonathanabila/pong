import pygame

HEIGHT = 600
WIDTH = 800
SIDE_SIZE = 50

INITIAL_SPEED = 240

MID_POINT_SCREEN = (int(WIDTH / 2) - 25, int(HEIGHT / 2) - 25)

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Questão 14")


class Rect(object):
    def __init__(self):
        self.rect = None
        self.x, self.y = list(MID_POINT_SCREEN)

    def draw(self):
        self.rect = pygame.draw.rect(
            screen, GREEN, (self.x, self.y, SIDE_SIZE, SIDE_SIZE)
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            self.x, self.y = pos_x - int(SIDE_SIZE / 2), pos_y - int(SIDE_SIZE / 2)


def main():
    rect = Rect()
    pygame.init()
    clock = pygame.time.Clock()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        screen.fill(BLACK)

        rect.draw()
        rect.handle_event(event)
        pygame.display.update()

        clock.tick(INITIAL_SPEED)

    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
