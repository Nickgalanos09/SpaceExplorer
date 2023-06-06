import pygame, random
#THIS SCRIPT IS NOT USED
class FinalBoss(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("OfficialSprites/alien.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = 1
            self.direction.x = 0
        elif keys[pygame.K_s]:
            self.direction.y = -1
            self.direction.x = 0
        elif keys[pygame.K_a]:
            self.direction.x = 1
            self.direction.y = 0
        elif keys[pygame.K_d]:
            self.direction.x = -1
            self.direction.y = 0
        else:
            self.direction.y = 0
            self.direction.x = 0

    def update(self):
        self.get_input()
        self.rect.y += self.direction.y
        self.rect.x += self.direction.x
