import pygame
import random
import threading
from pygame.locals import *


class Stage:
    def __init__(self, player, boss, enemies, backgounds, enemyTextures, name, font):
        self.objects = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = player
        self.boss = boss
        self.enemies = enemies
        self.enemyTextures = enemyTextures
        self.backgrounds = backgounds
        self.objects.add(self.backgrounds, self.boss, self.player)
        self.name = name
        self.font = font

    def spawnEnemies(self):
        enemy = random.choice(self.enemies)
        self.objects.add(enemy)
        self.enemies.add(enemy)

    def spawnBoss(self):
        pass

    def end(self):
        pass

    def restart(self):
        pass

    def update(self, window):
        if True:
            delay = random.randrange(0, 3)
            spawnEnemy = threading.Timer(delay, self.spawnEnemies)
            spawnEnemy.start()
        self.objects.draw(window)
        self.objects.update()
        # events
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.objects.add()
