# import stuff
import pygame
import sys
import os
import settings
import random
import object as obj
import background as bj
import stage
from pygame.locals import*


# initialize pygame, setup window
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
window = pygame.display.set_mode((650, 980), 0, 32)

score = 0

# textures and objects
playerBulletTexture = os.path.join(settings.laserFolder, 'laserBlue16.png')
bgTexture = os.path.join(settings.bgFolder, 'black.png')
player = obj.Player(3, os.path.join(settings.imgFolder, 'playerShip1_blue.png'), (325, 900), playerBulletTexture, 0)


# enemy dictionaries for each stage
stg1EnemyDic = (obj.Meteor(1, os.path.join(settings.enemyFolder, 'meteorBrown1.png'), (random.randrange(0, 650), 0, random.randrange(-5, 5), random.randrange(4, 8)), 0, 0),
                obj.Meteor(1, os.path.join(settings.enemyFolder, 'meteorBrown2.png'), (random.randrange(0, 650), 0, random.randrange(-5, 5), random.randrange(4, 8)), 0, 0),
                obj.Meteor(1, os.path.join(settings.enemyFolder, 'meteorGrey1.png'), (random.randrange(0, 650), -20, random.randrange(-5, 5), random.randrange(4, 8)), 0, 0),
                obj.Meteor(1, os.path.join(settings.enemyFolder, 'ufoGrey.png'), (random.randrange(0, 650), -20, random.randrange(-5, 5), random.randrange(4, 8)), 0, 0))

# crate stages
stage1 = stage.Stage(player, 0, 'Stage 1', bgTexture, score, stg1EnemyDic)

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

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

# quit when game loop is exited  
pygame.quit()
sys.exit()

# PricklyBerry
