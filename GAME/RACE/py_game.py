from random import randrange
import time
import pygame as p

p.init()

display_w = 1920
display_h = 1080

black = (0,0,0)
bright_green = (0,255,0)
bright_red = (255,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,128,0)
block_color = (53,115,255)
car_w = 73
gameDisplay = p.display.set_mode((display_w,display_h))
p.display.set_caption('A bit Racey')
clock = p.time.Clock()

carImg = p.image.load('race.png')

def things_dodged(count):
    font = p.font.SysFont(None,25)
def things(thingx,thingy,thingw,thingh,color):
    p.draw.rect(gameDisplay,color, [thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text,font):
    textSurface = font.render(text,True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largetext = p.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect= text_objects(text, largetext)
    TextRect.center = ((display_w / 2), (display_h / 2))
    gameDisplay.blit(TextSurf,TextRect)
    p.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('RE START')

def game_loop():
    x = (display_w * 0.45)
    y = (display_h * 0.8)

    x_change = 0

    thing_startx = randrange(0, display_w)
    thing_starty = -600
    thing_speed = 4
    thing_w = 100
    thing_h = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:


        #score += 1

        for event in p.event.get():
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    quit()

            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:
                    x_change = -10

                if event.key == p.K_RIGHT:
                    x_change = -1

            if event.type == p.KEYUP:
                if event.key == p.K_LEFT or event.key == p.K_RIGHT:
                  x_change = 0

        x += x_change

        gameDisplay.fill(white)

        things(thing_startx,thing_starty,thing_w,thing_h,block_color)

        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_w - car_w or x < 0:
            crash()

        if thing_starty > display_h:
            thing_starty = 0 - thing_h
            thing_startx = randrange(0, display_w)
            dodged += 1
            thing_speed += 1
            thing_w += (dodged * 1.2)

        if y< thing_starty + thing_h:
            print('Y crossover')

            if x > thing_startx and x < thing_startx + thing_w or x + car_w > thing_startx and x + car_w < thing_startx + thing_w:
                print("x crossover")
                crash()
        p.display.update()
        clock.tick(60)

def quitgame():
    p.quit()

game_loop()
quit()


