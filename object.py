import pygame
import random
import bullets


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, health, currentHealth, texture, position):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.currentHealth = currentHealth
        self.position = position
        self.sImage = pygame.image.load(texture).convert()

    def update(self):
        scale = (self.currentHealth / self.health, self.sImage.get_height())
        self.image = pygame.transform.scale(self.sImage, scale)


class Movables(pygame.sprite.Sprite):
    def __init__(self, health, texture, startingPos, bulletTexture, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.startingPos = startingPos

        # make a 'default' option for scale
        if self.scale == 0:
            self.sImage = pygame.image.load(texture).convert()
            scl = (self.sImage.get_width(), self.sImage.get_height())
            self.image = pygame.transform.scale(self.sImage, scl)
        else:
            self.sImage = pygame.image.load(texture).convert()
            self.image = pygame.transform.scale(self.sImage, self.scale)

        # setup image
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = startingPos[0]
        self.rect.centery = startingPos[1]
        self.health = health
        self.speedX = 0
        self.speedY = 0
        self.cooldownTimer = 0
        self.currentHealth = self.health

        # setup bullet
        self.bulletGroup = pygame.sprite.Group()
        self.objectGroup = pygame.sprite.Group()
        self.bulletTexture = bulletTexture
        # self.bullet = bullet, bullet

    def move(self):
        pass

    def collision(self):
        self.currentHealth -= 1

    def cooldown(self):
        if self.cooldownTimer >= 10:
            self.cooldownTimer = 0
        elif self.cooldownTimer > 0:
            self.cooldownTimer += 1

    def shoot(self):
        bullet = bullets.Bullet(self.bulletTexture, (self.rect.centerx, self.rect.top - 45), 40)
        self.bulletGroup.add(bullet)
        self.objectGroup.add(bullet)

    def update(self):
        self.move()
        if self.currentHealth <= 1:
            self.kill()


class Player(Movables):
    # move
    def move(self):
        self.cooldown()
        # reset speed
        self.speedX = 0
        self.speedY = 0

        # detect input
        event = pygame.key.get_pressed()
        if event[pygame.K_w]:
            self.speedY -= 6
        if event[pygame.K_s]:
            self.speedY += 6
        if event[pygame.K_a]:
            self.speedX -= 6
        if event[pygame.K_d]:
            self.speedX += 6
        if event[pygame.K_SPACE] and self.cooldownTimer == 0:
            self.cooldownTimer = 1
            self.shoot()

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

    def update(self):
        self.screenWrap()
        self.move()


class Meteor(Movables):
    def destroy(self):
        if self.rect.top >= 980 or self.health <= 0:
            self.kill()

    def move(self):
        self.rect.x += self.startingPos[2]
        self.rect.y += self.startingPos[3]
