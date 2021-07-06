import pygame
import random
import threading
import object
import background
from pygame.locals import *


class Stage:
    def __init__(self, player, boss, enemies, name, font, bgTexture, score):
        # setting up the groups
        self.objectGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.bulletGroup = pygame.sprite.Group()
        self.bgTexture = bgTexture
        self.player = player
        self.boss = boss
        self.enemies = enemies
        self.name = name
        self.font = font
        self.score = score

        # set up backgrounds
        self.bg1 = background.Background(bgTexture, (650, 650), 0)
        self.bg2 = background.Background(bgTexture, (650, 650), 1)
        self.bg3 = background.Background(bgTexture, (650, 650), 2)
        self.objectGroup.add(self.bg1, self.bg2, self.bg3, self.player)

    def spawnEnemies(self):
        enemy = random.choice(self.enemies)
        self.objectGroup.add(enemy)
        self.enemyGroup.add(enemy)

    def collisions(self):
        bulletEnemyCollide = pygame.sprite.groupcollide(self.enemyGroup, self.player.bulletGroup, True, True)
        if bulletEnemyCollide:
            self.score += 50

    def spawnBoss(self):
        pass

    def end(self):
        pass

    def restart(self):
        pass

    def update(self, window):
        self.collisions()
        self.spawnEnemies()
        self.objectGroup.add(self.player.objectGroup)
        self.objectGroup.update()
        self.objectGroup.draw(window)
