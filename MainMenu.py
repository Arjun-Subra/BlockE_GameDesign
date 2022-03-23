#Arjun Subramanian
#03/23/2022

#Main Menu for the game and creating functions for the menu

import pygame, os, time
pygame.init()

WIDTH=700
HEIGHT=700


window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Circle Eats Square")

colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75], 
'mag':[255,0,255], 'green':[0,255,0],'mag2':[255,50,255], 'Ω':[57, 11, 92]}


background= colors.get('mag')
cr_color=colors.get('green')



TITLE_FONT=pygame.font.SysFont('algerian', 80)
MENU_FONT=pygame.font.SysFont('comicsans', 40)
INST_FONT=pygame.font.SysFont('comicsans', 25)

text=TITLE_FONT.render('Game', 1, (255,0,0))
window.fill((255,255,255))
window.blit(text,(100,50))

text=INST_FONT.render("Write your insturctions", 1, (0,255,0))
window.blit(text,(220,220))

wb=30
hb=30
xs=50
ys=250
square=pygame.Rect(xs,ys,wb,hb)

pygame.display.update()
pygame.time.delay(10000)