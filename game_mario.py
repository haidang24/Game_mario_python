# import library
import pygame

# setup game
pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("game_mario")
icon = pygame.image.load('mario.ico')
pygame.display.set_icon(icon)

# setup background
background_x = 0
background_y = 0
background_image = pygame.image.load('background.png')
# set mario
mario_x = 0
mario_y = 220
mario_image = pygame.image.load('mario.png')
# set dragon
dragon_x = 500
dragon_y = 200
dragon_image = pygame.image.load('dragon.png')
# set fireball
fireball_x = 430
fireball_y = 220
fireball_image = pygame.image.load("fireball.png")
# set display end_game
end_x = 40
end_y = 13
end_image = pygame.image.load("end.png")

# set variable
ktgame = True
jump = False
clock = pygame.time.Clock()
end_game = True
Nhac = False
score = 0
TopScore = 0
speed = 100
level = 1
pygame.mixer.music.load('mario_theme.wav')
pygame.mixer.music.play(-1, 0.0)
font = pygame.font.SysFont('forte', 20)


def setup():
    clock.tick(speed)
    background_1 = screen.blit(
        background_image, (background_x, background_y))
    mario_1 = screen.blit(mario_image, (mario_x, mario_y))
    fireball_1 = screen.blit(fireball_image, (fireball_x, fireball_y))
    dragon_1 = screen.blit(dragon_image, (dragon_x, dragon_y))
    textsurface = font.render(f'Score: {score}', False, (0, 0, 0))
    screen.blit(textsurface, (2, 0))
    textsurface1 = font.render(f'TopScore: {TopScore}', False, (0, 0, 0))
    screen.blit(textsurface1, (100, 0))
    textsurface2 = font.render(f'Level: {level}', False, (0, 0, 0))
    screen.blit(textsurface2, (230, 0))


# loop game
while (end_game):
    # set music theme
    # set & insert background for game
    if ktgame == True:
        setup()
        # set & insert mario for game
        if mario_y > 80:
            if (jump == True):
                mario_y -= 5
        else:
            jump = False
        if mario_y < 220:
            if jump == False:
                mario_y += 5
        # set & insert dragon for game
        fireball_x -= 3
        if fireball_x < -100:
            fireball_x = 430
            score += 1
            if score == 10:
                speed += 10
                level += 1
            if score == 20:
                speed += 5
                level += 1
            if score == 30:
                speed += 5
                level += 1
            if score == 40:
                speed += 5
                level += 1
            if score == 50:
                speed += 5
                level += 1
            if score == 60:
                speed += 10
                level += 1
            if score == 70:
                speed += 10
                level += 1
            if score == 100:
                level += 1
            if score > TopScore:
                TopScore = score
        # set & insert dragon for game
        # Lose
        if (mario_y == fireball_y and -40 <= fireball_x <= mario_x+20 or level == 9):
            ktgame = False
            fireball_x = 430
            fireball_y = 220
            score = 0
            Nhac = False
            speed = 100
            level = 1
            pygame.mixer.music.stop()
            music = pygame.mixer.Sound('mario_dies.wav')
            music.play()
    if ktgame == False:
        screen.fill((0, 0, 0))
        end_1 = screen.blit(end_image, (end_x, end_y))
    # Check event pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if mario_y == 220:
                    jump = True
            if event.key:
                if event.key != pygame.K_SPACE and event.key != pygame.K_UP:
                    ktgame = True
                    pygame.mixer.music.play(-1, 0.0)
    pygame.display.flip()

# End Game
pygame.quit()
