import pygame,random
pygame.init()


black=(0,0,0)
white=(255,255,255)
blue=(0,0,120)
backgroundClolor=(50,50,50)
testplace=pygame.Surface((50,50))
testRect=pygame.Rect(0,0,50,50)
test=pygame.draw.rect(testplace,blue,testRect)
yyue=pygame.mixer.music.load("m87.mp3")
ball=pygame.image.load("intro_ball.gif")
face=pygame.image.load("smiley.png")
ball_rect=ball.get_rect()
