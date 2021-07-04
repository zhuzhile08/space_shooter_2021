# import stuff
import pygame
import sys
import os
import random
import data.scripts.object as obj
import data.scripts.stage as stage
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
assetsFolder = os.path.join('data', 'Assets')
imgFolder = os.path.join(assetsFolder, 'img')
bgFolder = os.path.join(imgFolder, 'bg')
laserFolder = os.path.join(imgFolder, 'Lasers')
enemyFolder = os.path.join(imgFolder, 'Enemies')


# create the Groups and Sprites
objects = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

kenFont = pygame.font.Font(os.path.join(assetsFolder, 'kenvector_future_thin.ttf'), 30)     # font
player = obj.Player(3, score, os.path.join(imgFolder, 'playerShip1_blue.png'), (325, 890), 0)       # player
bg1 = obj.Background(0, score, os.path.join(bgFolder, 'black.png'), (325, 0), (650, 650))      # backgrounds
bg2 = obj.Background(0, score, os.path.join(bgFolder, 'black.png'), (325, 650), (650, 650))
bg3 = obj.Background(0, score, os.path.join(bgFolder, 'black.png'), (325, 1300), (650, 650))

objects.add(bg1, bg2, bg3, player)      # add sprites to normal objects group


# crate stages
# stage1 = stage.Stage()


# main game loop
running = True

while running:

    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                # spawn bullets
                playerBullet = obj.Bullet(0, score, os.path.join(laserFolder, 'laserBlue01.png'), (player.rect.centerx, player.rect.top + 3), 0)
                objects.add(playerBullet)
                bullets.add(playerBullet)

                meteor = obj.Meteor(1, score, os.path.join(enemyFolder, 'meteorBrown_big1.png'),(random.randrange(0, 650), -20, random.randrange(-5, 5), random.randrange(4, 8)), 0)
                objects.add(meteor)
                mobs.add(meteor)

    enemyShot = pygame.sprite.groupcollide(mobs, bullets, True, True)
    if enemyShot:
        score += 1

    # update and draw stuff on the screen
    window.fill((0, 0, 0))
    objects.draw(window)
    objects.update()

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
