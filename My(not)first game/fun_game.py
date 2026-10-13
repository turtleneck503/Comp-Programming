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
import math

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

    G = 0.000000000067

    lmb_pressed = False

    x = SCREEN_WIDTH//2
    y = SCREEN_HEIGHT//2

    bodies = {}


    class body():

        instances = []

        def __init__(self, radius = 0, color = "BLUE", mass = 1, speed = 1.0, x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2, vx = 0.0, vy = 0.0, ax = 0.0, ay = 0.0, fx = 0.0, fy = 0.0):
            self.radius: int = radius
            self.color: str = color
            self.mass: int = mass
            self.speed: float = speed
            self.x: float = x
            self.y: float = y
            self.vx: float = vx
            self.vy: float = vy
            self.ax: float = ax
            self.ay: float = ay 
            self.fx: float = fx
            self.fy:float = fy

            body.instances.append(self)

        def apply_gravity():
            for me in body.instances:
                for other_body in body.instances:
                    if other_body == me:
                        pass
                    else:
                            dx = other_body.x - me.x + .01
                            dy = other_body.y - me.y + .01

                            distance = math.sqrt((dx * dx) + (dy * dy)) + .01

                            force = (me.mass * other_body.mass) * (distance * distance) * G

                            me.fx += force / (dx / distance)
                            me.fy += force / (dy / distance)
                        
        def process():
            
            for me in body.instances:
                
                #controls
                
                # if keys[pygame.K_a]:
                #     me.vx -= me.speed
                
                # if keys[pygame.K_d]:
                #     me.vx += me.speed
                
                # if keys[pygame.K_w]:
                #     me.vy -= me.speed
                
                # if keys[pygame.K_s]:
                #     me.vy += me.speed

                #bounce

                if me.x > SCREEN_WIDTH - me.radius or me.x < 0 + me.radius:
                    me.vx *= -1
                if me.y > SCREEN_HEIGHT - me.radius or me.y < 0 + me.radius:
                    me.vy *= -1

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

                me.ax = me.fx / me.mass
                me.ay = me.fx / me.mass

                me.vx += me.ax
                me.vy += me.ax

                me.x += me.vx
                me.y += me.vy

                me.fx = 0
                me.fy = 0

                pygame.draw.circle(SCREEN,me.color,(me.x,me.y),me.radius)   
                
    #Game Loop
    is_running = True
    while is_running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                
        keys = pygame.key.get_pressed()

        SCREEN.fill(BLACK)

        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)
        
        if pygame.mouse.get_just_pressed()[0]:
            body(20,BLUE,1,10000,mouse_pos[0],mouse_pos[1])
        
        body.apply_gravity()
        body.process()

        pygame.display.flip()

        clock.tick(240)

#conditional execution

if __name__ == "__main__":
    main()