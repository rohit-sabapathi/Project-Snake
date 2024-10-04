import pygame
from random import *

pygame.init()

screen = pygame.display.set_mode((600,450))
clock = pygame.time.Clock()
running = True
dt = 0
temp = 0
game = 0
touch = 0
# add_box = 0
# direction = 0
# box_positions = []
# check = 0

fonts = pygame.font.SysFont("tomorrowregular",42,False,False)
text = fonts.render("Start",False,"black")

fonts1 = pygame.font.SysFont("tomorrowregular",50)
text1 = fonts.render("Mission Successfully Failed!",False,"black")

player_position = pygame.Vector2(screen.get_width() /2, screen.get_height()/2)

# def add_box1(x,y,dir):
#     if dir == 1:
#         y = y + 16
#     elif dir == 2:
#         y = y - 16
#     elif dir == 3:
#         x = x + 16
#     else:
#         x = x - 16
#     return pygame.Rect(x,y,16,16)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
              if button1.collidepoint(pygame.mouse.get_pos()):
                game = True

    if game == 1:
        left_border = pygame.Rect(0,0,25,450)
        top_border = pygame.Rect(25,0,550,25)
        right_border = pygame.Rect(575,0,25,450)
        bottom_border = pygame.Rect(25,425,550,25)

        rectangle = pygame.Rect(25,25,550,400)

        border_left = pygame.draw.rect(screen,"black",left_border)
        border_top = pygame.draw.rect(screen,"black",top_border)
        border_right = pygame.draw.rect(screen,"black",right_border)
        border_bottom = pygame.draw.rect(screen,"black",bottom_border)

        ground = pygame.draw.rect(screen,"grey",rectangle)

        snake = pygame.Rect(player_position.x,player_position.y,16,16)
        snake1 = pygame.draw.rect(screen,"red",snake)

        if not touch:
            one = randrange(26,550)
            two = randrange(26,400)
            if snake1.collidepoint((one,two)):
                pass
            else:
                box = pygame.Rect(one,two,12,12)
                touch = 1

        boxes = pygame.draw.rect(screen,"yellow",box)

        if snake1.colliderect(boxes):
            boxes = pygame.draw.rect(screen,"grey",box)
            touch = 0
            # add_box = 1

        # if add_box:
        #     box_positions.append(add_box1(player_position.x,player_position.y,dir))
        #     check = 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or temp == 1:
                player_position.y -= 50 *dt
                direction = 1
                temp = 1
        if keys[pygame.K_s] or temp == 2:
                player_position.y += 50 *dt
                direction = 2
                temp = 2
        if keys[pygame.K_a] or temp == 3:
                player_position.x -= 50 *dt
                direction = 3
                temp = 3
        if keys[pygame.K_d] or temp == 4:
                player_position.x += 50 *dt
                direction = 4
                temp = 4
        if temp == 0:
            player_position.x += 50 *dt
            direction = 4



        if snake1.colliderect(border_bottom) or snake1.colliderect(border_top) or snake1.colliderect(border_right) or snake1.colliderect(border_left):
            game = 2
    elif game == 2:
        screen.fill("lavender")
        screen.blit(text1,(300 - text1.get_width() //2,225 - text1.get_height() //2))
    else:
        screen.fill("lavender")
        button = pygame.Rect(player_position.x-50,player_position.y-25,100,50)
        button1 = pygame.draw.rect(screen,"lightslateblue",button)
        screen.blit(text,button1)
    # if check:
    #     for i in range(len(box_positions)):
    #         pygame.draw.rect(screen,"red",box_positions[i])
    #         pygame.display.flip()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()