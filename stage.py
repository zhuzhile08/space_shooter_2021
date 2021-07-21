import pygame
import random
import settings
import background


class Stage:
    def __init__(self, player, boss, name, bgTexture, score, enemyDic):
        # setting up the sprite groups and textures
        self.objectGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.bulletGroup = pygame.sprite.Group()
        self.bgTexture = bgTexture
        self.player = player
        self.boss = boss
        self.name = name
        self.score = score
        self.enemyDic = enemyDic

        # set up backgrounds
        self.bg1 = background.Background(bgTexture, (650, 650), 0)
        self.bg2 = background.Background(bgTexture, (650, 650), 1)
        self.bg3 = background.Background(bgTexture, (650, 650), 2)
        self.objectGroup.add(self.bg1, self.bg2, self.bg3, self.player)

    def collisions(self):
        pass

    def spawnBoss(self):
        pass

    def end(self):
        pass

    def restart(self):
        pass

    def update(self, window):
        self.objectGroup.add(self.player.objectGroup)
        for i in range(len(self.enemyDic)):
            self.objectGroup.add(self.enemyDic[i])
        self.collisions()
        self.objectGroup.update()
        self.objectGroup.draw(window)

        # initialize and draw text on screen (score, player health, stage name)
        scoreFont = settings.kenFont.render('Score: ' + str(self.score), True, (255, 255, 255))
        healthFont = settings.kenFont.render('health: ' + str(self.player.health), True, (255, 255, 255))
        stageFont = settings.kenFont.render(self.name, True, (255, 255, 255))
        window.blit(stageFont, (10, 40))    # draw text
        window.blit(scoreFont, (10, 5))
        window.blit(healthFont, (480, 5))
