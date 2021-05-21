import pygame, random, sys

from pygame.locals import *
from collision import doRectsOverlap, isPointInsideRect
from utilities import Center, terminate, render, newEnemyPerTick, trueOrFalse
from colours import BLUE,RED,GREEN,snow,sky, BLACK,LIGHTBLACK, BLACK_2,LIGHTBLACK_2,WHITE, DARKRED,DARKBLUE,DARKGREEN,BROWN, DARKBROWN
#from fonts import basicFont
from base_character import Character
from entities import Enemy, Weapon, FlyingEnemy, HockeyPlayer, Pancake, Null, Moose
from sprites import Animation
from scoring import PointSystem

#creates a base class for all screens that are not the opening menu or the game itself, i.e death screen, help screen, and credits screen
class Window(object):
    #creates important variables like font sizes for text, the width and height of the screen, sprite images of the enemies etc.
    def __init__(self, input_width, input_height, new_colour, basicFont, input_x, input_y):
        self.font = basicFont
        self.small_font = pygame.font.SysFont(None, 40)
        self.smaller_font = pygame.font.SysFont(None, 30)
        self.smallest_font = pygame.font.SysFont(None, 18)
        self.big_font = pygame.font.SysFont(None, 120)
        self.tiny_font = pygame.font.SysFont(None, 20)
        self.x = input_x
        self.y = input_y
        self.width = input_width - 100
        self.height = input_height - 100
        self.colour = new_colour
        self.lumber = pygame.transform.scale(pygame.image.load('./Sprites/lumber_00.png'), (75, 105))
        self.beaver = pygame.transform.scale(pygame.image.load('./Sprites/sprite_beaver00.png'), (87, 39))
        self.coffee = pygame.transform.scale(pygame.image.load('./Sprites/sprite_flyingCoffeeCup00.png'), (114, 63))
        self.hockey = pygame.transform.scale(pygame.image.load('./Sprites/hockey00.png'), (80, 72))
        self.pancake = pygame.transform.scale(pygame.image.load('./Sprites/sprite_pancakeF.png'), (93, 63))
        self.moose = pygame.transform.scale(pygame.image.load('./Sprites/sprite_moose00.png'), (86, 104))
        self.base_rect = pygame.Rect(170, 140, 200, 200)
        self.base_rect2 = pygame.Rect(70, 405, 200, 200)
        self.base_rect3 = pygame.Rect(90, 290, 200, 200)
        self.base_rect4 = pygame.Rect(210, 375, 200, 200)
        self.base_rect5 = pygame.Rect(225, 290, 200, 200)
        self.base_rect6 = pygame.Rect(70, 450, 200, 200)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    #Makes a function that draws the window repeatedly
    def draw(self):
        pygame.draw.rect(windowSurface, self.colour, (self.x, self.y, self.width, self.height))
    #Makes a function that updates the window's image
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    #Draws the text for the window, this text is specifically for the help screen
    def drawText(self):
        windowSurface.blit(self.font.render('HELP MENU', True, (255, 255, 255)), (300, 90))
        windowSurface.blit(self.small_font.render('This is your guy', True, (255, 255, 255)), (380, 180))
        windowSurface.blit(self.smaller_font.render('+ 5 pts - Walks', True, (0, 0, 0)), (60, 380))
        windowSurface.blit(self.smaller_font.render('+ 15 pts - Flies', True, (0, 0, 0)), (60, 270))
        windowSurface.blit(self.smaller_font.render('+ 15 pts - Jumps', True, (0, 0, 0)), (210, 270))
        windowSurface.blit(self.smallest_font.render('+ 10 pts - Shoots', True, (0, 0, 0)), (280, 380))
        windowSurface.blit(self.smallest_font.render('invincible puck', True, (0, 0, 0)), (295, 390))
        windowSurface.blit(self.smallest_font.render('+ 20 pts - Runs across', True, (0, 0, 0)), (180, 470))
        windowSurface.blit(self.smallest_font.render('screen, you can only kill', True, (0, 0, 0)), (180, 480))
        windowSurface.blit(self.smallest_font.render("it when its not facing you", True, (0, 0, 0)), (180, 490))
        windowSurface.blit(self.smallest_font.render("and is not moving", True, (0, 0, 0)), (180, 500))
        windowSurface.blit(self.small_font.render('These are the enemies', True, (255, 255, 255)), (380, 260))
        windowSurface.blit(self.small_font.render('that you must defeat!', True, (255, 255, 255)), (390, 290))
        windowSurface.blit(self.small_font.render('Defeat them and survive', True, (255, 255, 255)), (380, 370))
        windowSurface.blit(self.small_font.render('as long as possible!', True, (255, 255, 255)), (380, 400))
        windowSurface.blit(self.small_font.render('Get the new high score!', True, (255, 255, 255)), (380, 460))
    #Draws the enemies onto the help screen
    def drawGuys(self):
        windowSurface.blit(self.lumber, self.base_rect)
        windowSurface.blit(self.beaver, self.base_rect2)
        windowSurface.blit(self.coffee, self.base_rect3)
        windowSurface.blit(self.hockey, self.base_rect4)
        windowSurface.blit(self.pancake, self.base_rect5)
        windowSurface.blit(self.moose, self.base_rect6)
    #Makes a function to leave the menu
    def leaveMenu(self):
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    return True
        return False

