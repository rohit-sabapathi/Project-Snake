import pygame

pygame.init()

screen = pygame.display.set_mode((600,450))
clock = pygame.time.Clock()
running = True
dt = 0
temp = 0

player_position = pygame.Vector2(screen.get_width() /2, screen.get_height()/2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    outer_rectangle = pygame.Rect(0,0,600,450)

    rectangle = pygame.Rect(25,25,550,400)

    border_rectangle = pygame.draw.rect(screen,"black",outer_rectangle)

    ground = pygame.draw.rect(screen,"grey",rectangle)

    snake = pygame.draw.circle(screen,"brown1",player_position,16)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or temp == 1:
            player_position.y -= 50 *dt
            temp = 1
    if keys[pygame.K_s] or temp == 2:
            player_position.y += 50 *dt
            temp = 2
    if keys[pygame.K_a] or temp == 3:
            player_position.x -= 50 *dt
            temp = 3
    if keys[pygame.K_d] or temp == 4:
            player_position.x += 50 *dt
            temp = 4
    if temp == 0:
          player_position.x += 50 *dt

    # print(pygame.Rect.colliderect(snake,outer_rectangle))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()