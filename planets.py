import pygame, random
from player import *

#Here I am creating a class, where I set the positioning of the sprites, colour, and properties.

class Planets(pygame.sprite.Sprite):

    def __init__(self, pos):
        #Properties of Planets
        super().__init__()
        folderName = "PlanetImages/"
        planetList = [folderName + "planet1.png", folderName + "planet2.png", folderName + "planet7.png", folderName + "planet6.png", folderName + "planet8.png", folderName + "planet3.png", folderName + "planet9.png", folderName + "planet4.png", folderName + "planet5.png"]
        randomSize = random.randint(1300, 1300)
        imageChoice = random.choice(planetList)
        self.speed = 10
        self.image = pygame.Surface((randomSize, randomSize))
        self.image = pygame.image.load(imageChoice)
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)

    def get_input(self):
        #Movements of Planets with Inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = 1
        elif keys[pygame.K_s]:
            self.direction.y = -1
        else:
            self.direction.y = 0
            self.direction.x = 0

    def update(self, rotation):
        #Rotating system
        self.get_input()
        rotation += 90
        angle_radians = math.radians(rotation % 360)

        delta_x = -math.cos(angle_radians) * self.speed
        delta_y = math.sin(angle_radians) * self.speed

        self.rect.y += self.direction.y * delta_y
        self.rect.x += self.direction.y * delta_x
        #print(self.direction.y * delta_x, self.direction.y * delta_y)