#Creates a subclass of Window, to overide the text function
class CreditWindow(Window):
    #Overides the drawText function of the original class, since it's text changes for the Credit scrreen
    def drawText(self):
        windowSurface.blit(self.font.render('CREDITS', True, (255, 255, 255)), (320, 100))
        windowSurface.blit(self.font.render('Lumber Jack - by DJ', True, (255, 255, 255)), (240, 150))
        windowSurface.blit(self.font.render('Background - by Enrico', True, (255, 255, 255)), (230, 200))
        windowSurface.blit(self.font.render('Beaver - by Andrew', True, (255, 255, 255)), (240, 250))
        windowSurface.blit(self.font.render('Coffee Cup - by Andrew', True, (255, 255, 255)), (230, 300))
        windowSurface.blit(self.font.render('Hockey Player - by Andrew', True, (255, 255, 255)), (200, 350))
        windowSurface.blit(self.font.render('Pancake - by Andrew', True, (255, 255, 255)), (240, 400))
        windowSurface.blit(self.font.render('Moose - by Andrew', True, (255, 255, 255)), (250, 450))
        windowSurface.blit(self.font.render('Title - by Andrew', True, (255, 255, 255)), (260, 500))

#Creates a subclass of Window, to overide the text function
class DeathWindow(Window):
    #Overides the drawText function of the original class, since it's text changes for the Death screen
    def drawText(self):
        windowSurface.blit(self.big_font.render('You are Dead', True, (0, 0, 0)), (150, 80))
        windowSurface.blit(self.tiny_font.render('(Sorry...)', True, (0, 0, 0)), (380, 180))
        playerScore.printHighScore((282,220),RED)

#creates a class that will allow for access of center x and y values
class Center():
    def __init__(self, display_width, display_height):
        self.x = display_width / 2
        self.y = display_height / 2
        self.center = (display_width, display_height)

#Creates a class for all the clickable buttons in this game
class Button():
    #Intialises a bunch of variables for the buttons like it's colour, x coordinate, y coordinate, and the rectangular button itself
    def __init__(self, x_cord, y_cord, colour):
        self.small_font = pygame.font.SysFont(None, 30)
        self.width = 200
        self.height = 45
        self.x = x_cord
        self.y = y_cord
        self.colour = colour
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)
    #Draws the button onto the screen with it's colour
    def drawBox(self):
        pygame.draw.rect(windowSurface, self.colour, self.button)
    #Changes the background colour of the button, dependent on if the user's mouse is hovering over the button
    def changeColour(self, alt_colour, og_colour):
        if playerOnButton(self.button) == True:
            self.colour = alt_colour
        elif playerOnButton(self.button) == False:
            self.colour = og_colour
    #Changes the backgound colour of the text, dependent of if the mouse is hovering over the button, significantly longer than the previous function because the text needs to be rendered again with different variables
    def createText(self, base, alt_colour):
        if playerOnButton(self.button) == True:
            if self.colour == RED or self.colour == DARKRED:
                self.text = basicFont.render('START', True, base, alt_colour)
            elif self.colour == BLUE or self.colour == DARKBLUE:
                self.text = basicFont.render('HELP', True, base, alt_colour)
            elif self.colour == GREEN or self.colour == DARKGREEN:
                self.text = basicFont.render('QUIT', True, base, alt_colour)
            elif self.colour == BLACK or self.colour == LIGHTBLACK:
                self.text = basicFont.render('RETRY', True, base, alt_colour)
            elif self.colour == BLACK_2 or self.colour == LIGHTBLACK_2:
                self.text = self.small_font.render('RETURN TO MENU', True, base, alt_colour)
            elif self.colour == BROWN or self.colour == DARKBROWN:
                self.text = basicFont.render('CREDITS', True, base, alt_colour)
        elif playerOnButton(self.button) == False:
            if self.colour == RED:
                self.text = basicFont.render('START', True, base, self.colour)
            elif self.colour == BLUE:
                self.text = basicFont.render('HELP', True, base, self.colour)
            elif self.colour == GREEN:
                self.text = basicFont.render('QUIT', True, base, self.colour)
            elif self.colour == BLACK:
                self.text = basicFont.render('RETRY', True, base, self.colour)
            elif self.colour == BLACK_2:
                self.text = self.small_font.render('RETURN TO MENU', True, base, self.colour)
            elif self.colour == BROWN:
                self.text = basicFont.render('CREDITS', True, base, self.colour)
    #Draws the text of the button onto the screen
    def drawText(self, text_x, text_y):
        windowSurface.blit(self.text, (text_x, text_y))
    #Checks if the mouse is being pressed and if it is on a specific button
    def checkButtonPress(self, click):
        if click[0] == 1 and playerOnButton(self.button) == True:
            return True
        else:
            return False
    #Checks if the player is hovering over a button
    def playerOnButton(self):
        if self.button.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False

