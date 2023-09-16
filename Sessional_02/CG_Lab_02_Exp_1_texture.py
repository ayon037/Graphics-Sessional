import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

v= (
   (1, -1, -1),
   (1, 1, -1),
   (-1, 1, -1),
   (-1, -1, -1),
   (1, -1, 1),
   (1, 1, 1),
   (-1, -1, 1),
   (-1, 1, 1)
)


surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

uv = [(0, 0), (0, 1), (1, 1), (1, 0)]


def Cube():
    
   glEnable(GL_DEPTH_TEST)
   
   glBegin(GL_QUADS)
   for surface in surfaces:
       
       for ti, vi in enumerate(surface):
           glTexCoord2fv(uv[ti])
           glVertex3fv(v[vi])
   glEnd()

def texture():
   image = pygame.image.load('woodtiles.jpg')
   #image = pygame.image.load('ObjectSheet.png')
   datas = pygame.image.tostring(image, 'RGBA')
   
   
   texID = glGenTextures(1)
   glBindTexture(GL_TEXTURE_2D, texID)
   
   glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA8, image.get_width(), image.get_height())
   glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, image.get_width(), image.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, datas)

   glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
   glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

   glEnable(GL_TEXTURE_2D)  
       
def main():
   
       
   pygame.init()
   display = (400,300)
   window= pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
  
  
   gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
   glTranslatef(0, 0, -5)
  
   
 
  
   while True:
       
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               quit() 
           

      

       glRotatef(1, 1, 3, 1)
       
       glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
       
       
       texture()
       Cube()   
       
       pygame.display.flip()
       pygame.time.wait(10)

      
   
   

if __name__ == "__main__":

   main()