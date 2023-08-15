# WRITE YOUR SOLUTION HERE:
import pygame, math, datetime

pygame.init()

display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()

def convert_degrees_to_radians(R, theta):
    x = math.sin(2*math.pi*theta/360)*R
    y = math.cos(2*math.pi*theta/360)*R
    return x+400, -(y-400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.fill((0, 0, 0))
    pygame.draw.circle(display, (255, 0, 0), (400, 400), 300, 4)

    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute
    hour = current_time.hour

    # second
    R = 280
    theta = second*(360/60)
    pygame.draw.line(display, (0, 0, 255), (400, 400), convert_degrees_to_radians(R, theta), 1)

    # minute
    R = 260
    theta = minute*(360/60)
    pygame.draw.line(display, (0, 0, 255), (400, 400), convert_degrees_to_radians(R, theta), 2)

    # hour
    R = 200
    theta = hour*(360/12)
    pygame.draw.line(display, (0, 0, 255), (400, 400), convert_degrees_to_radians(R, theta), 8)

    pygame.display.update()
    clock.tick(50)