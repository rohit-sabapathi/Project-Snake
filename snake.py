import pygame

pygame.init()

screen = pygame.display.set_mode((600,450))
clock = pygame.time.Clock()
running = True
dt = 0

player_position = pygame.Vector2(screen.get_width() /2, screen.get_height()/2)    # returns the default position of the object in the screen

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.circle(screen,"red",player_position,30)  #draws a circle with parameters (surfaceObject,color,position of circle in screen,radius of circle)

    keys = pygame.key.get_pressed()   #returns a tuple of boolean values .True if key is pressed False if released
    #K_w,K_a etc.. each holds a number value or index for the tuple of key states in the 'keys' tuple
    if keys[pygame.K_w]:
        player_position.y -= 300 * dt
    if keys[pygame.K_s]:
        player_position.y += 300 * dt
    if keys[pygame.K_a]:
        player_position.x -= 300 * dt
    if keys[pygame.K_d]:
        player_position.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()