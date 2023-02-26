import pygame


def start():
    size = (300, 300)
    pygame.init()
    pygame.display.set_caption('перетащил')
    screen = pygame.display.set_mode(size)
    running = True
    x1 = x = 0
    y1 = y = 0
    moving = False
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    fps = 60
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    if x1 in range(x, x + 101) and y1 in range(y, y + 101):
                        moving = True
            if event.type == pygame.MOUSEMOTION:
                if moving:
                    x1, y1 = event.rel
                    x = x1 + x
                    y = y1 + y
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                moving = False

        rect = pygame.draw.rect(screen, (0, 255, 0), (x, y, 100, 100))
        clock.tick(fps)
        pygame.display.flip()


if __name__ == '__main__':
    start()
