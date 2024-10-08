import pygame
from random import *

pygame.init()

screen = pygame.display.set_mode((600, 450))
clock = pygame.time.Clock()
running = True
dt = 0
temp = 0
game = 0
touch = 0


snake_body = []
snake_length = 5
segment_size = 20
move_speed = 100

fonts = pygame.font.SysFont("tomorrowregular", 42, False, False)
text = fonts.render("Start", False, "black")
fonts1 = pygame.font.SysFont("tomorrowregular", 50)
text1 = fonts.render("Mission Successfully Failed!", False, "black")

player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
direction = pygame.Vector2(1, 0)

def draw_snake(screen, snake_body):
    for part in snake_body:
        pygame.draw.rect(screen, "red", pygame.Rect(part[0], part[1], segment_size, segment_size))

def update_snake_body(snake_body, snake_length, head_position):
    snake_body.insert(0, list(head_position))

    if len(snake_body) > snake_length:
        snake_body.pop()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(pygame.mouse.get_pos()):
                game = True

    if game == 1:
        left_border = pygame.Rect(0, 0, 25, 450)
        top_border = pygame.Rect(25, 0, 550, 25)
        right_border = pygame.Rect(575, 0, 25, 450)
        bottom_border = pygame.Rect(25, 425, 550, 25)

        rectangle = pygame.Rect(25, 25, 550, 400)

        border_left = pygame.draw.rect(screen, "black", left_border)
        border_top = pygame.draw.rect(screen, "black", top_border)
        border_right = pygame.draw.rect(screen, "black", right_border)
        border_bottom = pygame.draw.rect(screen, "black", bottom_border)

        ground = pygame.draw.rect(screen, "grey", rectangle)

        update_snake_body(snake_body, snake_length, player_position)
        draw_snake(screen, snake_body)

        if not touch:
            one = randrange(26, 550)
            two = randrange(26, 400)
            if pygame.Rect(player_position.x, player_position.y, segment_size, segment_size).collidepoint((one, two)):
                pass
            else:
                box = pygame.Rect(one, two, 16, 16)
                touch = 1

        boxes = pygame.draw.rect(screen, "yellow", box)

        if pygame.Rect(player_position.x, player_position.y, segment_size, segment_size).colliderect(boxes):
            boxes = pygame.draw.rect(screen, "grey", box)
            touch = 0
            snake_length += 5

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and direction.y == 0:
            direction = pygame.Vector2(0, -1)
        if keys[pygame.K_s] and direction.y == 0:
            direction = pygame.Vector2(0, 1)
        if keys[pygame.K_a] and direction.x == 0:
            direction = pygame.Vector2(-1, 0)
        if keys[pygame.K_d] and direction.x == 0:
            direction = pygame.Vector2(1, 0)

        player_position += direction * move_speed * dt


        temp_rect = pygame.Rect(player_position.x, player_position.y, segment_size, segment_size)
        if temp_rect.colliderect(border_bottom) or temp_rect.colliderect(border_top) or temp_rect.colliderect(border_right) or temp_rect.colliderect(border_left):
            game = 2

        for segment in snake_body[:-1]:
            if segment == (player_position.x, player_position.y):
                game = 2
                break

    elif game == 2:
        screen.fill("lavender")
        screen.blit(text1, (300 - text1.get_width() // 2, 225 - text1.get_height() // 2))
    else:
        screen.fill("lavender")
        button = pygame.Rect(player_position.x - 50, player_position.y - 25, 100, 50)
        button1 = pygame.draw.rect(screen, "lightslateblue", button)
        screen.blit(text, button1)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
