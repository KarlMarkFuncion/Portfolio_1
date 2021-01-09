import pygame
from Assets import *


class playerAnimations():

    standingMC = pygame.image.load('Assets/CharSprites/MC_walkDown1.png')

    standingMCseries = [
        pygame.image.load('Assets/CharSprites/MC_walkDown1.png'),
        pygame.image.load('Assets/CharSprites/MC_walkUp1.png'),
        pygame.image.load('Assets/CharSprites/MC_walkLeft1.png'),
        pygame.image.load('Assets/CharSprites/MC_walkRight1.png')
    ]

    walkMCRight = [
        pygame.image.load('Assets/CharSprites/MC_walkRight1.png'),
        pygame.image.load('Assets/CharSprites/MC_walkRight2.png'),
        pygame.image.load('Assets/CharSprites/MC_walkRight3.png'),
        pygame.image.load('Assets/CharSprites/MC_walkRight4.png'),
    ]

    walkMCLeft = [
        pygame.image.load('Assets/CharSprites/MC_walkLeft1.png'),
        pygame.image.load('Assets/CharSprites/MC_walkLeft2.png'),
        pygame.image.load('Assets/CharSprites/MC_walkLeft3.png'),
        pygame.image.load('Assets/CharSprites/MC_walkLeft4.png')
    ]

    walkMCUp = [
        pygame.image.load('Assets/CharSprites/MC_walkUp1.png'),
        pygame.image.load('Assets/CharSprites/MC_walkUp2.png'),
        pygame.image.load('Assets/CharSprites/MC_walkUp3.png'),
        pygame.image.load('Assets/CharSprites/MC_walkUp4.png')
    ]

    walkMCDown = [
        pygame.image.load('Assets/CharSprites/MC_walkDown1.png'),
        pygame.image.load('Assets/CharSprites/MC_walkDown2.png'),
        pygame.image.load('Assets/CharSprites/MC_walkDown3.png'),
        pygame.image.load('Assets/CharSprites/MC_walkDown4.png')

    ]


bg1 = pygame.image.load('Assets/Bgs/bg.png')
