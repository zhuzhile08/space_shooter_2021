import pygame
""" Bullet class """


class Bullet(pygame.sprite.Sprite):
    def __init__(self, texture, startingPos):
        pygame.sprite.Sprite.__init__(self)
        self.startingPos = startingPos
        self.image = pygame.image.load(texture).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = startingPos[0]
        self.rect.top = startingPos[1]
        self.speedX = 0
        self.speedY = 0

    def destroy(self):
        self.kill()

    def move(self):
        self.speedY = 10
        self.rect.y -= self.speedY

    def update(self):
        self.move()
        if self.rect.bottom <= 0 or self.rect.top >= 980:
            self.destroy()
