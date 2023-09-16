# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 23:58:40 2023

@author: User
"""

"""
Created on Thu Aug 17 17:11:24 2023

@author: shaikikat
"""

import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
uv = [(0,0),(0,1),(1,1),(1,0)]

def wireCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

def solidCube():
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()
    

def Read_Image_Add_Texture():
    image = pg.image.load('woodtiles.jpg')
    datas = pg.image.tostring(image,'RGBA')
    texID = glGenTextures(1)
    
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA8, image.get_width(), image.get_height())
    glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, image.get_width(), image.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, datas)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glEnable(GL_TEXTURE_2D)

def main():
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        solidCube()
        Read_Image_Add_Texture()
        #wireCube()
        pg.display.flip()
        pg.time.wait(10)

if __name__ == "__main__":
    main()