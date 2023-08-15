# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("src/robot.png")
x1 = 0
y1 = 0
x2 = 0
y2 = 100
velocity1 = 1
velocity2 = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0,0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    x1 += velocity1
    if x1 + robot.get_width() >= 640:
        velocity1 *= -1
    if x1 < 0:
        velocity1 *= -1

    x2 += velocity2
    if x2 + robot.get_width() >= 640:
        velocity2 *= -1
    if x2 < 0:
        velocity2 *= -1
    
    clock.tick(60)