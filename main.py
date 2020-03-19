import pygame

m = input()
pygame.init()
size = width, height = 501, 501
screen = pygame.display.set_mode(size)
running = True
zoom = 10
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                zoom += 1
            elif event.button == 5:
                zoom -= 1
    screen.fill(pygame.Color('black'))
    a = [list(map(lambda x: int(float('.'.join(x.split(','))) * zoom) + 250,
                  ''.join(j for j in i if j not in ['(', ')']).split(';'))) for i in m.split(', ')]
    pygame.draw.polygon(screen, (0, 0, 255), a, 1)
    pygame.display.flip()
pygame.quit()