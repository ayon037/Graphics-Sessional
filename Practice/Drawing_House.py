import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

vertices = (
    (0,0),
    (2,0),
    (2,-2),
    (0,-2),
    (0.5,1),
    (2.7,1),
    (2.7,-1.5),
    (2.7,-2),
    (2,-2.5),
    (0,-2.5),
    (0.5,-2),
    (1.5,-2),
    (0.5,-0.5),
    (1.5,-0.5),
    (2.1,-1),
    (2.6,-1),
    (2.1,-0.5),
    (2.6,-0.5),
    
)

edges = (
    (4,5),
    (4,0),
    (5,1),
    (0,1),
    (0,3),
    (1,2),
    (2,3),
    (5,6),
    (6,2),
    (6,7),
    (7,8),
    (2,8),
    (8,9),
    (3,9),
    (10,12),
    (12,13),
    (11,13),
    (14,15),
    (14,16),
    (15,17),
    (16,17)
)

colors = (
    (0.0, 0.5, 0.0)  # RGB color as floats (R=0.0, G=0.5, B=0.0)
)


def Home():
    glBegin(GL_QUADS)
    glColor3f(0.36, 0.25, 0.20)
    for edge in edges:
        for vertex in edge:
            glVertex2fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display=(800,700)
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
        Home()
        # glRotatef(1,0,1,0)
        pygame.display.flip()
        pygame.time.wait(10)
        
if __name__ == "__main__":
    main()