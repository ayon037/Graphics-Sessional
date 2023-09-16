import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

Position= [0,0,0]
class Cube:  
    def __init__(self, x, y):
        self.v = [(-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1), (-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1)]
        self.edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
        self.x = x
        self.y = y

    def draw(self):
        glPushMatrix()
        glTranslate(self.x, self.y, 0)
        
        #glColor3fv((1, 1, 1))
        glBegin(GL_LINES)
        for e in self.edges:
            glVertex3fv(self.v[e[0]])
            glVertex3fv(self.v[e[1]])
        glEnd()
        glPopMatrix()

pygame.init()
size = (400, 300)
pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()


gluPerspective(45, size[0] / size[1], 0.1, 40.0)
glTranslatef(0.0, 0.0, -20)

cube1 = Cube(-3, 0)
cube2 = Cube(3, 0)

#run = True
while True:
    #clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    cube1.x = max(-6, min(6, cube1.x + (keys[pygame.K_d] - keys[pygame.K_a]) * 0.1))
    cube1.y = max(-6, min(6, cube1.y + (keys[pygame.K_w] - keys[pygame.K_s]) * 0.1))
    cube2.x = max(-6, min(6, cube2.x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 0.1))
    cube2.y = max(-6, min(6, cube2.y + (keys[pygame.K_UP] - keys[pygame.K_DOWN]) * 0.1))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube1.draw()
    #cube2.draw()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
exit()