import pygame, sys, random

#creates a class that will allow for access of center x and y values
class Center():
    def __init__(self, display_width, display_height):
        self.x = display_width / 2
        self.y = display_height / 2
        self.center = (display_width, display_height)
        
#creates a function that will terminate the program
def terminate():
    sys.exit()
    
def render(screen, colour, rect):
    pygame.draw.rect(screen, colour, rect)
    
def newEnemyPerTick(enemyType, enemyList, numTicks, maxTicks):
    if numTicks % maxTicks == 0:
        enemyList.append(enemyType)
        numTicks = 0
    return numTicks

def trueOrFalse():
    check = random.randint(1, 2)
    if check == 1:
        return True
    if check == 2:
        return False

