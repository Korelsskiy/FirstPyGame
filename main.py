import pygame
pygame.init()

W, H = 600, 400
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("KorelskiyPyGame1")
pygame.display.set_icon(pygame.image.load("rifle.bmp"))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

x = 0
y = 0
for num in range(6):
    for num in range(6):
        pygame.draw.rect(sc, WHITE, (x, y, 48, 48))
        x += 50
    x = 0
    y += 50

pygame.display.update()

clock = pygame.time.Clock()
FPS = 60

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        clock.tick(FPS)