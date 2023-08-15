# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("src/robot.png")

window.fill((0, 0, 0))
for i in range(0, 1000):
    x_val = random.randint(0, 590)
    y_val = random.randint(0, 400)
    window.blit(robot, (x_val, y_val))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()