import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *

cube_verticies = (
   ( 1, -1, -1),  # 0
   ( 1,  1, -1),  # 1
   (-1,  1, -1),  # 2
   (-1, -1, -1),  # 3
   ( 1, -1,  1),  # 4
   ( 1,  1,  1),  # 5
   (-1, -1,  1),  # 6
   (-1,  1,  1)   # 7
)

cube_surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

uv = [(0, 0), (0, 1), (1, 1), (1, 0)]

texture = ['Images\\Netherite.jpg', 'Images\\magma.png', 'Images\\grass.jpg', 'Images\\brick.jpg', 'Images\\woodtiles.jpg', 'Images\\roof.jpg']


def Cube(surface):
    glEnable(GL_DEPTH_TEST)
    glBegin(GL_QUADS)
    for ti, vertex in enumerate(surface):
        glTexCoord2fv(uv[ti])
        glVertex3fv(cube_verticies[vertex])
    glEnd()    
    
def Cube_texture(file_path):
    image = pg.image.load(file_path)
    datas = pg.image.tostring(image, 'RGBA')
    
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
    glTranslate(0.0, 0.0, -8)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotate(2, 3, 2, 1)
        for i, surface in enumerate(cube_surfaces):
            Cube_texture(texture[i])
            Cube(surface)
        pg.display.flip()
        pg.time.wait(5)


if __name__ == '__main__':
    main()