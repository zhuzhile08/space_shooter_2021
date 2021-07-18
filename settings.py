import os
import pygame
import object as obj
import random

pygame.init()
pygame.font.init()

# define some folders
imgFolder = os.path.join('data', 'img')
bgFolder = os.path.join(imgFolder, 'bg')
laserFolder = os.path.join(imgFolder, 'Lasers')
enemyFolder = os.path.join(imgFolder, 'Enemies')

kenFont = pygame.font.Font(os.path.join('data', 'kenvector_future_thin.ttf'), 30)     # font

