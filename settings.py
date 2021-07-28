import os
import object as obj
import random

# define some folders
imgFolder = os.path.join('data', 'img')
bgFolder = os.path.join(imgFolder, 'bg')
laserFolder = os.path.join(imgFolder, 'Lasers')
enemyFolder = os.path.join(imgFolder, 'Enemies')

# generate contents of the enemy dictionaries


def generateEnemyDictionaryStage1():
    stg1EnemyList = []
    for i in range(100):
        change = random.randint(0, 10)
        if 0 <= change <= 4:
            enemy = obj.Meteor(1, os.path.join(enemyFolder, 'meteorBrown1.png'), (random.randrange(200, 450), -200 * i, random.randrange(-5, 5), random.randrange(4, 8)), 0, 0)
        elif 5 <= change <= 9:
            enemy = obj.Meteor(1, os.path.join(enemyFolder, 'meteorGrey1.png'), (random.randrange(200, 450), -200 * i, random.randrange(-5, 5), random.randrange(4, 8)), 0, 0)
        else:
            enemy = obj.Meteor(1, os.path.join(enemyFolder, 'ufoGrey.png'), (random.randrange(200, 450), -200 * i, random.randrange(-5, 5) * 1.5, random.randrange(4, 8) * 1.5), 0, 0)

        stg1EnemyList.append(enemy)

    return stg1EnemyList
