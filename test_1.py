import pygame
x = pygame.init()
#creating window for game
gamewindow = pygame.display.set_mode((200, 500))
pygame.display.set_caption("My first game")# its gives name of window

exit_game = False
game_over = False

#creating the game loop
while not exit_game:
    for event in pygame.event.get():#what you do with keywords/mouse it reacts
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN: #lets know whats we pressed
            if event.key == pygame.K_RIGHT: #what key we pressed
                print("you have pressed right key")
pygame.quit()
quit()
