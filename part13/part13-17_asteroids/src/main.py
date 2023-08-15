# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))
rock = pygame.image.load("src/rock.png")
robot = pygame.image.load("src/robot.png")

score = 0
number = 20
rocks = []
for i in range(number):
    # causes the new random start position to be drawn immediately
    rocks.append([-1000,480])

x = 0
y = 480 - robot.get_height()
to_right = False
to_left = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        if event.type == pygame.QUIT:
            exit()

    if to_right and x + robot.get_width() < 640:
        x += 2
    if to_left and x > 0:
        x -= 2
    
    for i in range(number):
        if rocks[i][1] + rock.get_height() < 480:
            # the rock falls downwards
            rocks[i][1] += 1
        else:
            for i in range(number):
                rocks[i][0] = randint(0, 640 - rock.get_width())
                rocks[i][1] = - randint(100,1000)
                x = 0
            score = 0
        if rocks[i][1] + rock.get_height() >= y and x - rock.get_width() < rocks[i][0] < x + rock.get_width():
            rocks[i][0] = randint(0, 640 - rock.get_width())
            rocks[i][1] = - randint(100,1000)
            score += 1

    if to_right and x + robot.get_width() < 640:
        x += 1
    if to_left and x > 0:
        x -= 1
 
    window.fill((0, 0, 0))
    for i in range(number):
        window.blit(rock, (rocks[i][0], rocks[i][1]))
    window.blit(robot, (x, y))
    game_font = pygame.font.SysFont("Arial", 18) 
    text = game_font.render(f"Score: {score}", True, (255, 0, 255)) 
    window.blit(text, (530, 0)) 
    pygame.display.flip()
    clock.tick(60)