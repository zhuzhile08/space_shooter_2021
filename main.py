# import stuff
import pygame
import sys
import os
import settings
import random
import object as obj
import stage
from pygame.locals import*


# initialize pygame, setup window
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
window = pygame.display.set_mode((650, 980))

score = 0

# textures and objects
playerBulletTextures = [os.path.join(settings.laserFolder, 'laserBlue16.png'), os.path.join(settings.effectsFolder, 'fire16.png')]
playerTexture = os.path.join(settings.imgFolder, 'playerShip1_blue.png')
bgTexture = os.path.join(settings.bgFolder, 'black.png')

# enemy dictionaries for each stage
stg1EnemyDic = settings.generateEnemyDictionaryStage1()

stg2EnemyDic = []
stg3EnemyDic = []
stg4EnemyDic = []
stg5EnemyDic = []

# crate stages
stage1 = stage.Stage([playerTexture, playerBulletTextures], 0, 'Stage 1', bgTexture, score, stg1EnemyDic)

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
