import pygame

# this line initializes all the modules in the pygame environment
pygame.init()
#this line implicitly initializes the display surface and set the display height and width
screen = pygame.display.set_mode((600,450))
#this line creates an object that helps to track time.
clock = pygame.time.Clock()
running = True

while running:
    #there is an event buffer or a queue to store the events which occurs
    #at the window, by looping each object in the buffer , the
    #type of the event is checked, if the user has clicked the
    # cancel button[X] the code execution stops
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:   #pygame.QUIT represents cancel[X]
            running = False

    screen.fill("purple")  # fills the screen with the color mentioned

    pygame.display.flip()  # updates the screen surface in the window with the new changes

    clock.tick(60) # represents the frames that should be run per second like the while loop will now run 60 times per second.

pygame.quit() # safely quits the pygame environment.
