import pygame
""" Bullet class """


class Bullet(pygame.sprite.Sprite):
    def __init__(self, texture, startingPos, speed):
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

    def move(self):
        self.speedY = self.speed
        self.rect.y -= self.speedY

    def update(self):
        self.move()
        if self.rect.bottom <= 0 or self.rect.top >= 980:
            self.kill()
