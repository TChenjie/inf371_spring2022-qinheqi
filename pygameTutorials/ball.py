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
testplace=pygame.Surface((50,50))
testRect=pygame.Rect(0,0,50,50)
test=pygame.draw.rect(testplace,blue,testRect)
ball=("intro_ball.gif",size1,ballspeed)
smiley=("smiley.png",size2,ballspeed)
def move(self):
    


