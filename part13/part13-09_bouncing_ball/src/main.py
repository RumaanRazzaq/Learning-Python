# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("src/ball.png")
x = 0
y = 0
x_velocity = 5
y_velocity = 5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0,0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += x_velocity
    y += y_velocity

    if x + robot.get_width() >= 640:
        x_velocity *= -1
    if x < 0:
        x_velocity *= -1

    if y + robot.get_height() >= 480:
        y_velocity *= -1
    if y < 0:
        y_velocity *= -1
    
    clock.tick(60)