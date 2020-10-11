import pygame

HEIGHT = 600
WIDTH = 800

MID_POINT_SCREEN = (int(WIDTH / 2), int(HEIGHT / 2))

BLUE = (0, 0, 255)


def draw_circle():
    pygame.draw.circle(screen, BLUE, MID_POINT_SCREEN, 100)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    events = pygame.event.get()
    for event in events:
        draw_circle()
        pygame.display.update()

        if event.type == pygame.QUIT:
            running = False

pygame.display.quit()
pygame.quit()
