import pygame
import random

#They are called stars but really are enemies.
class Stars(pygame.sprite.Sprite):

    def __init__(self, pos):
        #Properties of Enemies
        super().__init__()
        self.image = pygame.image.load("OfficialSprites/zombie.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 2

    def update(self, player_pos):
        #System to move the enemies towards the position of the player
        dx = player_pos[0] - self.rect.x
        dy = player_pos[1] - self.rect.y
        distance = pygame.math.Vector2(dx, dy)

        if distance.length() > 100:  # Adjust the distance threshold as needed
            distance.normalize()
            distance.scale_to_length(self.speed)
            self.rect.move_ip(distance)

