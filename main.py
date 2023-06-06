import pygame, sys, random, time
from settings import *
from player import Player
from planets import Planets
from SmallBosses import Stars
from LargerBosses import FinalBoss
from Background import Background
from backgroundWin import BackgroundWin

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()

# MAIN VARIABLES
dead = False
counter = 10
collisionPlanet = False
win = False

# PLAYER POSITIONING
xPlayer = 530
yPlayer = 280
xPlanet = 200
yPlanet = 100
player = Player((xPlayer, yPlayer))
playerGroup = pygame.sprite.GroupSingle()
playerGroup.add(player)

starsGroup = pygame.sprite.Group()

planetGroup = pygame.sprite.GroupSingle()

finalBossGroup = pygame.sprite.Group()

#Background for general game
background = Background((0, 0))
backgroundGroup = pygame.sprite.Group()
backgroundGroup.add(background)

#Background for Winning Page
backgroundWin = BackgroundWin((0, 0))
backgroundWinGroup = pygame.sprite.GroupSingle()
backgroundWinGroup.add(backgroundWin)

#Generation of Enemies and Planets
for i in range(10, 10):
    stars = Stars((random.randint(-10000, 30000), random.randint(-15000, 15000)))
    starsGroup.add(stars)

for i in range(10):
    x = random.randint(-500, 100)
    y = random.randint(-150, 100)
    planets = Planets((x, y))
    planetGroup.add(planets)

for i in range(200, 300):
    finalBosses = FinalBoss((random.randint(-2500, 30000), random.randint(-15000, 15000)))
    finalBossGroup.add(finalBosses)

#Creation of Fonts
font = pygame.font.Font("f-feeling-soon-font/FeelingSoon-1GVr0.otf", 32)
fontBig = pygame.font.Font("spacebar/SPACEBAR.ttf", 80)
text = font.render("You have discovered a new Planet !", True, (0, 255, 0))
text1 = fontBig.render("GAME OVER", True, (255, 0, 0))

#Creation of Time
start_time = time.time()
time_limit = 1 * 10  # 2 minutes in seconds

while True:
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")

    # Detects Collision
    collided_with2 = pygame.sprite.spritecollide(playerGroup.sprite, starsGroup, False)
    if len(collided_with2) > 0:
        dead = True

    collided_with3 = pygame.sprite.spritecollide(playerGroup.sprite, finalBossGroup, False)
    if len(collided_with3) > 0:
        dead = True

    if not dead:

        # Music Creation
        pygame.mixer.music.load("Music/NonDeadMusic.mp3")
        pygame.mixer.music.set_volume(2)
        pygame.mixer.music.play()

        # Creation of background
        backgroundGroup.update(playerGroup.sprite.rotate_amount)
        backgroundGroup.draw(screen)

        # Drawing all planets
        planetGroup.update(playerGroup.sprite.rotate_amount)
        planetGroup.draw(screen)

        # Drawing all aliens
        player_pos = player.rect.center
        starsGroup.update(player_pos)  # Pass player's position to the update method
        starsGroup.draw(screen)

        # Drawing player
        playerGroup.draw(screen)
        playerGroup.update()

        # Update and display timer
        elapsed_time = time.time() - start_time
        remaining_time = max(0, time_limit - elapsed_time)

        # Creating a timer display
        timer_text = font.render(f"Time left: {int(remaining_time // 60)}:{int(remaining_time % 60):02}", True, (255, 255, 255))
        screen.blit(timer_text, (10, 10))

        remaining_time -= dt
        if remaining_time <= 0:
            dead = True
            remaining_time = 0

        # Displaying the Discovery Text
        collided_with1 = pygame.sprite.spritecollide(playerGroup.sprite, planetGroup, False)
        if len(collided_with1) > 0 and not collisionPlanet:
            screen.blit(text, (300, 50))
            counter -= 1
            print(str(counter))
            collisionPlanet = True

        # Stop collision handling until objects are no longer colliding
        if collisionPlanet:
            if len(collided_with1) == 0:
                collisionPlanet = False

        if counter == 0:
            win = True

        # Creating a countdown Display
        countdown_text = font.render("Planets to Discover: " + str(counter), True, (255, 255, 255))
        screen.blit(countdown_text, (500, 10))

        if win:
            win = True

        if win == True:
            print("You win!")
            # Creation of background for Winning
            backgroundWinGroup.draw(screen)
    else:
        #DEATH SCREEN
        keys = pygame.key.get_pressed()
        backgroundGroup.draw(screen)
        fontBig = pygame.font.Font("f-feeling-soon-font/FeelingSoon-1GVr0.otf", 100)
        fontSmall = pygame.font.Font("f-feeling-soon-font/FeelingSoon-1GVr0.otf", 20)
        text1 = fontBig.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text1, (320, 200))

    pygame.display.update()
    clock.tick(fps)





