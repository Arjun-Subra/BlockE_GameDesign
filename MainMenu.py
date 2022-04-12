#Arjun Subramanian
#03/23/2022

#Main Menu for the game and creating functions for the menu

import pygame, os, time
pygame.init()

WIDTH=700
HEIGHT=700
wb=30
hb=30
xs=50
ys=250

window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Circle Eats Square")

colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75], 
'mag':[255,0,255], 'green':[0,255,0],'mag2':[255,50,255], 'Ω':[74, 37, 102],
'black':[0,0,0], 'crim':[163,16,16]}

MenuList=["Instuctions", "Settings", "Level 1", "Level 2", "Level 3", "Score Board", "Exit"]

background= colors.get('black')
sq_color2=colors.get('Ω')



TITLE_FONT=pygame.font.SysFont('algerian', 80)
MENU_FONT=pygame.font.SysFont('comicsans', 40)
INST_FONT=pygame.font.SysFont('chiller', 30)

text=TITLE_FONT.render('MENU', 1, colors.get('crim'))
window.fill(background)
xt=WIDTH/2-text.get_width()/2
 
window.blit(text,(xt,50))




square=pygame.Rect(xs,ys,wb,hb)
for i in range(7):
    message=MenuList[i]
    text=INST_FONT.render(message, 1, colors.get('crim'))
    window.blit(text,(90,ys))
    pygame.draw.rect(window, sq_color2,square)
    square.y+=50
    ys+=50


pygame.display.update()
pygame.time.delay(10000)