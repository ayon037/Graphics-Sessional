import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0,0),
    (2,0),
    (1,2)
)

edges = (
    (0,1),
    (0,2),
    (1,2),
)

def Triangle():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex2fv(vertices[vertex])
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
        Triangle()
        # glRotatef(1,3,1,1)
        pygame.display.flip()
        pygame.time.wait(10)
        
if __name__ == "__main__":
    main()