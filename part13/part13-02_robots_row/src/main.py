# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("src/robot.png")

window.fill((0, 0, 0))
x_val = 70
for i in range(0, 10):
    window.blit(robot, (x_val, 150))
    x_val += 50
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()