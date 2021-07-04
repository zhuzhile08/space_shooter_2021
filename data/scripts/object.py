import pygame
import random
""" Object class """


class Object(pygame.sprite.Sprite):
    def __init__(self, health, score, texture, startingPos, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.startingPos = startingPos

        # make a 'default' option for scale
        if self.scale == 0:
            self.sImage = pygame.image.load(texture).convert()
            scl = (self.sImage.get_width(), self.sImage.get_height())
            self.scale = scl
            self.image = pygame.transform.scale(self.sImage, self.scale)
        else:
            self.sImage = pygame.image.load(texture).convert()
            self.image = pygame.transform.scale(self.sImage, self.scale)

        # rest of the setup
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = startingPos[0]
        self.rect.centery = startingPos[1]
        self.health = health
        self.score = score
        self.speedX = 0
        self.speedY = 0
        # self.bullet = bullet, bullet

    def move(self):
        pass

    def collision(self):
        pass

    def destroy(self):
        self.kill()

    def update(self):
        pass


class Player(Object):
    # move
    def move(self):
        # reset speed
        self.speedX = 0
        self.speedY = 0

        event = pygame.key.get_pressed()
        if event[pygame.K_w]:
            self.speedY -= 6
        if event[pygame.K_s]:
            self.speedY += 6
        if event[pygame.K_a]:
            self.speedX -= 6
        if event[pygame.K_d]:
            self.speedX += 6

        # update the position of the player
        self.rect.x += self.speedX
        self.rect.y += self.speedY

    def screenWrap(self):
        if self.rect.right <= 0:
            self.rect.left = 649
        if self.rect.left >= 650:
            self.rect.right = 1
        if self.rect.bottom <= 0:
            self.rect.top = 979
        if self.rect.top >= 980:
            self.rect.bottom = 1

    # update
    def update(self):
        self.move()
        self.screenWrap()


class Background(Object):
    def move(self):
        self.speedX = 0
        self.speedY = 0
        if True:
            self.speedY += 5
        self.rect.y += self.speedY
        if self.rect.y >= 980:
            self.rect.y = -800

    def update(self):
        self.move()


class Bullet(Object):
    def destroy(self):
        if self.rect.bottom <= 0 or self.rect.top >= 980:
            self.kill()

    def move(self):
        if True:
            self.speedY -= 4.5
        self.rect.y += self.speedY
        self.destroy()

    def update(self):
        self.move()


class Meteor(Object):
    def destroy(self):
        if self.rect.top >= 980:
            self.kill()

    def move(self):
        self.rect.x += self.startingPos[2]
        self.rect.y += self.startingPos[3]
        self.destroy()

    def update(self):
        self.move()
