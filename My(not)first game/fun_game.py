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

    class player:
        def __init__(self):
            self.radius: int
            self.speed: float
            self.x: float  
            self.y: float
            self.vx: float
            self.vy: float
            self.ax: float
            self.ay: float 

    player1 = player()


    

    #Game Loop
    is_running = True
    while is_running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                
        keys = pygame.key.get_pressed()

        SCREEN.fill(BLACK)

        #gets velocities
        
            #p1

        if keys[pygame.K_a]:
            p1_vx -= p1_speed
        
        if keys[pygame.K_d]:
            p1_vx += p1_speed
        
        if keys[pygame.K_w]:
            p1_vy -= p1_speed
        
        if keys[pygame.K_s]:
            p1_vy += p1_speed

            #p2

        if keys[pygame.K_LEFT]:
            p2_vx -= p2_speed
                
        if keys[pygame.K_RIGHT]:
            p2_vx += p2_speed
                
        if keys[pygame.K_UP]:
            p2_vy -= p2_speed
                
        if keys[pygame.K_DOWN]:
            p2_vy += p2_speed

        #makes players bounce off of walls

            #p1

        if player1.x > SCREEN_WIDTH - p1_r or player1.x < 0 + p1_r:
            if p1_hb == False:
                p1_vx *= -1 * p1_bounciness
                p1_hb = True
        if player1.y > SCREEN_HEIGHT - p1_r or player1.y < 0 + p1_r:
            if p1_hb == False:
                p1_vy *= -1 * p1_bounciness
                p1_hb = True

        if player1.x < SCREEN_WIDTH - p1_r or player1.x > 0 + p1_r:
            p1_hb = False
        if player1.y < SCREEN_HEIGHT - p1_r or player1.y > 0 + p1_r:
            p1_hb = False

        if player1.x > SCREEN_WIDTH - p1_r:
            player1.x -= 1
        if player1.x < 0 + p1_r:
            player1.x += 1

        if player1.y > SCREEN_HEIGHT - p1_r:
            player1.y -= 1
        if player1.y < 0 + p1_r:
            player1.y += 1

            #p2

        if player2.x > SCREEN_WIDTH - p2_r or player2.x < 0 + p2_r:
            if p2_hb == False:
                p2_vx *= -1 * p2_bounciness
                p2_hb = True
        if player2.y > SCREEN_HEIGHT - p2_r or player2.y < 0 + p2_r:
            if p2_hb == False:
                p2_vy *= -1 * p2_bounciness
                p2_hb = True

        if player2.x < SCREEN_WIDTH - p2_r or player2.x > 0 + p2_r:
            p2_hb = False
        if player2.y < SCREEN_HEIGHT - p2_r or player2.y > 0 + p2_r:
            p2_hb = False

        if player2.x > SCREEN_WIDTH - p2_r:
            player2.x -= 1
        if player2.x < 0 + p2_r:
            player2.x += 1

        if player2.y > SCREEN_HEIGHT - p2_r:
            player2.y -= 1
        if player2.y < 0 + p2_r:
            player2.y += 1

        #adds friction to velocity

            #p1

        if p1_vx > 0:
            p1_vx -= p1_speed / 4
        elif p1_vx < 0:
            p1_vx += p1_speed / 4
        
        if p1_vy > 0:
            p1_vy -= p1_speed / 4
        elif p1_vy < 0:
            p1_vy += p1_speed / 4

            #p2

        if p2_vx > 0:
            p2_vx -= p2_speed / 4
        elif p2_vx < 0:
            p2_vx += p2_speed / 4
                
        if p2_vy > 0:
            p2_vy -= p2_speed / 4
        elif p2_vy < 0:
            p2_vy += p2_speed / 4


        #add velocity to positions

            #p1

        player1.x += p1_vx
        player1.y += p1_vy

            #p2

        player2.x += p2_vx
        player2.y += p2_vy

        pygame.draw.circle(SCREEN,BLUE,(player1.x,player1.y),p1_r)
        pygame.draw.circle(SCREEN,RED,(player2.x,player2.y),p2_r)

        pygame.display.flip()

        clock.tick(120)
#conditional execution

if __name__ == "__main__":
    main()