import pygame

HEIGHT = 600
WIDTH = 800

MID_POINT_SCREEN = (int(WIDTH / 2), int(HEIGHT / 2))

# Colors
RED = (255, 0, 0)
BLACK = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Questão 10")


class Rect(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((350, 250, 100, 100))

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.move_ip(-1, 0)
        elif key[pygame.K_d]:
            self.rect.move_ip(1, 0)
        elif key[pygame.K_w]:
            self.rect.move_ip(0, -1)
        elif key[pygame.K_s]:
            self.rect.move_ip(0, 1)


def main():
    rect = Rect()
    pygame.init()

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                break

        screen.fill(BLACK)

        rect.draw()
        rect.handle_keys()
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
