import pygame, sys

pygame.init()

#Animation Class. Contains ALL ARAYS. 
class Animation(object):
    def __init__(self,windowSurface):
        self.windowSurface = windowSurface
        #LumberJack Array
        self.lmbr_0= pygame.image.load('./Sprites/lumber_00.png')
        self.lmbr_1= pygame.image.load('./Sprites/lumber_01.png')
        self.lmbr_2= pygame.image.load('./Sprites/lumber_02.png')
        self.lmbr_3= pygame.image.load('./Sprites/lumber_03.png')
        self.lmbr_4= pygame.image.load('./Sprites/lumber_04.png')
        self.lmbr_5= pygame.image.load('./Sprites/lumber_05.png')
        self.lmbr_6= pygame.image.load('./Sprites/lumber_06.png')
        self.lmbr_7= pygame.image.load('./Sprites/lumber_07.png')
        self.lmbr_8= pygame.image.load('./Sprites/lumber_08.png')
        self.lmbr_9= pygame.image.load('./Sprites/lumber_09.png')
        self.lmbr_10= pygame.image.load('./Sprites/lumber_10.png')
        self.lmbr_11= pygame.image.load('./Sprites/lumber_11.png')
        self.lmbr_12= pygame.image.load('./Sprites/lumber_12.png')
        self.lmbr_13= pygame.image.load('./Sprites/lumber_13.png')
        self.lmbr_14= pygame.image.load('./Sprites/lumber_14.png')
        #Sprite List
        self.lumber = [self.lmbr_0,self.lmbr_1,self.lmbr_2,self.lmbr_3,\
                       self.lmbr_4,self.lmbr_5,self.lmbr_6,self.lmbr_7,self.lmbr_8,\
                       self.lmbr_9,self.lmbr_10,self.lmbr_11,self.lmbr_12,\
                       self.lmbr_13,self.lmbr_14]
        #Sprite Frame Length
        self.lumber_f = ((len(self.lumber)) - 1)
        
        #Beaver Array
        self.bvr_0 = pygame.image.load('./Sprites/sprite_beaver00.png')
        self.bvr_1 = pygame.image.load('./Sprites/sprite_beaver01.png')
        self.bvr_2 = pygame.image.load('./Sprites/sprite_beaver02.png')
        self.bvr_3 = pygame.image.load('./Sprites/sprite_beaver03.png')
        self.bvr_4 = pygame.image.load('./Sprites/sprite_beaver04.png')
        self.bvr_5 = pygame.image.load('./Sprites/sprite_beaver05.png')
        self.bvr_6 = pygame.image.load('./Sprites/sprite_beaver06.png')
        self.bvr_7 = pygame.image.load('./Sprites/sprite_beaver07.png')
        self.bvr_8 = pygame.image.load('./Sprites/sprite_beaver08.png')
        self.bvr_9 = pygame.image.load('./Sprites/sprite_beaver09.png')
        self.bvr_10 = pygame.image.load('./Sprites/sprite_beaver10.png')
        self.bvr_11 = pygame.image.load('./Sprites/sprite_beaver11.png')
        self.bvr_12 = pygame.image.load('./Sprites/sprite_beaver12.png')
        self.bvr_13 = pygame.image.load('./Sprites/sprite_beaver13.png')
        self.bvr_14 = pygame.image.load('./Sprites/sprite_beaver14.png')
        self.bvr_15 = pygame.image.load('./Sprites/sprite_beaver15.png')
        self.bvr_16 = pygame.image.load('./Sprites/sprite_beaver16.png')
        self.bvr_17 = pygame.image.load('./Sprites/sprite_beaver17.png')
        self.bvr_18 = pygame.image.load('./Sprites/sprite_beaver18.png')
        self.bvr_19 = pygame.image.load('./Sprites/sprite_beaver19.png')
        #Sprite List
        self.beaver = [self.bvr_0,self.bvr_1,self.bvr_2,self.bvr_3,\
                       self.bvr_4,self.bvr_5,self.bvr_6,self.bvr_7,\
                       self.bvr_8,self.bvr_9,self.bvr_10,self.bvr_11,\
                       self.bvr_12,self.bvr_13,self.bvr_14,self.bvr_15,\
                       self.bvr_16,self.bvr_17,self.bvr_18,self.bvr_19]
        #Sprite Frame Length
        self.beaver_f = ((len(self.beaver)) - 1)
        
        #COFFEE CUP ARRAY
        self.FCC_0 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup00.png')
        self.FCC_1 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup01.png')
        self.FCC_2 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup02.png')
        self.FCC_3 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup03.png')
        self.FCC_4 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup04.png')
        self.FCC_5 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup05.png')
        self.FCC_6 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup06.png')
        self.FCC_7 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup07.png')
        self.FCC_8 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup08.png')
        self.FCC_9 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup09.png')
        self.FCC_10 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup10.png')
        self.FCC_11 = pygame.image.load('./Sprites/sprite_flyingCoffeeCup11.png')
        #Sprite List
        self.flyingCoffee = [self.FCC_0,self.FCC_1,self.FCC_2,self.FCC_3,\
                             self.FCC_4,self.FCC_5,self.FCC_6,self.FCC_7,\
                             self.FCC_8,self.FCC_9,self.FCC_10,self.FCC_11]
        #Sprite Frame Length
        self.flyingCoffee_f = ((len(self.flyingCoffee)) - 1)
        
        #PANCAKE ARRAY
        self.panc_0 = pygame.image.load('./Sprites/sprite_pancake00.png')
        self.panc_1 = pygame.image.load('./Sprites/sprite_pancake01.png')
        self.panc_2 = pygame.image.load('./Sprites/sprite_pancake02.png')
        self.panc_3 = pygame.image.load('./Sprites/sprite_pancake03.png')
        self.panc_4 = pygame.image.load('./Sprites/sprite_pancake04.png')
        self.panc_5 = pygame.image.load('./Sprites/sprite_pancake05.png')
        self.panc_6 = pygame.image.load('./Sprites/sprite_pancake06.png')
        self.panc_7 = pygame.image.load('./Sprites/sprite_pancake07.png')
        self.panc_8 = pygame.image.load('./Sprites/sprite_pancake08.png')
        self.panc_9 = pygame.image.load('./Sprites/sprite_pancake09.png')
        self.panc_10 = pygame.image.load('./Sprites/sprite_pancake10.png')
        self.panc_11 = pygame.image.load('./Sprites/sprite_pancake11.png')
        self.panc_12 = pygame.image.load('./Sprites/sprite_pancake12.png')
        self.panc_13 = pygame.image.load('./Sprites/sprite_pancake13.png')
        #Sprite List
        self.pancake = [self.panc_0,self.panc_1,self.panc_2,self.panc_3,\
                        self.panc_4,self.panc_5,self.panc_6,self.panc_7,\
                        self.panc_8,self.panc_9,self.panc_10,self.panc_11,\
                        self.panc_12,self.panc_13]
        #Sprite Frame Length
        self.pancake_f = ((len(self.pancake)) - 1)
        
        #Moose Array
        self.moose_0 = pygame.image.load('./Sprites/sprite_moose00.png')
        self.moose_1 = pygame.image.load('./Sprites/sprite_moose01.png')
        self.moose_2 = pygame.image.load('./Sprites/sprite_moose02.png')
        self.moose_3 = pygame.image.load('./Sprites/sprite_moose03.png')
        self.moose_4 = pygame.image.load('./Sprites/sprite_moose04.png')
        self.moose_5 = pygame.image.load('./Sprites/sprite_moose05.png')
        self.moose_6 = pygame.image.load('./Sprites/sprite_moose06.png')
        self.moose_7 = pygame.image.load('./Sprites/sprite_moose07.png')
        self.moose_8 = pygame.image.load('./Sprites/sprite_moose08.png')
        self.moose_9 = pygame.image.load('./Sprites/sprite_moose09.png')
        self.moose_10 = pygame.image.load('./Sprites/sprite_moose10.png')
        self.moose_11 = pygame.image.load('./Sprites/sprite_moose11.png')
        self.moose_12 = pygame.image.load('./Sprites/sprite_moose12.png')
        self.moose_13 = pygame.image.load('./Sprites/sprite_moose13.png')
        self.moose_14 = pygame.image.load('./Sprites/sprite_moose14.png')
        self.moose_15 = pygame.image.load('./Sprites/sprite_moose15.png')
        #Sprite List 
        self.moose = [self.moose_0,self.moose_1,self.moose_2,self.moose_3,\
                      self.moose_4,self.moose_5,self.moose_6,self.moose_7,\
                      self.moose_8,self.moose_9,self.moose_10,self.moose_11,\
                      self.moose_12,self.moose_13,self.moose_14,self.moose_15]
        #Sprite Frame Length
        self.moose_f = ((len(self.moose)) - 1)
        
        #Hockey Player
        self.hckplyr_0 = pygame.image.load('./Sprites/hockey00.png')
        #Sprite list
        self.hockeyPlayer = [self.hckplyr_0,self.hckplyr_0]
        #Sprite Frame Length
        self.hockeyPlayer_f = ((len(self.hockeyPlayer)) - 1)
        
        #Sword Thing
        self.axe_0 = pygame.image.load('./Sprites/axe.png')
        #Sprite List
        self.axe = [self.axe_0,self.axe_0]
        #Sprite Length
        self.axe_f = ((len(self.axe)) - 1)
        
        #background sprite
        self.background = pygame.image.load('./Sprites/winter_bg.png')
        
        #menu_bg
        self.menu_bg = pygame.image.load('./Sprites/menu_background.png')
        
        #heart sprites
        self.heart_1 = pygame.image.load('./Sprites/sprite_heart1.png')
        self.heart_2 = pygame.image.load('./Sprites/sprite_heart2.png')
        
        #Title
        self.title_0 = pygame.image.load('./Sprites/sprite_title0.png')
        self.title_1 = pygame.image.load('./Sprites/sprite_title1.png')
        self.title_2 = pygame.image.load('./Sprites/sprite_title2.png')
        self.title_3 = pygame.image.load('./Sprites/sprite_title3.png')
        #title array
        self.title = [self.title_0,self.title_1,self.title_2,self.title_3]
        self.title_f = ((len(self.title)) - 1)
        
        #Arrow key image
        self.keys = pygame.image.load('./Sprites/keys.png')
        #Animates given array
    def animate(self, sprite, entity, game_frames,direction):
        self.flag = False
        self.sprite_frames = game_frames
        
        #Allows choice of sprite
        if sprite == "LumberJack":
            self.frames = self.lumber_f
            self.sprite = self.lumber
            self.width = 50
            self.height = 70
        if sprite == "Beaver":
            self.frames = self.beaver_f
            self.sprite = self.beaver
            self.width = 100
            self.height = 40
        if sprite == "coffee":
            self.frames = self.flyingCoffee_f
            self.sprite = self.flyingCoffee
            self.width = 55
            self.height = 40
        if sprite == "pancake":
            self.frames = self.pancake_f
            self.sprite = self.pancake
            self.width = 50
            self.height = 50
        if sprite == "hockey":
            self.frames = self.hockeyPlayer_f
            self.sprite = self.hockeyPlayer
            self.width = 50
            self.height = 50
        if sprite == "puck":
            pass
        if sprite == "Axe":
            self.frames = self.axe_f
            self.sprite = self.axe
            self.width = 35
            self.height = 25
            if direction == False:
                entity.left += 5
            if direction == True:
                entity.left -= 5
        if sprite == "moose":
            self.frames = self.moose_f
            self.sprite = self.moose
            self.width = 85
            self.height = 85
        if sprite == "title":
            self.frames = self.title_f
            self.sprite = self.title
            self.width = 700
            self.height = 150
            
        #Tests If The Sprite Has More Frames To Run
        while self.flag == False:
            if self.sprite_frames >= self.frames:
                self.sprite_frames = (self.sprite_frames - self.frames)
            elif self.sprite_frames < self.frames:
                self.flag = True
        
        #Places Image in Variable
        self.image = (self.sprite[self.sprite_frames])
        
        #Resize Image
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        
        #Flips Image Depending on The Direction. TRUE == Right FALSE == Left
        if direction == False:
            self.image = pygame.transform.flip(self.image,True, False)
        
        #Displays image to screen
        self.windowSurface.blit(self.image, entity)
    
    def displayImage(self,image, entity):
        if image == "background":
            self.image = self.background
        if image == "Heartfull" :
            self.image = self.heart_1
        if image == "Heartnull":
            self.image = self.heart_2
        if image == "menu_bg":
            self.image = self.menu_bg
        if image == "keys":
            self.image = self.keys
        self.windowSurface.blit(self.image, entity)
