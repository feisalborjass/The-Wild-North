import pygame, sys, random, math

from collision import doRectsOverlap, isPointInsideRect
from utilities import Center, terminate, render, newEnemyPerTick, trueOrFalse
from colours import BLACK, GREEN, WHITE, RED, BLUE, NAVY, snow, sky
from fonts import font
from base_character import Character
from entities import Enemy, Weapon, FlyingEnemy, HockeyPlayer, Pancake, Null
from sprites import Animation
from scoring import PointSystem

#set up screen
display_width = 800
display_height  = 600
windowSurface = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Wild North')

#set up center object and initialize the clock
center = Center(display_width, display_height)
clock = pygame.time.Clock()

#build the player, weapon and ground
player = Character(center.x - 30, center.y, 50, 70, display_width, windowSurface)
sword = Weapon(player.x + player.width, player.y, 35, 25, display_width, windowSurface)
ground = pygame.Rect(0, 400, 800, 200)
rectGround = (0, 400, 800, 200)

#set up the enemies - initialize base size and set up the list
enemySize = 35
enemies = []

#initialize a variable that will represent the y position of the ground
enemyGroundPosY = display_height - 199 - enemySize

#create instance of beaver, coffee, and hockey player enemies
enemy = Enemy(random.randint(0, display_width - enemySize), display_height, enemySize, enemySize, display_width, windowSurface)
flyEnemy = FlyingEnemy(random.randint(0, display_width - enemySize), 0, enemySize, enemySize, display_width, windowSurface)
hockeyEnemy = HockeyPlayer(random.randint(1, 2), enemyGroundPosY - 15, enemySize, enemySize, display_width, windowSurface)
pancakeEnemy = Pancake(random.randint(0, display_width - enemySize), display_height, enemySize, enemySize, display_width, windowSurface)

#append each type of enemy into the main enemy list
enemies.append(enemy)
enemies.append(flyEnemy)
enemies.append(hockeyEnemy)
enemies.append(pancakeEnemy)

#set up movement variables
moveLeft = False
moveRight = True
jump = False

#these variables hold the number of ticks it will take to spawn a new type of enemy
numTicksPerBaseEnemy = 150
numTicksPerFlyingEnemy = 250
numTicksPerHockeyEnemy = 400
numTicksPerPancakeEnemy = 300

#positions of hearts
heart_box_1 = pygame.Rect(575,25,0,0)
heart_box_2 = pygame.Rect(650,25,0,0)
heart_box_3 = pygame.Rect(725,25,0,0)

#tracks difficulty level of the player
currentLevel = 1
print('current level: 1')

#miscellaneous counter variables used in the game loop
main_counter = 0
tick_counter = 0
tick_counter2 = 0
tick_counter3 = 0
tick_counter4 = 0
tick_counter5 = 0

corner = pygame.Rect(0, 100, 0, 0)

#set up the sky
rectSky = (0,0,800,100)

#set up hit variables
invincibilityFrames = 0
invulnerable = 60
hit = False

playerScore = PointSystem(windowSurface)

#set up animation - initialize the animation class and game frames
animation = Animation(windowSurface)
game_frames = 0

while True:
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
        
        #if player's sword intersects with an enemy (except puck), remove the enemy and append a new base enemy
        if doRectsOverlap(sword.rect, enemies[i].rect) and enemies[i].rect.top <= enemyGroundPosY \
        and invincibilityFrames <= 10 and enemies[i].id != 'puck' and enemies[i].id != 'null':
            
            playerScore.addToScore(enemies[i].id)
            
            enemies.remove(enemies[i])
            nullEnemy = Null(0, 0, 1, 1, display_width, windowSurface)
            enemies.append(nullEnemy)
            
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

    #difficulty progression - every 800 ticks, increase frequency of enemy spawn rate
    if main_counter == 400 and numTicksPerBaseEnemy >= 50 and numTicksPerFlyingEnemy >= 150 and \
    numTicksPerHockeyEnemy >= 300 and numTicksPerPancakeEnemy >= 200:
    
        currentLevel += 1
        
        if currentLevel < 12:
            print('difficulty increased: level ' + str(currentLevel))
        if currentLevel == 12:
            print('difficulty increased: level 12 (MAX LEVEL)')
            
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
    
    #append a new pancake enemy every 180 ticks
    pancakeEnemy = Pancake(random.randint(0, display_width - enemySize), display_height, enemySize, enemySize, display_width, windowSurface)
    tick_counter5 = newEnemyPerTick(pancakeEnemy, enemies, tick_counter5, numTicksPerPancakeEnemy)
    
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
        
    #Animate Character 
    #If hit, takes away weapon
    if hit == False:
        animation.animate("Axe", sword.rect, game_frames, player.direction)
        animation.animate("LumberJack", player.rect, game_frames, player.direction)
        
    #If hit, Flashes character to  symbolize inviciblity
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
    
    playerScore.printScore()
    playerScore.printHighScore()
    
    if player.health == 3:
        animation.displayImage("Heartfull",heart_box_1)
        animation.displayImage("Heartfull",heart_box_2)
        animation.displayImage("Heartfull",heart_box_3)
    if player.health == 2:
        animation.displayImage("Heartfull",heart_box_1)
        animation.displayImage("Heartfull",heart_box_2)
        animation.displayImage("Heartnull",heart_box_3)
    if player.health == 1:
        animation.displayImage("Heartfull",heart_box_1)
        animation.displayImage("Heartnull",heart_box_2)
        animation.displayImage("Heartnull",heart_box_3)
    
    
    #If player is 0, bring end game
    if player.health == 0:
        screen = 2
        run = False
        playerScore.setHi_score()
        
    #draw the enemies on the screen. TAKE THIS OUT WHEN HADNING IN GAME. TO CHECK HITBOXES
    #for i in range(len(enemies)):
        #pygame.draw.rect(windowSurface, GREEN, enemies[i])    

    #update the display
    pygame.display.update()
    clock.tick(40)
