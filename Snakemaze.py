import pygame
import random
from button import Button
pygame.init()

screen_width, screen_height  = 800, 800
player_width, player_height = 30, 30
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
player = pygame.Rect((300, 400, player_width, player_height))

food = pygame.Rect((random.randint(0,790),random.randint(0,790),10,10))
pygame.display.set_caption("Snake")

start_img = pygame.image.load('C:/Users/Nikhil/Desktop/img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('C:/Users/Nikhil/Desktop/img/exit_btn.png').convert_alpha()

start_button = Button(300, 300, start_img, 0.5)
exit_button = Button(310, 400, exit_img, 0.5)
running = True
playing = False
color = "black"

# def scoreboard():

while running:

    screen.fill(color)
    for i in range(len(player)):
        pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen,(0, 255, 0),food)
    if playing:
        
        key = pygame.key.get_pressed()
        
        if key[pygame.K_q] == True:
            running = False
        else:    
            if key[pygame.K_a] == True:
                if player.x>-1:
                    player.move_ip(-1, 0)
                

            elif key[pygame.K_d] == True:
                if player.x<(screen_width - player_width) + 1:
                    player.move_ip(1, 0)

            elif key[pygame.K_w] == True:
                if player.y>-1:
                    player.move_ip(0, -1)

            elif key[pygame.K_s] == True:
                if player.y<(screen_height - player_height) + 1:
                    player.move_ip(0, 1)

        
                
        collide = pygame.Rect.colliderect(player, food)
        if collide:
            food.x = random.randint(0,800)
            food.y = random.randint(0,800)
        
    else:
        if start_button.draw(screen):
           playing = True

        if exit_button.draw(screen):
            print("exit")
            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    
    '''if color == "black":
        color = "blue"
    
    else:
        color = "black"'''
    
pygame.quit()