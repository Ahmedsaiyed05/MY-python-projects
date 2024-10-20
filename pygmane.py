import pygame 
import random
import time
pygame.init()
width, height = 400,400
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("snake game")

x, y = 200,200

def snake():
    pygame.draw.rect(game_screen,(255,255,255),[x,y,10,10])
    pygame.display.update()

while True:
    events=pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
    snake()




