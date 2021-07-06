import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, texture, scale, number):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.smallImage = pygame.image.load(texture).convert()
        self.image = pygame.transform.scale(self.smallImage, self.scale)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 325
        self.rect.centery = 650 * number
        self.speedY = 0

    def move(self):
        self.speedY = 0
        if True:
            self.speedY += 5
        self.rect.y += self.speedY
        if self.rect.y >= 980:
            self.rect.y = -800

    def update(self):
        self.move()
