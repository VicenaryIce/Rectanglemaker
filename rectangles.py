import pygame,sys#new libraries


from pygame.locals import QUIT
from random import randint




pygame.init()
screen = pygame.display.set_mode((1000,750))
pygame.display.set_caption('Rectangle maker')
myfont = pygame.font.SysFont('sans',50)
#mytext = myfont.render('Hello World',True,'white')
screen.blit(myfont.render('Hello World',True,'white'),(100,700))


class Rectangles():
    def __init__(self,color,dimensions):
        self.color = color
        self.dimensions = dimensions
    def create(self):
        pygame.draw.rect(screen,self.color,self.dimensions)
    def colorchange(self):
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        pygame.draw.rect(screen,self.color,self.dimensions)


circle = pygame.draw.circle(screen,'green',(500,500),50,3)

long = Rectangles('orange',(100,100,100,500))
verybig = Rectangles('purple',(500,0,300,500))
long.create()
verybig.create()








#While loop goes last
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            long.colorchange()
        if event.type == pygame.MOUSEWHEEL:
            verybig.colorchange()
    pygame.display.update()





