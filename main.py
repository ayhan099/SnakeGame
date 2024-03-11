#AYHANS SNAKE SPEL


#Importera
import pygame
import time
import random

#Initialisera modulen
pygame.init()

#Definiera färger med färg värden
white = (205, 210, 200)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (0, 255, 0)
green = (50, 153, 213)


#Ställ in fönsterbredd och fönsterhöjd
dis_width = 500
dis_height = 300

#Skapa ett fönster med angiven bredd och höjd
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('IMERS SNAKE')

#Ladda bakgrundsbilden från filen "turkey_flag.png"
background = pygame.image.load("turkey_flag.png")

#Bakgrundsbilden till samma storlek som fönstret
background = pygame.transform.scale(background, (dis_width, dis_height))

#Skapa en klocka för att kontrollera hastigheten
clock = pygame.time.Clock()

#Ange storleken på ormens block och ormens hastighet
snake_block = 10
snake_speed = 10


font_style = pygame.font.SysFont(None, 25)

#Definera själva ormen/snakeblock
def our_snake(snake_block, snake_list):
    for x in snake_list:
        # Ritar ett rektangel för varje block av ormen
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#Funktion för att visa "message" på skärmen
def message(msg, color):
    #Fixa "message" med använding av fonter eller stil
    mesg = font_style.render(msg, True, color)
    #Rita meddelande på skärmen med position.
    dis.blit(mesg, [dis_width / 6, dis_height / 2])



