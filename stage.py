import pygame
import random
import object
import settings
import background


class Stage:
    def __init__(self, playerTextures, boss, name, bgTexture, score, enemyList):
        # setting up the sprite groups
        self.objectGroup = pygame.sprite.Group()
        self.enemyList = enemyList
        self.bulletList = []

        # some textures
        self.bgTexture = bgTexture
        self.playerTextures = playerTextures
        self.boss = boss

        self.name = name    # name of the stage
        self.score = score  # score

        # set up the sprites
        self.bg1 = background.Background(bgTexture, (650, 650), 0)  # backgrounds that loop on the stage
        self.bg2 = background.Background(bgTexture, (650, 650), 1)
        self.bg3 = background.Background(bgTexture, (650, 650), 2)
        self.player = object.Player(3, self.playerTextures[0], (325, 900), self.playerTextures[1], 0, 0)    # the player

        # add the required sprites of a stage to the object group
        self.objectGroup.add(self.bg1, self.bg2, self.bg3, self.player)

    def collisions(self):
        for enemy in self.enemyList:
            if pygame.sprite.spritecollideany(enemy, self.player.bulletGroup) is not None:
                enemy.currentHealth -= 1
                enemy.collision(self.player.bulletGroup, True)
            if enemy.currentHealth <= 0 and enemy.rect.top == 1000:
                self.score += enemy.score

    def spawnBoss(self):
        pass

    def end(self):
        pass

    def restart(self):
        pass

    def update(self, window):
        self.objectGroup.add(self.player.objectGroup)
        for enemy in self.enemyList:
            self.objectGroup.add(enemy)
        self.collisions()
        self.objectGroup.update()
        self.objectGroup.draw(window)

        # initialize and draw text on screen (score, player health, stage name)
        scoreFont = settings.kenFont.render('Score: ' + str(self.score), True, (255, 255, 255))
        healthFont = settings.kenFont.render('health: ' + str(self.player.health), True, (255, 255, 255))
        stageFont = settings.kenFont.render(self.name, True, (255, 255, 255))
        window.blit(stageFont, (10, 40))  # draw text
        window.blit(scoreFont, (10, 5))
        window.blit(healthFont, (480, 5))
