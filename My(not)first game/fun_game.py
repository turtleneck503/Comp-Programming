"""
Name: Jonathan Perry
Class: Computer Programming 1
Section: A2
Project: Fun Game
"""

#Import statements

import pygame
import random
import time

#User Functions



#main function

def main():
    pygame.init()

    #setup window
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("The Gravitron")


    #define some colors

    RED = (176, 19, 22)
    BLUE = (17, 17, 171)
    PURPLE = (122, 17, 171)
    WHITE = (256,256,256)
    BLACK = (0,0,0)
    YELLOW = (201, 195, 20)


    #define some things idk
    clock = pygame.time.Clock()

    x = SCREEN_WIDTH//2
    y = SCREEN_HEIGHT//2

    bodies = {}


    class body():

        instances = []

        def __init__(self, radius = 0, color = "BLUE", speed = 1.0, x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2, vx = 0.0, vy = 0.0, ax = 0.0, ay = 0.0):
            self.radius: int = radius
            self.color: str = color
            self.speed: float = speed
            self.x: float = x
            self.y: float = y
            self.vx: float = vx
            self.vy: float = vy
            self.ax: float = ax
            self.ay: float = ay 

            body.instances.append(self)

        def process():
            
            for me in body.instances:
                
                #controls
                
                if keys[pygame.K_a]:
                    me.vx -= me.speed
                
                if keys[pygame.K_d]:
                    me.vx += me.speed
                
                if keys[pygame.K_w]:
                    me.vy -= me.speed
                
                if keys[pygame.K_s]:
                    me.vy += me.speed

                #bounce

                if me.x > SCREEN_WIDTH - me.radius or me.x < 0 + me.radius:
                    me.vx *= -.8
                if me.y > SCREEN_HEIGHT - me.radius or me.y < 0 + me.radius:
                    me.vy *= -.8

                if me.x > SCREEN_WIDTH - me.radius:
                    me.x -= 1
                if me.x < 0 + me.radius:
                    me.x += 1
        
                if me.y > SCREEN_HEIGHT - me.radius:
                    me.y -= 1
                if me.y < 0 + me.radius:
                    me.y += 1

                #friction

                # if me.vx > 0:
                #     me.vx -= me.speed / 4
                # elif me.vx < 0:
                #     me.vx += me.speed / 4
                
                # if me.vy > 0:
                #     me.vy -= me.speed / 4
                # elif me.vy < 0:
                #     me.vy += me.speed / 4


                me.x += me.vx
                me.y += me.vy


                pygame.draw.circle(SCREEN,me.color,(me.x,me.y),me.radius)   
    bodies = 5000
    for object in range(bodies):
        body(50,BLUE,1,random.randrange(1,SCREEN_WIDTH),random.randrange(1,SCREEN_HEIGHT))
    
    #Game Loop
    is_running = True
    while is_running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                
        keys = pygame.key.get_pressed()

        SCREEN.fill(BLACK)


        e_pressed = False
        if keys[pygame.K_e] and e_pressed == False:
            body(random.randrange(10,150))
            e_pressed = True
        if not keys[pygame.K_e]:
            e_pressed = False

        body.process()

        pygame.display.flip()

        clock.tick(240)
#conditional execution

if __name__ == "__main__":
    main()