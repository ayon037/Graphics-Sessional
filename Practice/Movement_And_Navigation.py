import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1),
    
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1)
)

def Cube():
    # glEnable(GL_DEPTH_TEST)
    # glLineWidth(3)
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glVertex3fv(vertices[vertex])
            glColor3fv(colors[x])
    glEnd()
    
def main():
    pygame.init()
    display=(800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(45,(display[0]/display[1]),0.1,50.0)
    glTranslatef(0.0,0.0, -5)
    glRotatef(0,0,0,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-1,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(1,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslate(0,0,-1.0)
                if event.button == 5:
                    glTranslate(0,0,1.0)
                    
            
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        # glRotatef(1,3,1,1)
        pygame.display.flip()
        pygame.time.wait(10)
            
      
if __name__ == "__main__":
    main()