#Checks if the player is hovering over a button, different than the previous one since I don't know how to call one of a classes functions in itself
def playerOnButton(button):
    if button.collidepoint(pygame.mouse.get_pos()):
        return True
    return False
        
#creates a function that will terminate the program
def terminate():
    pygame.QUIT
    sys.exit()


#initialize pygame


pygame.init()

#Creates a couple flags which run the game, game runs the game loop, help_menu_flag runs the help screen, death_menu_flag runs the death screen and screen is a variable which decides if the player is in the game itself, the opening menu or exitting the game
game = True
help_menu_flag = True
death_menu_flag = True
screen = 0

# set up fonts
basicFont = pygame.font.SysFont(None, 48)

release = 0
release_list = []
#set up screen
display_width = 800
display_height = 600
windowSurface = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Wild North')

center = Center(display_width, display_height)

small_size = pygame.font.SysFont(None, 28)

#creates all the buttons
start_box = Button(center.x - 100, center.y - 80, RED)

help_box = Button(center.x - 100, center.y + 15, BLUE)

exit_box = Button(center.x - 100, center.y + 105, GREEN)

retry_box = Button(center.x - 100, center.y + 15, BLACK)

return_box = Button(center.x - 100, center.y + 150, BLACK)

#sets up the help screen, death screen, and credit screen
help_menu = Window(800, 600, BROWN, basicFont, 50, 50)

credit_menu = CreditWindow(1000, 800, BLACK, basicFont, 0, 0)

death_menu = DeathWindow(900, 700, RED, basicFont, 0, 0)

#Creates a specific rendered text which is for the credits screen and help screen, which tells the player to press ESC if they want to go back
text_leave = basicFont.render('Press ESC to back', True, BLACK, snow) #creates the text to leave the help menu

#add text to help menu
h_text = basicFont.render('HELP MENU', True, BROWN, WHITE)

#add credits button
credit_box = Button(center.x - 100, center.y +195, BROWN)

#initialize clock
clock = pygame.time.Clock()

playerScore = PointSystem(windowSurface)

#set up animation - initialize the animation class and game frames
animation = Animation(windowSurface)
game_frames = 0


corner = pygame.Rect(0, 100, 0, 0)
corner2 = pygame.Rect(0, 150, 0, 0)

#positions of hearts
heart_box_3 = pygame.Rect(575,25,0,0)
heart_box_2 = pygame.Rect(625,25,0,0)
heart_box_1 = pygame.Rect(675,25,0,0)
heart_box_0 = pygame.Rect(725,25,0,0)

#set up movement variables
moveLeft = False
moveRight = True
jump = False

#set up the sky
rectSky = (0,0,800,100)
#Set up Ground
rectGround = (0, 400, 800, 200)
ground = pygame.Rect(0, 400, 800, 200)

#these variables hold the number of ticks it will take to spawn a new type of enemy
numTicksPerBaseEnemy = 150
numTicksPerFlyingEnemy = 250
numTicksPerHockeyEnemy = 400
numTicksPerPancakeEnemy = 300
numTicksPerMooseEnemy = 400

