# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
x = 320
y = 240

to_right = False
to_left = False
to_down = False
to_up = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_UP:
                to_up = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_UP:
                to_up = False

        if event.type == pygame.QUIT:
            exit()

    if to_right and x + robot.get_width() < 640:
        x += 2
    if to_left and x > 0:
        x -= 2
    if to_down and y + robot.get_height() < 480:
        y += 2
    if to_up and y > 0:
        y -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)