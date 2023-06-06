import pygame, random
from player import *

#Here I am creating a class, where I set the positioning of the sprites, colour, and properties.

class Background(pygame.sprite.Sprite):

    def __init__(self, pos):
        #Properties of Background
        super().__init__()
        self.image = pygame.image.load("OfficialSprites/SpaceBackground.png")
        self.original_image = self.image
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 1.5

    #Creation of Key inputs
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = 1
        elif keys[pygame.K_s]:
            self.direction.y = -1
        else:
            self.direction.y = 0
            self.direction.x = 0

    #Rotating System
    def update(self, rotation):
        self.get_input()
        rotation += 90
        angle_radians = math.radians(rotation % 360)

        delta_x = -math.cos(angle_radians) * self.speed
        delta_y = math.sin(angle_radians) * self.speed

        self.rect.y += self.direction.y * delta_y
        self.rect.x += self.direction.y * delta_x
        #print(self.direction.y * delta_x, self.direction.y * delta_y)
