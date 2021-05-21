import pygame

class Character(object):
    
    def __init__(self, x, y, width, height, display_width, windowSurface):
        self.x = x 
        self.y = y
        self.height = height
        self.width = width
        self.direction = True
        self.health = 4
        self.display_width = display_width
        self.windowSurface = windowSurface
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.moveSpeed = 8
        self.velocityY = 0
        self.onGround = False
        
    def jump(self):
        self.onGround = False       
        self.y = self.y - self.velocityY 
        self.velocityY = self.velocityY - 1.5
            
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
         
    def moveLeft(self):
        if self.x <= self.display_width and self.x >= 0:
            self.x -= self.moveSpeed
            
    def moveRight(self):
        if self.x <= self.display_width - 30 and self.x >= -10:
            self.x += self.moveSpeed

    def render(self, colorName):
        pygame.draw.rect(self.windowSurface, colorName, (self.x, self.y, self.width, self.height))

