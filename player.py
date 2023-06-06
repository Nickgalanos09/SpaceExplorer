import pygame, sys, random, time, math

class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        #Properties of Player
        super().__init__()
        self.image = pygame.image.load("OfficialSprites/space-shuttle.png")
        self.mov_image = pygame.image.load("OfficialSprites/space-shuttle-moving.png")
        self.original_image = self.image
        self.rect = self.image.get_rect(topleft=pos)
        self.rotate_amount = 0

    def get_input(self):
        #Rotating system + Moving in the correct direction.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate_amount += 0.5
            self.image = pygame.transform.rotate(self.original_image, self.rotate_amount)
            self.rect = self.image.get_rect(center=self.rect.center)
        elif keys[pygame.K_d]:
            self.rotate_amount -= 0.5
            self.image = pygame.transform.rotate(self.original_image, self.rotate_amount)
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            # Reset rotation amount when no key is pressed
            self.image = pygame.transform.rotate(self.original_image, self.rotate_amount)
            self.rect = self.image.get_rect(center=self.rect.center)

        if keys[pygame.K_w]:
            #Moving in the correct direction.
            self.image = pygame.transform.rotate(self.mov_image, self.rotate_amount)
            self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.get_input()



