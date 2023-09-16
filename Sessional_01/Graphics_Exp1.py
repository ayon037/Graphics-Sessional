import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices_3d = ((1,1,1),(-1,1,1),(-1,-1,1),(1,-1,1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,-1))
edges_3d = ((0,1),(0,3),(1,2),(2,3),(2,6),(1,5),(4,5),(4,7),(6,7),(3,7),(5,6),(0,4))

def rec_3d():
   glBegin(GL_LINES)
   for edge in edges_3d:
      for vertex in edge:
         glVertex3fv(vertices_3d[vertex])
   glEnd()

def main():
    
   pygame.init()
   display = (800,600)
   pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
   
   gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

   glTranslatef(0.0,0.0, -5)
   
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
      glRotatef(3, 3, 3, 3)
      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
      
      
      rec_3d()
      
      pygame.display.flip()
      pygame.time.wait(100)
   
   

if __name__ == "__main__":
    main()
