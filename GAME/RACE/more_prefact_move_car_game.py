import pygame

pygame.init()


display_width = 1600
display_height = 900

black = (0,0,0)
white = (255,255,255)




gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')


car_speed = 0

car_width = 728

def car(carImg,x,y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text,font):
    textSurface = font.render(text,True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect= text_objects(text, largetext)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

def crash():
    message_display('do not move')

def game_loop():
    x = (display_width * 0.3)
    y = (display_height * 0.3)

    x_change = 0
    y_change = 0

    while not False:

        for event in pygame.event.get():


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        x += x_change
        y += y_change

        gameDisplay.fill(white)
        car(carImg,x,y)

        if x > display_width - car_width or x < 0:
             crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()