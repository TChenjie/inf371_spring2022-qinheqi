import pygame,random
pygame.init()

size1=width,height=640,480
size2=width,height=800,600
ballspeed=[2,2]
black=(0,0,0)
white=(255,255,255)
blue=(0,0,120)
backgroundClolor=(50,50,50)
facespeed=[5,5]
class unit():
    def __init__(self,file,screenSize,speed):
        self.picture=pygame.image.load(file)
        self.rect=self.picture.get_rect()
        self.height=screenSize[0]
        self.weight=screenSize[1]
        self.speed=speed
        self.randomPosition()
    def move(self):
        self.rect=self.rect.move(self.speed)
        if self.rect.left<0 or self.rect.ringht>self.weight:
            self.speed[0]=-self.speed[0]
        if self.rect.top<0 or self.rect.bottom>self.height: 
            self.speed[1]=-self.speed[1] 

testplace=pygame.Surface((50,50))
testRect=pygame.Rect(0,0,50,50)
test=pygame.draw.rect(testplace,blue,testRect)
ball=("intro_ball.gif",size1,ballspeed)
smiley=("smiley.png",size2,ballspeed)