#Text used beside arrow keys
jumptxt = small_size.render(('Jump'),True,(0, 0, 0),snow)
lefttxt = small_size.render(('Move Left'),True,(0, 0, 0),snow)
righttxt = small_size.render(('Move Right'),True,(0, 0, 0),snow)
#game loop
while game == True:
    #set up animation frames
    game_frames += 1
    if game_frames > 100:
        game_frames = 0
    #If statement where if screen is 0 then the opening menu runs
    if screen == 0:
        windowSurface.fill(snow) #Makes background the colour "snow"
        animation.displayImage('menu_bg', corner2)#Displays the title screen
        animation.animate('title',(47,25),game_frames, True) #Animates the title
        click = pygame.mouse.get_pressed() #Sees where the user pressed last

        #This whole box of code basically draws the box and changes the colour of it to a darker one if the user is hovering over it
        start_box.changeColour(DARKRED, RED)
        start_box.drawBox()
        start_box.createText(WHITE, DARKRED)
        start_box.drawText(center.x - 50, center.y - 70)
        help_box.changeColour(DARKBLUE, BLUE)
        help_box.drawBox()
        help_box.createText(WHITE, DARKBLUE)
        help_box.drawText(center.x - 40, center.y + 25)
        exit_box.changeColour(DARKGREEN, GREEN)
        exit_box.drawBox()
        exit_box.createText(WHITE, DARKGREEN)
        exit_box.drawText(center.x - 40, center.y + 115)
        credit_box.changeColour(DARKBROWN, BROWN)
        credit_box.drawBox()
        credit_box.createText(WHITE, DARKBROWN)
        credit_box.drawText(center.x - 75, center.y + 205)

        #Creates variables which shows if the user presses which button, if one is True then the user pressed that one
        start_press = start_box.checkButtonPress(click)
        help_press = help_box.checkButtonPress(click)
        exit_press = exit_box.checkButtonPress(click)
        credit_press = credit_box.checkButtonPress(click)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        #When start_press is True, then screen becomes 1, resulting in the actual game to run  
        if start_press == True:
            screen = 1

        #When credit_press is True, then the credit_flag becomes True resulting in the Credits screen to come up
        elif credit_press == True:
            credit_flag = True
            while credit_flag == True:

                #Draws the credits screen, updates it repeatedly, and draws the text for it
                credit_menu.draw()
                credit_menu.update()
                credit_menu.drawText()
                windowSurface.blit(text_leave, (0, 0))
                pygame.display.update()

                #Calls the function leaveMenu() which checks if the user pressed ESC or not, if they did then the user leaves and the flag turns off
                credit_checker = help_menu.leaveMenu()
                if credit_checker == True:
                    credit_flag = False
                else:
                    credit_flag = True

        #When help_press is True, then the help_menu_flag becomes True resulting in the help screen to pop up
        elif help_press == True:
            help_menu_flag = True
            while help_menu_flag == True:

                #Draws the help screen, updates it repeatedly, draws the text for it, and also draws the enemies onto it
                help_menu.draw()
                help_menu.update()
                help_menu.drawText()
                help_menu.drawGuys()
                windowSurface.blit(text_leave, (0, 0))
                pygame.display.update()

                #Calls the function leaveMenu() which checks if the user pressed ESC or not, if they did then the user leaves and the flag turns off
                checker = help_menu.leaveMenu()
                if checker == True:
                    help_menu_flag = False
                else:
                    help_menu_flag = True

        #When exit_press is True, terminate() is called and the game exits
        elif exit_press == True:
            terminate()

    #Screen becomes 1 when the user presses start, resulting in the game loop to occur
    elif screen == 1:
        ###########################GAME CODE########
        #DECLARE ALL GAME VARIABLES
        run = True
        
        #Reset player score to 0
        playerScore.score = 0
        
        #build the player, weapon and ground
        player = Character(center.x - 30, center.y, 50, 70, display_width, windowSurface)
        sword = Weapon(player.x + player.width, player.y, 35, 25, display_width, windowSurface)
        
        #set up the enemies - initialize base size and set up the list
        enemySize = 35
        enemies = []
        
        #initialize a variable that will represent the y position of the ground
        enemyGroundPosY = display_height - 199 - enemySize
        
        #create instance of beaver, coffee, and hockey player enemies
        enemy = Enemy(random.randint(0, display_width - enemySize), display_height, enemySize, enemySize, display_width, windowSurface)
        flyEnemy = FlyingEnemy(random.randint(0, display_width - enemySize), 0, enemySize, enemySize, display_width, windowSurface)
        hockeyEnemy = HockeyPlayer(random.randint(1, 2), enemyGroundPosY - 15, enemySize, enemySize, display_width, windowSurface)
        mooseEnemy = Moose(random.randint(1,2), -100, enemySize, enemySize, display_width, windowSurface)
        pancakeEnemy = Pancake(random.randint(0, display_width - enemySize), display_height, enemySize, enemySize, display_width, windowSurface)
        
        #append each type of enemy into the main enemy list
        enemies.append(enemy)
        enemies.append(flyEnemy)
        enemies.append(hockeyEnemy)
        enemies.append(mooseEnemy)
        enemies.append(pancakeEnemy)
        
        #tracks difficulty level of the player
        currentLevel = 1
        leveltext = small_size.render(('Difficulty Level: ' + str(currentLevel)),True,(0, 0, 0),sky)
        
        #miscellaneous counter variables used in the game loop
        main_counter = 0
        tick_counter = 0
        tick_counter2 = 0
        tick_counter3 = 0
        tick_counter4 = 0
        tick_counter5 = 0
        tick_counter6 = 0
        moose_counter = 0
        moose_counter_kill = 0
        
        #set up hit variables
        invincibilityFrames = 0
        invulnerable = 60
        hit = False
               
        
    
        
        while run == True:
            #set up animation frames
            game_frames += 1
            if game_frames > 100:
                game_frames = 0
                
            #test if the player is hit
            if hit == True and invincibilityFrames > 0:
                invincibilityFrames -= 1
            else:
                hit = False
                
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                
                if event.type == pygame.KEYDOWN:
                    #if player presses escape, end the program
                    if event.key == pygame.K_ESCAPE:
                        terminate()
                    
                    #if player presses up direction key, player is not on the ground
                    if event.key == pygame.K_UP:
                        player.onGround = False
                    
                    #if player presses left direction key, player is moving and facing left
                    if event.key == pygame.K_LEFT:
                        moveLeft = True
                        moveRight = False
                        player.direction = False
                        
                    #if player presses right direction key, player is moving and facing right
                    if event.key == pygame.K_RIGHT:
                        moveRight = True
                        moveLeft = False
                        player.direction = True 
              
            #move the player right                        #****************NOTE*******************
            if moveRight == True:                         #WHEN REFERRING TO DIRECTION, TRUE MEANS
                player.moveRight()                        #     RIGHT, AND FALSE MEANS LEFT      #
                
            #move the player left
            if moveLeft == True:
                player.moveLeft()
            
            #make the player jump 
            if player.onGround == False:
                player.jump()
            
            #update the player's rect values
            player.update()  
              
            #check if player and ground collide
            #if yes, stop jumping and reset velocity to 24
            if doRectsOverlap(player.rect, ground):
                player.onGround = True 
                player.velocityY = 24
            
            #contains all code that deals with all or individual enemies       
            for i in range(len(enemies)):
                
                #if player's sword intersects with an enemy (except puck and moose), remove the enemy and append a new base enemy
                if doRectsOverlap(sword.rect, enemies[i].rect) and enemies[i].rect.top <= enemyGroundPosY \
                and invincibilityFrames <= 10 and enemies[i].id != 'puck' and enemies[i].id != 'null' and enemies[i].id != 'moose':
                    
                    #Adds score to playerscore depending on what enemy was hit
                    playerScore.addToScore(enemies[i].id)
                    
                    enemies.remove(enemies[i])
                    nullEnemy = Null(0, 0, 1, 1, display_width, windowSurface)
                    enemies.append(nullEnemy)
                    
                #if player's sword intersects with moose only, remove the enemy and append a new base enemy
                if doRectsOverlap(sword.rect, enemies[i].rect) and enemies[i].rect.top <= enemyGroundPosY \
                and invincibilityFrames <= 0 and enemies[i].id == 'moose' and moose_counter_kill > 0 and moose_counter_kill <= 100:
                    
                    #Adds score to playerscore depending on what enemy was hit
                    playerScore.addToScore(enemies[i].id)
                    
                    enemies.remove(enemies[i])
                    enemy = Enemy(1000, 600, enemySize, enemySize, display_width, windowSurface)
                    enemies.append(enemy)
                    moose_counter_kill = 0
                    
                    
                #if player intersects with an enemy, subtract one health point from the player and initialize invincibility
                if doRectsOverlap(player.rect, enemies[i].rect) and invincibilityFrames <= 0 and enemies[i].id != 'null':
                    player.health -= 1
                    invincibilityFrames = invulnerable
                    hit = True
                
                #if enemy is a beaver
                if enemies[i].id == 'Beaver':
                    
                    #increases tick counter
                    enemies[i].counter += 1
                    
                    #reset tick counter and change enemy direction every 25 ticks
                    if enemies[i].counter == 25:
                        enemies[i].direction = trueOrFalse()
                        enemies[i].counter = 0 
                                       
                    if enemies[i].rect.top <= enemyGroundPosY:
                        if enemies[i].direction == True:
                            enemies[i].moveRight() 
                        if enemies[i].direction == False:
                            enemies[i].moveLeft() 
                            
                    if enemies[i].rect.top > enemyGroundPosY:
                        enemies[i].counter = 0
                        enemies[i].moveUp()
                            
                           
                    #if enemy hits left side of screen, move right                
                    if enemies[i].rect.left <= 0:
                        enemies[i].direction = True
                    #if enemy hits right side of screen, move left  
                    if enemies[i].rect.left >= display_width - enemySize:
                        enemies[i].direction = False
                        
                #if enemy is coffee            
                if enemies[i].id == 'coffee':
                    
                    enemies[i].fly()
                    enemies[i].appearFromTop()
                    
                    #if enemy hits left side of screen, move right                
                    if enemies[i].rect.left <= 0:
                        enemies[i].direction = True
                    #if enemy hits right side of screen, move left  
                    if enemies[i].rect.left >= display_width - enemySize:
                        enemies[i].direction = False
                        
                    if enemies[i].direction == True:
                        enemies[i].moveRight() 
                    if enemies[i].direction == False:
                        enemies[i].moveLeft() 
                    
                    if enemies[i].rect.top <= -100:
                        enemies.remove(enemies[i])   
                        nullEnemy = Null(0, 0, 1, 1, display_width, windowSurface)
                        enemies.append(nullEnemy)
                        tick_counter3 = 1    
                
                #if enemy is a hockey player
                if enemies[i].id == 'hockey':
                    
                    if enemies[i].counter >= 250:
                        enemies[i].timeToLeave = True
                    
                    if enemies[i].timeToLeave == False:
                        enemies[i].counter += 1
                        
                        #shoot a puck every 100 ticks
                        if enemies[i].counter % 100 == 0:
                            enemies[i].shootPuck(enemies)
                        
                        enemies[i].appearFromLeft()
                        enemies[i].appearFromRight()
                        
                    if enemies[i].timeToLeave == True:
                        if enemies[i].direction == True:
                            enemies[i].moveLeft()
                        if enemies[i].direction == False:
                            enemies[i].moveRight()
                        enemies[i].counter = 1
                        tick_counter4 = 1
                    
                    if enemies[i].rect.left <= -100 or enemies[i].rect.left >= display_width + 100:
                        enemies.remove(enemies[i])  
                        nullEnemy = Null(0, 0, 1, 1, display_width, windowSurface)
                        enemies.append(nullEnemy)
                        tick_counter4 = 1
                
                #if enemy is a hockey puck
                if enemies[i].id =='puck':
                    if enemies[i].direction == True:
                        enemies[i].moveRight()
                    if enemies[i].direction == False:
                        enemies[i].moveLeft()
                
                #if enemy is a moose
                if enemies[i].id == 'moose':
                    
                    #spawn moose from top
                    enemies[i].dropFromTop()
                    
                    #will run if the moose is one the ground
                    if enemies[i].rect.top == 320:
                        
                        enemies[i].counter += 1    
                        
                        if enemies[i].counter >= 100 and (moose_counter == 0 or moose_counter == 1 or moose_counter == 2):
                            
                            #moose will run across the screen
                            if enemies[i].direction == True and enemies[i].rect.left <= 700 and enemies[i].counter_stop == 100:
                                enemies[i].moveRight()
                            if enemies[i].direction == False and enemies[i].rect.left >= 0 and enemies[i].counter_stop == 100:
                                enemies[i].moveLeft()
                            
                            
                            if enemies[i].rect.left >= 700:
                                enemies[i].counter_stop += 1
                                moose_counter_kill += 1
                            if enemies[i].rect.left <= 1:
                                enemies[i].counter_stop += 1
                                moose_counter_kill += 1
                                
                        
                        #moose will face one direction for 100 ticks at one end of the screen, then will face the other direction
                        if enemies[i].counter_stop >= 200 and (moose_counter == 0 or moose_counter == 1 or moose_counter == 2):

                            if enemies[i].direction == True:
                                enemies[i].direction = False
                                enemies[i].counter = 0
                                moose_counter += 1
                                
                            elif enemies[i].direction == False:
                                enemies[i].counter = 0
                                enemies[i].direction = True
                                moose_counter += 1
                                
                            enemies[i].counter_stop = 100
                            enemies[i].counter = 0
                            moose_counter_kill = 0
                            
                            tick_counter5 = 1
                            
                        
                        #after three sprints across the screen, moose will disappear
                        if moose_counter == 3:
                            if enemies[i].direction == True:
                                enemies[i].disappearFromLeft()
                            if enemies[i].direction == False:
                                enemies[i].disappearFromRight()
                        
                        
                        if enemies[i].rect.left <= -100 or enemies[i].rect.left >= display_width + 100:
                            enemies.remove(enemies[i]) 
                            mooseEnemy = Moose(random.randint(1,2), -100, enemySize, enemySize, display_width, windowSurface)
                            enemies.append(mooseEnemy)
                            moose_counter = 0
                            enemies[i].counter_stop = 100
                            enemies[i].counter = 0
                            moose_counter_kill = 0
                
                #if enemy is a pancake
                if enemies[i].id == 'pancake':
                    
                    #check if player and ground collide
                    #if yes, stop jumping and reset velocity to 24
                    if doRectsOverlap(enemies[i].rect, ground) and enemies[i].rect.top == enemyGroundPosY - 1:
                        enemies[i].onGround = True
                        enemies[i].reachedSurface = True 
                        enemies[i].velocityY = 13
                        enemies[i].direction = trueOrFalse()
                        
                    
                    if enemies[i].rect.top > enemyGroundPosY:
                        if enemies[i].reachedSurface == False:
                            enemies[i].moveUp()
                        
                    #if enemy hits left side of screen, move right                
                    if enemies[i].rect.left <= 0:
                        enemies[i].direction = True
                    #if enemy hits right side of screen, move left  
                    if enemies[i].rect.left >= display_width - enemies[i].size:
                        enemies[i].direction = False   
                    
                    if enemies[i].rect.top <= enemyGroundPosY:
                        if enemies[i].direction == True:
                            enemies[i].bounce() 
                            enemies[i].moveRight()
                        if enemies[i].direction == False:
                            enemies[i].bounce() 
                            enemies[i].moveLeft()
                    
                    enemies[i].update()
                
            
            #miscellaneous tick counter
            main_counter += 1  
            tick_counter2 += 1
            tick_counter3 += 1
            tick_counter4 += 1
            tick_counter5 += 1
            tick_counter6 += 1
        
            #difficulty progression - every 800 ticks, increase frequency of enemy spawn rate
            if main_counter == 400 and numTicksPerBaseEnemy >= 50 and numTicksPerFlyingEnemy >= 150 and \
            numTicksPerHockeyEnemy >= 300 and numTicksPerPancakeEnemy >= 200:
            
                currentLevel += 1
                
                if currentLevel < 12:
                    leveltext = small_size.render(('Difficulty Level: ' + str(currentLevel)),True,(0, 0, 0),sky)
                    #print('difficulty increased: level ' + str(currentLevel))
                if currentLevel == 12:
                    leveltext = small_size.render(('Difficulty Level: 12 (MAX LEVEL)'),True,(0, 0, 0),sky)
                    
                    #print('difficulty increased: level 12 (MAX LEVEL)')
                    
                numTicksPerBaseEnemy -= 10
                numTicksPerFlyingEnemy -= 10
                numTicksPerHockeyEnemy -= 10
                numTicksPerPancakeEnemy -= 10
                main_counter = 1   
            
            #create a new instance of the base enemy
            enemy = Enemy(random.randint(0, display_width - enemySize), display_height, enemySize, enemySize, display_width, windowSurface)
            #append a new base enemy every 90 ticks
            tick_counter2 = newEnemyPerTick(enemy, enemies, tick_counter2, numTicksPerBaseEnemy)
            
            #create a new instance of flyEnemy
            flyEnemy = FlyingEnemy(random.randint(0, display_width - enemySize), -enemySize, enemySize, enemySize, display_width, windowSurface)
            #append a new flying enemy every 250 ticks
            tick_counter3 = newEnemyPerTick(flyEnemy, enemies, tick_counter3, numTicksPerFlyingEnemy)
            
            #append a new hockey enemy every 200 ticks
            hockeyEnemy = HockeyPlayer(random.randint(1, 2), enemyGroundPosY - 15, enemySize, enemySize, display_width, windowSurface)
            tick_counter4 = newEnemyPerTick(hockeyEnemy, enemies, tick_counter4, numTicksPerHockeyEnemy)
            
            #append a new moose enemy every 200 ticks
            mooseEnemy = Moose(random.randint(1,2), -100, enemySize, enemySize, display_width, windowSurface)
            tick_counter5 = newEnemyPerTick(mooseEnemy, enemies, tick_counter5, numTicksPerMooseEnemy)
            
            #append a new pancake enemy every 180 ticks
            pancakeEnemy = Pancake(random.randint(0, display_width - enemySize), display_height, enemySize, enemySize, display_width, windowSurface)
            tick_counter6 = newEnemyPerTick(pancakeEnemy, enemies, tick_counter6, numTicksPerPancakeEnemy)
            
            #update the sword's values to follow the player
            if player.direction == True:
                sword.x = player.x + player.width
                sword.y = player.y + 20
                
            if player.direction == False:
                sword.x = player.x - sword.width
                sword.y = player.y + 20
             
            #fill the window surface
            animation.displayImage("background", corner)
            
            #render the ground
            render(windowSurface, snow, rectGround)
            
            #Render arrow keys on ground, block out down arrow key
            animation.displayImage("keys",(150,425))
            render(windowSurface, snow, (225,501,67,67))
            #Print use of arrow keys
            windowSurface.blit(jumptxt,(232,500))
            windowSurface.blit(lefttxt,(50,550))
            windowSurface.blit(righttxt,(370,550))
            
            #Animate Character 
            #If hit, takes away weapon
            if hit == False:
                animation.animate("Axe", sword.rect, game_frames, player.direction)
                animation.animate("LumberJack", player.rect, game_frames, player.direction)
                
            #If hit, Flashes character to  symbolize invincibility
            if hit == True:
                if (invincibilityFrames % 4) == 2:
                    animation.animate("LumberJack", player.rect, game_frames, player.direction)
                if (10 % (1 + invincibilityFrames)) < 10:
                    animation.animate("Axe", sword.rect, game_frames, player.direction)
            
            #update player and sword rect values
            player.update()
            sword.update()
            
            #ANIMATES ALL ENEMIES
            for i in range(0,(len(enemies))):
                if enemies[i].id != 'puck' and enemies[i].id != 'null':
                    animation.animate(enemies[i].id, enemies[i].rect, game_frames, enemies[i].direction)
                
            #draw the enemies on the screen. TAKE THIS OUT WHEN HADNING IN GAME. TO CHECK HITBOXES
            for i in range(len(enemies)):
                if enemies[i].id == 'puck':
                    pygame.draw.rect(windowSurface, BLACK, enemies[i]) 
            
            #render the sky/top
            render(windowSurface, sky, rectSky)
            
            #Print player score, high score and current difficulty level
            playerScore.printScore()
            playerScore.printHighScore((300,20),sky)
            windowSurface.blit(leveltext,(20,60))
            
            
            #Displays hearts corresponding to how much health you have left
            if player.health == 4:
                animation.displayImage("Heartfull",heart_box_0)
                animation.displayImage("Heartfull",heart_box_1)
                animation.displayImage("Heartfull",heart_box_2)
                animation.displayImage("Heartfull",heart_box_3)
            if player.health == 3:
                animation.displayImage("Heartfull",heart_box_0)
                animation.displayImage("Heartfull",heart_box_1)
                animation.displayImage("Heartfull",heart_box_2)
                animation.displayImage("Heartnull",heart_box_3)
            if player.health == 2:
                animation.displayImage("Heartfull",heart_box_0)
                animation.displayImage("Heartfull",heart_box_1)
                animation.displayImage("Heartnull",heart_box_2)
                animation.displayImage("Heartnull",heart_box_3)
            if player.health == 1:
                animation.displayImage("Heartfull",heart_box_0)
                animation.displayImage("Heartnull",heart_box_1)
                animation.displayImage("Heartnull",heart_box_2)
                animation.displayImage("Heartnull",heart_box_3)
            
            
            #If player is 0, bring end game, bring to death screen
            if player.health == 0:
                screen = 2
                run = False
                playerScore.setHi_score() #Save high score
                
            #draw the enemies on the screen. TAKE THIS OUT WHEN HADNING IN GAME. TO CHECK HITBOXES
            #for i in range(len(enemies)):
                #pygame.draw.rect(windowSurface, GREEN, enemies[i])    
        
            #update the display
            pygame.display.update()
            clock.tick(40)

        
        
    #Screen becomes 2 if the player dies in the game loop, resulting in the death screen
    elif screen == 2:
        death_flag = True
        while death_flag == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
            
            #Basically a mini version of the opening menu but with 2 buttons instead of 4
            click = pygame.mouse.get_pressed()
            death_menu.draw()
            death_menu.drawText()

            #Draws the boxes, changes it's colour when the player is hovering over it
            retry_box.changeColour(LIGHTBLACK, BLACK)
            retry_box.drawBox()
            retry_box.createText(WHITE, LIGHTBLACK)
            retry_box.drawText(center.x - 60, center.y + 25)
            return_box.changeColour(LIGHTBLACK_2, BLACK_2)
            return_box.drawBox()
            return_box.createText(WHITE, LIGHTBLACK_2)
            return_box.drawText(center.x - 90, center.y + 165)
            death_menu.update()
            pygame.display.update()

            #Checks to see if the user pressed on the retry button or the return to menu button
            retry_press = retry_box.checkButtonPress(click)
            return_press = return_box.checkButtonPress(click)
            
            
            #If the user presses the retry button, the death flag becomes False, the death screen leaves, screen becomes 1, and the game loop begins anew
            if retry_press == True:
                death_flag = False
                screen = 1

            #If the user presses the return to menu button, the death flag becomes False, the death screen leaves, screen becomes 0, and the opening menu opens
            elif return_press == True:
                death_flag = False
                screen = 0
    #update the display
    pygame.display.update()
    clock.tick(40)

