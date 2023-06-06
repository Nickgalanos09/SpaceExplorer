import pygame, random
from player import *

#Here I am creating a class, where I set the positioning of the sprites, colour, and properties.

class BackgroundWin(pygame.sprite.Sprite):

    def __init__(self, pos):
        #Properties of Winning Background
        super().__init__()
        self.image = pygame.image.load("OfficialSprites/img.png")
        self.original_image = self.image
        self.rect = self.image.get_rect(topleft=pos)
