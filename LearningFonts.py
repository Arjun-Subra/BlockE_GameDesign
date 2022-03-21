import pygame, os, time
pygame.init()
window=pygame.display.set_mode((700,700))
pygame.display.set_caption("testing")
# creat different type

TITLE_FONT=pygame.font.SysFont('chiller', 80)
MENU_FONT=pygame.font.SysFont('comicsans', 40)
INTSTUCTIONS_FONT=pygame.font.SysFont('comicsans', 25)
text=TITLE_FONT.render('HELL', 1, (255,0,0))
window.fill((255,255,255))
window.blit(text,(50,50))
text=INTSTUCTIONS_FONT.render("Write your insturctions", 1, (0,255,0))
window.blit(text,(220,220))
pygame.display.update()

pygame.time.delay(10000)
