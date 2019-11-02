import pygame,time

pygame.init()

display_width = 800
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("마리오")

clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)

gameDisplay.fill(white)

x = (display_width * 0.38)
y = (display_height * 0.45)

x_change = 0
y_change = 0

gameExit = False

marioImg = pygame.image.load('aaa.png')
mario_width = 195
mario_height = 259

iceImg = pygame.image.load('ice.jpeg')
ice_width = 198
ice_height = 255


def text_object(text,font):

    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()


def message_display(text):

    largeText = pygame.font.Font("freesansbold.ttf",115)

    TextSurf, TextRect = text_object(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))

    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(2)


def crash():
    message_display("Game over")


def mario(x,y):

    gameDisplay.blit(marioImg,(x,y))


def ice(x,y):

    gameDisplay.blit(iceImg, (x, y))


while not gameExit:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            gameExit = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                x_change = -5

            if event.key == pygame.K_RIGHT:

                x_change = 5

            if event.key == pygame.K_UP:

                y_change = -5

            if event.key == pygame.K_DOWN:

                y_change = 5

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:

                x_change = 0
                y_change = 0


    x = x + x_change
    y = y + y_change

    gameDisplay.fill(white)

    mario(x,y)


    pygame.display.update()
    clock.tick(60)

    if(x > display_width - mario_width or x < 0):
        crash()
        gameDisplay = True

    if (y > display_height - mario_height or y < 0):
        crash()
        gameDisplay = True
