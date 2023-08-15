# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("src/robot.png")

window.fill((0, 0, 0))
x_val = 50
y_val = 100
for i in range(0, 10):
    for j in range(0, 10):
        window.blit(robot, (x_val, y_val))
        x_val += 40
    x_val -= 390
    y_val += 20
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()