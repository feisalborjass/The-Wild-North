import sys, pygame


class PointSystem (object):
    def __init__(self,windowSurface):
        self.score = 0 
        self.windowSurface = windowSurface
        self.font = pygame.font.SysFont(None, 48)
        self.highscore = 0
        
    def addToScore(self, enemies): #adds a score to the score counter depending on what enemy has been hit
        if enemies == 'Beaver':
            self.score += 5
        if enemies == 'coffee' or enemies == 'pancake':
            self.score += 15
        if enemies == 'hockey':
            self.score += 10
        if enemies == 'moose':
            self.score += 20
    
    def printScore(self):
        self.text = self.font.render(('Score: ' + str(self.score)),True,(0, 0, 0),(226, 238, 255))
        self.windowSurface.blit(self.text,(20,20))
    #Saves high Score in instance
    def setHi_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
    
    def printHighScore(self,where,colour):
        self.text = self.font.render(('High Score: ' + str(self.highscore)),True,(0, 0, 0),colour)
        self.windowSurface.blit(self.text,where)