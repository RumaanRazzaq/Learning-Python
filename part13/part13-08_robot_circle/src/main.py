# WRITE YOUR SOLUTION HERE:
import pygame, math

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("src/robot.png")
angle = 0
clock = pygame.time.Clock()

x = 0
y = 0
window.fill((0,0, 0))

# for i in range(0, 10):
#     x = 320+math.cos(angle)*100-robot.get_width()/2
#     y = 240+math.sin(angle)*100-robot.get_height()/2

#     window.blit(robot, (x, y))
#     pygame.display.flip()
    
#     angle += 36

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    for i in range(0, 10):
        x = 640/2+math.cos(angle+2*math.pi*i/10)*100
        y = 480/2+math.sin(angle+2*math.pi*i/10)*100

        window.blit(robot, (x, y))
        pygame.display.flip()
    
    angle += 0.01
    
    clock.tick(60)