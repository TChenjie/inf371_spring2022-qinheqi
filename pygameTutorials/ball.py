from turtle import Turtle
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
face_rect=face.get_rect()
still=False
key=Turtle
x=1
y=1
number=0
while key:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            key=False
            pygame.quit()
            break
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                if x>0:
                    x-=1
                if x<=0:
                    x+=1
            if event.key==pygame.K_RIGHT:
                x=x+1 if x>=0 else x-1
            if event.key==pygame.K_UP:
                y=y+1 if y>=0 else y-1
            if event.key==pygame.K_DOWN:
                if y>0:
                    y-=1
                if y<=0:
                    y+=1  
        if event.type == pygame.MOUSEMOTION:
            if event.buttons[0]==1:
                face_rect=face_rect.move(event.pos[0]-face_rect.x,event.pos[1]-face_rect)
    ball_rect=ball_rect.move(x,y)
    face_rect=face_rect.move(x,y)
    if ball_rect.left < 0 or ball_rect.right > 50:
         x = -x
    if ball_rect.top < 0 or ball_rect.bottom > 50:
        y = -y
        ball_rect=ball_rect.move(x,y)
    if face_rect.left < 0 or face_rect.right > 50:
        x = -x
    if face_rect.top < 0 or face_rect.bottom > 50:
        y = -y
    if pygame.Rect.colliderect(ball_rect, face_rect)and ball_rect.bottom - face_rect.top <= 1:
            y = -y
            number+=1
    test.blit(ball,ball_rect)
    test.blit(face,face_rect)
    pygame.display.update()
pygame.quit()