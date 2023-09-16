import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

vertices1 = (
    (0,0),
    (0,2),
    (3,0),
    (3,2)
)

vertices2 = (
    (0,2),
    (-0.3,2),
    (-0.3,-2),
    (0,-2)
)

edges = (
    (0,2),
    (0,1),
    (1,3),
    (2,3)
)

colors = (
    (0.0, 0.5, 0.0)  # RGB color as floats (R=0.0, G=0.5, B=0.0)
)

surfaces1 = (
    (0,2,3,1),
)

surfaces2 = (
    (0,1,2,3),
)

def Rectangle1():
    glBegin(GL_QUADS)
    x=0
    for surface in surfaces1:
        for vertex in surface:
            glColor3fv([0, 128, 0])   # Set the color outside of the loop
            glVertex2fv(vertices1[vertex])
    glEnd()
    
def Rectangle2():
    glBegin(GL_QUADS)
    x=0
    for surface in surfaces2:
        for vertex in surface:
            glColor3fv([139, 69, 19])   # Set the color outside of the loop
            glVertex2fv(vertices2[vertex])
    glEnd()
    
def circle():
    posx, posy = 1,1    
    sides = 32    
    radius = 0.7    
    glEnable(GL_POLYGON_SMOOTH)  
    glBegin(GL_POLYGON)  
    glColor3fv((1, 0, 0))  
    for i in range(100):    
            cosine= radius * cos(i*2*pi/sides) + posx    
            sine  = radius * sin(i*2*pi/sides) + posy    
            glVertex2f(cosine,sine)
    glEnd()


def main():
    pygame.init()
    display=(800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(60,(display[0]/display[1]),0.1,50.0)
    glTranslatef(0.0,0.0, -5)
    glRotatef(0,0,0,0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Rectangle1()
        Rectangle2()
        circle()
        # glRotatef(1,3,1,1)
        pygame.display.flip()
        pygame.time.wait(10)
        
if __name__ == "__main__":
    main()