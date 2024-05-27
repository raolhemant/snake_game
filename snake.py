import pygame
pygame.init()
#color
white = (255,255,255)
red =  (255,0,0)
black = (0,0,0)
#snake_head
snake_x = 45
snake_y = 55
snake_size = 10
#window_display
screen_width = 900
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake made by hemant")#game title
pygame.display.update()

exit_game = False
game_over = False

#movement
clock = pygame.time.Clock()
fps = 30
#game loop
while not exit_game:
    for event in pygame.event.get():
        # print(event)#if we left it empty it give error
        if event.type == pygame.QUIT:#its let exit the game
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10
            if  event.key == pygame.K_DOWN:
                snake_y = snake_y + 10

    gamewindow.fill(white)
    pygame.draw.rect(gamewindow, black ,[snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()# this should be kept only then we can change the change in code
    clock.tick(fps)
pygame.quit()
quit()
