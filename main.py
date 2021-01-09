import pygame
from objectPlayers import *
from animations import *

pygame.init()

winSizeX = 480
winSizeY = 480

win = pygame.display.set_mode((winSizeX, winSizeY))

clock = pygame.time.Clock()

player = trainer(300, 400, 64, 64)



def winDrawChanger():
    win.blit(bg1, (0, 0))
    player.draw(win)
    pygame.display.update()


run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and player.x < winSizeX - player.height - player.vel:
        player.x += player.vel
        player.right = True
        player.left = False
        player.up = False
        player.down = False

    elif keys[pygame.K_a] and player.x > player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.up = False
        player.down = False

    elif keys[pygame.K_w] and player.y > player.vel:
        player.y -= player.vel
        player.up = True
        player.down = False
        player.left = False
        player.right = False

    elif keys[pygame.K_s] and player.y < winSizeY - player.height - player.vel:
        player.y += player.vel
        player.up = False
        player.down = True
        player.left = False
        player.right = False

    else:
        player.right = False
        player.left = False
        player.left = False
        player.right = False
        player.walkCount = 0

    winDrawChanger()




pygame.quit