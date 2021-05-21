import pygame, math, random
from base_character import Character
from utilities import trueOrFalse


class Weapon(Character):
    pass
    
class Enemy(Character):
    
    def __init__(self, x, y, width, height, display_width, windowSurface):
        self.x = x 
        self.y = y
        self.height = height
        self.width = 85
        self.id = 'Beaver'
        self.display_width = display_width
        self.windowSurface = windowSurface
        self.size = 35
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = trueOrFalse()
        self.moveSpeed = 5
        self.timeToLeave = False
        self.counter = 0
        
    def moveLeft(self):
        if self.rect.left <= self.display_width and self.rect.left >= 0:
            self.rect.left -= self.moveSpeed
            
    def moveRight(self):
        if self.rect.left <= self.display_width - 30 and self.rect.left >= -10:
            self.rect.left += self.moveSpeed
            
    def moveUp(self):
        self.rect.top -= 4
    
class FlyingEnemy(Enemy):
    
    def __init__(self, x, y, width, height, display_width, windowSurface):
        self.x = x 
        self.y = y
        self.startPosY = y
        self.height = height
        self.width = 55
        self.id = 'coffee'
        self.display_width = display_width
        self.windowSurface = windowSurface
        self.size = 35
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = trueOrFalse()
        self.moveSpeed = 3
        self.flightFactor = 7
        self.counter = 0
    
    def fly(self):
        self.counter += 1
        if self.rect.left <= self.display_width and self.rect.left >= 0 and self.counter <= 1000:
            self.counter += math.pi
            self.rect.top += math.sin(math.radians(self.counter)) * self.flightFactor
        if self.counter >= 1000:
            self.moveUp()
            
    def moveUp(self):
        self.rect.top -= self.moveSpeed
    
    def appearFromTop(self):
        if self.rect.top <= 650 and self.counter <= 250:
            self.rect.top += self.moveSpeed
        
class Pancake(Enemy):
    
    def __init__(self, x, y, width, height, display_width, windowSurface):
        self.x = x 
        self.y = y
        self.height = height
        self.width = width
        self.id = 'pancake'
        self.display_width = display_width
        self.windowSurface = windowSurface
        self.size = 35
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = trueOrFalse()
        self.moveSpeed = 4
        self.velocityY = 0
        self.onGround = False
        self.reachedSurface = False
        
    def bounce(self):
        if self.rect.left <= self.display_width and self.rect.left >= 0:
            self.onGround = False       
            self.y -= self.velocityY 
            self.velocityY -= 0.5
    
    def moveLeft(self):
        self.x -= self.moveSpeed
            
    def moveRight(self):
        self.x += self.moveSpeed
        
    def moveUp(self):
        self.y -= self.moveSpeed
        
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    

class HockeyPlayer(Enemy):
    
    def __init__(self, x, enemyGroundPosY, width, height, display_width, windowSurface):
        self.x = x 
        self.y = enemyGroundPosY
        self.height = height
        self.width = width
        self.id = 'hockey'
        self.display_width = display_width
        self.windowSurface = windowSurface
        self.size = 35
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.moveSpeed = 2
        self.timeToLeave = False
        self.counter = 1
        
        if self.x == 1:
            self.rect.left = 0 - 100
            self.direction = True
        if self.x == 2:
            self.rect.left = display_width + 100
            self.direction = False
    
    def appearFromLeft(self):
        if self.rect.left <= 0 and self.timeToLeave == False:
            self.rect.left += self.moveSpeed
    
    def appearFromRight(self):
        if self.rect.left >= self.display_width - self.width - 25 and self.timeToLeave == False:
            self.rect.left -= self.moveSpeed
            
    def moveLeft(self):
        self.rect.left -= self.moveSpeed
            
    def moveRight(self):
        self.rect.left += self.moveSpeed
    
    def shootPuck(self, enemyList):
        puck = Puck(self.rect.left, self.rect.top, self.direction, self.display_width, self.windowSurface)
        enemyList.append(puck)


class Puck(HockeyPlayer):
    
    def __init__(self, x, enemyGroundPosY, hockeyPlayerDirection, display_width, windowSurface):    
        self.x = x 
        self.y = enemyGroundPosY + 20
        self.id = 'puck'
        self.display_width = display_width
        self.windowSurface = windowSurface
        self.size = 25
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.direction = hockeyPlayerDirection
        self.moveSpeed = 8
        
    def render(self, colorName):
        pygame.draw.rect(self.windowSurface, colorName, (self.x, self.y, self.size, self.size))
    
class Moose(Enemy):
    
    def __init__(self, x, y, width, height, display_width, windowSurface):
        self.x = x 
        self.y = y
        self.height = height
        self.width = width
        self.id = 'moose'
        self.display_width = display_width
        self.windowSurface = windowSurface
        self.size = 35
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = True
        self.moveSpeed = 12
        self.counter = 0
        self.counter_stop = 100
        self.enemyGroundPosY = 318
        
        if self.x == 1:
            self.direction = True
        if self.x == 2:
            self.direction = False
            
        if self.direction == False:
            self.rect.left = 709
        

    def disappearFromLeft(self):
        self.rect.left -= 4
    
    def dropFromTop(self):
        if self.rect.top <= self.enemyGroundPosY:
            self.rect.top += self.moveSpeed
    
    def disappearFromRight(self):
        self.rect.left += 4
            
    def moveLeft(self):
        self.rect.left -= self.moveSpeed
            
    def moveRight(self):
        self.rect.left += self.moveSpeed
        
class Null(Enemy):
    
    def __init__(self, x, y, width, height, display_width, windowSurface):
        self.x = x 
        self.y = y
        self.height = height
        self.width = 85
        self.id = 'null'
        self.display_width = display_width
        self.windowSurface = windowSurface
        self.size = 35
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = trueOrFalse()
        self.moveSpeed = 5
        self.timeToLeave = False
        self.counter = 0
