import pygame
import random

pygame.init()

#Colours
red = (255,0,0)
green = (0,255,0)
olive = (128,128,0)
background = (70,190,30)
blue = (0,0,255)
black = (0,0,0)
white = (225,225,225)

colourList = [red,green,blue]

width = 640
height = 640

#Grid dimentions
rows = 16
columns = 16

cellSize = 40

#Snake
head = 15
vel = 16
head_colour = (70,190,30)

head_x = (width // 2) + 16
head_y = (height // 2) + 16

body_size = 3

#Food
food = 15
food_colour = (255,0,0)
food_x,food_y = random.randrange(0, width)//16*16,random.randrange(0, height)//16*16 #Rounds down to the nearest 10 then multiplies it back to original size



clock = pygame.time.Clock()


window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Roan's Snake Game")

deltaX, deltaY = 16,0

bodyList = [(head_x,head_y)]

def updateDisplay():
    global head_x,head_y,food_x,food_y
    head_x = (head_x + deltaX)%width
    head_y = (head_y + deltaY)%height

    bodyList.append((head_x,head_y))

    


    if(head_x == food_x and head_y == food_y):
        bodyList.append((head_x,head_y))
    else:
        del bodyList[0]

    
    #Clears Screen
    window.fill(black)

    #Draw food
    pygame.draw.rect(window, food_colour, (food_x,food_y ,food,food))

    #Draw head
    for (i,j) in bodyList:
        pygame.draw.rect(window, head_colour, (i,j ,head,head))

    pygame.display.update()



#Game Loop
running = True
updateDisplay()

#FPS


while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        #Game Logic
        if(event.type == pygame.KEYDOWN):
            #keys = pygame.key.get_pressed()
            if(event.key == pygame.K_LEFT):
                if(deltaX != vel):
                    deltaX = -vel
                deltaY = 0
            elif (event.key == pygame.K_RIGHT):
                if(deltaX != -vel):
                    deltaX = vel
                deltaY = 0
            elif (event.key == pygame.K_UP):
                if(deltaY != vel):
                    deltaY = -vel
                deltaX = 0
            elif (event.key == pygame.K_DOWN):
                if(deltaY != -vel):
                    deltaY = vel
                deltaX = 0
            else:
                continue

            updateDisplay()

    if (not events):
        updateDisplay()

    clock.tick(7)
    
        
        #pygame.time.delay(50)

#Clean up

pygame.quit()
