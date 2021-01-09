from pygame import *
from animations import *

class trainer():
    def __init__(self, x, y, width, height):
        # Pos. attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5


        # Attributes for walk direction
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0

    def draw(self, win):

        walkComplement = 3 #This is the divisor of the walkCount index

        if self.walkCount + 1 >= 12:
            self.walkCount = 0

        elif self.right:
            win.blit(playerAnimations.walkMCRight[self.walkCount // walkComplement], (self.x, self.y))
            self.walkCount += 1

        elif self.left:
            win.blit(playerAnimations.walkMCLeft[self.walkCount // walkComplement], (self.x, self.y))
            self.walkCount += 1

        elif self.up:
            win.blit(playerAnimations.walkMCUp[self.walkCount // walkComplement], (self.x, self.y))
            self.walkCount += 1

        elif self.down:
            win.blit(playerAnimations.walkMCDown[self.walkCount // walkComplement], (self.x, self.y))
            self.walkCount += 1
        else:
            if self.right:
                win.blit(playerAnimations.standingMCseries[3], (self.x, self.y))
            elif self.up:
                win.blit(playerAnimations.standingMCseries[1], (self.x, self.y))
            elif self.down:
                win.blit(playerAnimations.standingMCseries[0], (self.x, self.y))
            else:
                win.blit(playerAnimations.standingMCseries[2], (self.x, self.y))