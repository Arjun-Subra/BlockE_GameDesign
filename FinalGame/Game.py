import pygame, time, random, math
pygame.init()

colors={'red':[255,0,0],'white':[255,255,255],'mag':[255,0,255],
'aqua':[51,153,255],'m':[47,192,229]}
game=True
WIDTH=700
HEIGHT=700
wWidth=25
wLength=100
wx=0
wy=0 
px=30
py=30
pWidth=20
pLength=20
wColor=colors.get('red')
move = 5
pColor=colors.get('aqua')
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Maze")
wall=pygame.Rect(wx,wy,wWidth,wLength)
p1=pygame.Rect(px,py,pWidth,pLength)

while game:
    keys=pygame.key.get_pressed()
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            game=False
    if game:
        screen.fill(colors.get('mag'))
        pygame.draw.rect(screen, wColor, wall)
        if keys[pygame.K_w]and p1.y >=move:
            p1.y -= move
        if keys[pygame.K_s]and p1.x <HEIGHT-pLength:
            p1.y += move
        if keys[pygame.K_a] and p1.x >=move:
            p1.x -= move
        if keys[pygame.K_d] and p1.x <WIDTH-pWidth:
            p1.x += move  
        pygame.draw.rect(screen,pColor,p1)
        pygame.time.delay(10)
        pygame.display.update()
