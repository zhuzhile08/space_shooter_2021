# import stuff
import pygame
import sys
import os
import random
import object as obj
import background as bj
import stage
from pygame.locals import*


# initialize pygame, setup window
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
window = pygame.display.set_mode((650, 980), 0, 32)

score = 0

# define some folders
imgFolder = os.path.join('data', 'img')
bgFolder = os.path.join(imgFolder, 'bg')
laserFolder = os.path.join(imgFolder, 'Lasers')
enemyFolder = os.path.join(imgFolder, 'Enemies')
kenFont = pygame.font.Font(os.path.join('data', 'kenvector_future_thin.ttf'), 30)     # font

# textures and objects
playerBulletTexture = os.path.join(laserFolder, 'laserBlue16.png')
bgTexture = os.path.join(bgFolder, 'blue.png')
player = obj.Player(3, os.path.join(imgFolder, 'playerShip1_blue.png'), (325, 900), playerBulletTexture, 0)
meteor = obj.Meteor(1, os.path.join(enemyFolder, 'meteorBrown_big1.png'), (random.randrange(0, 650), 0, random.randrange(-5, 5), random.randrange(4, 8)), 0, 0)
meteor2 = obj.Meteor(1, os.path.join(enemyFolder, 'meteorGrey_big1.png'), (random.randrange(0, 650), -20, random.randrange(-5, 5), random.randrange(4, 8)), 0, 0)

# crate stages
stage1 = stage.Stage(player, 0, (meteor, meteor2), 'Stage 1', kenFont, bgTexture, score)

# main game loop
running = True

while running:

    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # update and draw stuff on the screen
    window.fill((0, 0, 0))

    # draw stage
    stage1.update(window)

    # score
    scoreFont = kenFont.render('Score: ' + str(score), True, (255, 255, 255))
    window.blit(scoreFont, (10, 5))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

# quit when game loop is exited  
pygame.quit()
sys.exit()

# PricklyBerry
