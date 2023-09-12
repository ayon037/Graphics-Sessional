# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
from math import *

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
   (1, -1, -1),
   (1, 1, -1),
   (-1, 1, -1),
   (-1, -1, -1),
   (1, -1, 1),
   (1, 1, 1),
   (-1, -1, 1),
   (-1, 1, 1)
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

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

uv = [(0,0),(0,1),(1,1),(1,0)]


surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for ti,vi in enumerate(surface):
            x+=1
            glTexCoord2fv(uv[ti])
            glVertex3fv(verticies[vi])
    glEnd()
    
def Read_Image_Add_Texture():
    image = pygame.image.load('cookie.jpg')
    datas = pygame.image.tostring(image,'RGBA')
    texID = glGenTextures(1)
    
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA8, image.get_width(), image.get_height())
    glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, image.get_width(), image.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, datas)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glEnable(GL_TEXTURE_2D)


def circle():
    posx, posy = 0,0    
    sides = 32    
    radius = 1    
    glBegin(GL_POLYGON)    
    for i in range(100):    
            cosine= radius * cos(i*2*pi/sides) + posx    
            sine  = radius * sin(i*2*pi/sides) + posy    
            glVertex2f(cosine,sine)
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
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                glTranslatef(-0.5,0,0)
             if event.key == pygame.K_RIGHT:
                glTranslatef(0.5,0,0)
             if event.key == pygame.K_UP:
                glTranslatef(0,0.5,0)
             if event.key == pygame.K_DOWN:
                glTranslatef(0,-0.5,0)
         if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 4:
                 glTranslate(0,0,1.0)
      
      glRotatef(1, 1, 1, 1)
      
      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #   Cube()
    #   Read_Image_Add_Texture()
      circle()
      pygame.display.flip()
      pygame.time.wait(10)

if __name__ == "__main__":

   main()