# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
x1 = 160
y1 = 240
x2 = 480
y2 = 240

p1_to_right = False
p1_to_left = False
p1_to_down = False
p1_to_up = False

p2_to_right = False
p2_to_left = False
p2_to_down = False
p2_to_up = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p1_to_left = True
            if event.key == pygame.K_RIGHT:
                p1_to_right = True
            if event.key == pygame.K_DOWN:
                p1_to_down = True
            if event.key == pygame.K_UP:
                p1_to_up = True
            if event.key == pygame.K_a:
                p2_to_left = True
            if event.key == pygame.K_d:
                p2_to_right = True
            if event.key == pygame.K_s:
                p2_to_down = True
            if event.key == pygame.K_w:
                p2_to_up = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p1_to_left = False
            if event.key == pygame.K_RIGHT:
                p1_to_right = False
            if event.key == pygame.K_DOWN:
                p1_to_down = False
            if event.key == pygame.K_UP:
                p1_to_up = False
            if event.key == pygame.K_a:
                p2_to_left = False
            if event.key == pygame.K_d:
                p2_to_right = False
            if event.key == pygame.K_s:
                p2_to_down = False
            if event.key == pygame.K_w:
                p2_to_up = False

        if event.type == pygame.QUIT:
            exit()

    if p1_to_right and x1 + robot.get_width() < 640:
        x1 += 2
    if p1_to_left and x1 > 0:
        x1 -= 2
    if p1_to_down and y1 + robot.get_height() < 480:
        y1 += 2
    if p1_to_up and y1 > 0:
        y1 -= 2
    
    if p2_to_right and x2 + robot.get_width() < 640:
        x2 += 2
    if p2_to_left and x2 > 0:
        x2 -= 2
    if p2_to_down and y2 + robot.get_height() < 480:
        y2 += 2
    if p2_to_up and y2 > 0:
        y2 -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)