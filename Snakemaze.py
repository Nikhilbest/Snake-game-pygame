import pygame
import random
from button import Button
pygame.init()

fps = 10
screen_width, screen_height  = 800, 800
player_size = 20
background_image = pygame.image.load("background_img/background.jpg")
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)


clock = pygame.time.Clock()

food = pygame.Rect((random.randint(0,790),random.randint(50,840),10,10))

pygame.display.set_caption("Snake Game")

start_img = pygame.image.load('C:/Users/Nikhil/Desktop/img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('C:/Users/Nikhil/Desktop/img/exit_btn.png').convert_alpha()

start_button = Button(300, 300, start_img, 0.5)
exit_button = Button(310, 400, exit_img, 0.5)

running = True
playing = False

score = 0
font = pygame.font.SysFont("Lucida Calligraphy", 32)

snake = []
snake.append(pygame.Rect(260, 400, player_size, player_size))
snake.append(pygame.Rect(240, 400, player_size, player_size))
snake.append(pygame.Rect(220, 400, player_size, player_size))

direction = 'right'

while running:

    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen,(0, 0, 0),food)

    if playing:
        
        key = pygame.key.get_pressed()
        
        if key[pygame.K_q] == True:
            running = False
        else:
            if key[pygame.K_UP] == True and direction != "down":
                direction = "up"
            elif key[pygame.K_DOWN] == True and direction != "up":
                direction = "down"
            elif key[pygame.K_LEFT] == True and direction != "right":
                direction = "left"
            elif key[pygame.K_RIGHT] == True and direction != "left":
                direction = "right"

            new_head = snake[0].copy()
            if direction == "left":
                new_head.x -= player_size
                
            elif direction == "right":
                new_head.x += player_size

            elif direction == "up":
                new_head.y -= player_size
                
            elif direction == "down":
                new_head.y += player_size

            snake.insert(0, new_head)
            snake.pop()

        collide = pygame.Rect.colliderect(snake[0], food)
        if collide:
            score += 1
            snake.append(snake[-1].copy())
            food.x = random.randint(0,790)
            food.y = random.randint(50,840)

        if (snake[0].x < 0 or snake[0].x >= screen_width or
            snake[0].y < 0 or snake[0].y >= screen_height or
            snake[0] in snake[1:]):
            
            running = False

    else:
        if start_button.draw(screen):
           playing = True   

        if exit_button.draw(screen):
            running = False 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    for square in snake:
        pygame.draw.rect(screen, (255, 0, 0), square)   

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()
    clock.tick(fps)
    
    
pygame.quit()