import pygame
""" Bullet class """


class Bullet(pygame.sprite.Sprite):
    def __init__(self, texture, startingPos, speed, explosionTexture):
        pygame.sprite.Sprite.__init__(self)
        self.startingPos = startingPos
        self.image = pygame.image.load(texture).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = startingPos[0]
        self.rect.top = startingPos[1]
        self.speed = speed
        self.speedX = 0
        self.speedY = 0
        self.explosion = Explosion(self.startingPos, explosionTexture)

    def move(self):
        self.speedY = self.speed
        self.rect.y -= self.speedY

    def update(self):
        self.move()
        if self.rect.bottom <= 0 or self.rect.top >= 980:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, texture):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(texture).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = position[0]
        self.rect.centery = position[1]

