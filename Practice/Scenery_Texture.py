import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *


sky_vertex = (( 10, 10), ( 10,-0.9), (-10, 10), (-10,-0.9))
mati_vertex = (( 10, -0.9), ( 10,-10), (-10, -0.9), (-10,-10))


h1_vertex = (( 0, -1), ( 1, -1.15), ( 1, 0.85), (0.7,1.78), ( 0, 0.955))
h2_vertex = (( 3, 1), ( 3, -1), ( 1, 0.85), ( 1, -1.15))
w1_vertex = (( 0.25, -0.2), ( 0.25, 0.5), ( 0.75, -0.3), ( 0.75, 0.4))
d1_vertex = (( 1.75, 0.39), ( 1.75, -1.11), ( 2.25, 0.44), ( 2.25, -1.06))
r1_vertex = (( 1.075, 0.72), ( 0.55, 1.78), ( 3.3, 0.97), ( 2.8, 1.97))
r2_vertex = (( 2.8, 1.97), ( 0.55, 1.78), ( 2, 0.97), ( -0.25, 0.85))


windmill_vertex = ((-5.5, -1), (-4.5, -1), (-5, 5.5))
wm_stick_vertex = ((-5, 5), (-8, 8), (-2, 8), (-8, 2), (-2, 2))
wm_f1_vertex = ((-8  , 8), (-5.5, 5.5), (-9.25, 7.25), (-6.25, 4.75))
wm_f2_vertex = ((-2, 8), (-4.5, 5.5), (-2.75, 9.25), (-5.25, 6.25))
wm_f3_vertex = ((-8, 2), (-5.5, 4.5), (-7.25, 0.75), (-4.75, 3.75))
wm_f4_vertex = ((-2,2), (-4.5, 4.5), (-0.75, 2.75), (-3.75, 5.25))
wm_b1_vertex = ((-8,8), (-5, 5), (-8.05, 7.95), (-5, 4.95))
wm_b2_vertex = ((-2,8), (-5, 5), (-2.05, 7.95), (-5, 4.95))
wm_b3_vertex = ((-8,2), (-5, 5), (-8.05, 1.95), (-5, 4.95))
wm_b4_vertex = ((-2,2), (-5, 5), (-2.05, 1.95), (-5, 4.95))


line_edges = ((0,1), (0,2), (0,3), (0,4))
tri_surface = ((0,1,2))
rec_surface = ((0,1,3,2))
pen_surface = ((0,1,2,3,4))


uv_pentagon = [(0, 0), (1, 0), (1, 0.7), (0.5, 1), (0, 0.7)]
uv_rec = [(0, 0), (0, 1), (1, 1), (1, 0)]
uv_tri = [(0, 0), (1, 0), (0.5, 1)]


def Line(vertex, edge):
    glLineWidth(3)
    glBegin(GL_LINES)
    for e in edge:
        for v in e:
            glColor3fv((100,180,210))
            glVertex2fv(vertex[v])
    glEnd()


def Triangle(vertex, surface, color=None):
    glBegin(GL_TRIANGLES)
    for i, v in enumerate(surface):
        if color:
            glColor3fv(color)
        else:
            glTexCoord2fv(uv_tri[i])
        glVertex2fv(vertex[v])
    glEnd()


def Rectangle(vertex, surface, color=None):
    glBegin(GL_QUADS)
    for i, v in enumerate(surface):
        if color:
            glColor3fv(color)
        else:
            glTexCoord2fv(uv_rec[i])
        glVertex2fv(vertex[v])
    glEnd()


def Pentagon(vertex, surface, color=None):
    glBegin(GL_POLYGON)
    for i, v in enumerate(surface):
        if color:
            glColor3fv(color)
        else:
            glTexCoord2fv(uv_pentagon[i])
        glVertex2fv(vertex[v])
    glEnd()
        
    
def Circle(center, r, color=None):
    posx, posy = center  
    sides = 64
    radius = r   
    glBegin(GL_POLYGON)    
    for i in range(64):    
            cosine= radius * cos(i*2*pi/sides) + posx    
            sine  = radius * sin(i*2*pi/sides) + posy
            if color:
                glColor3fv(color)
            else:
                tex_x = 0.5 * (cos(i*2*pi/sides) + 1.0)  # Map x-coordinate to texture (range [-1, 1] to [0, 1])
                tex_y = 0.5 * (sin(i*2*pi/sides) + 1.0)  # Map y-coordinate to texture (range [-1, 1] to [0, 1])
                glTexCoord2f(tex_x, tex_y)
            glVertex2f(cosine,sine)
    glEnd()
    
def Texture(file_path):
    image = pg.image.load(file_path)
    datas = pg.image.tostring(image, 'RGBA')
    
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
   
    glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA8, image.get_width(), image.get_height())
    glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, image.get_width(), image.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, datas)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glEnable(GL_TEXTURE_2D)
    
    # Enable alpha blending
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)



def main():
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslate(1.5, -3.5, -15)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        
        # glTranslatef(-5, 5, 0)
        # glRotatef(1,0,0,-1)
        # glTranslatef(5, -5, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        Texture("Images/cloudy.jpg")
        Rectangle(sky_vertex, rec_surface)
        Texture("Images/dark_grass.jpg")
        Rectangle(mati_vertex, rec_surface)
        Texture("Images/sun.png")
        Circle((3,6), 2.5)
        
        Texture("Images/roof.jpg")
        Rectangle(r2_vertex, rec_surface)
        Texture("Images/brick.jpg")
        Pentagon(h1_vertex, pen_surface)
        Texture("Images/brick.jpg")
        Rectangle(h2_vertex, rec_surface)
        Texture("Images/woodtiles.jpg")
        Rectangle(w1_vertex, rec_surface)
        Texture("Images/door.jpg")
        Rectangle(d1_vertex, rec_surface)
        Texture("Images/roof.jpg")
        Rectangle(r1_vertex, rec_surface)
        
        Texture("Images/windmill.jpg")
        Triangle(windmill_vertex, tri_surface)
        Texture("Images/fan.jpg")
        Rectangle(wm_f1_vertex, rec_surface)
        Rectangle(wm_f2_vertex, rec_surface)
        Rectangle(wm_f3_vertex, rec_surface)
        Rectangle(wm_f4_vertex, rec_surface)
        # Line(wm_stick_vertex, line_edges)
        Texture("Images/bamboo.png")
        Rectangle(wm_b1_vertex, rec_surface)
        Rectangle(wm_b2_vertex, rec_surface)
        Rectangle(wm_b3_vertex, rec_surface)
        Rectangle(wm_b4_vertex, rec_surface)
        Texture("Images/wheel.png")
        Circle((-5,5), 0.3)
        
        pg.display.flip()
        pg.time.wait(50)


if __name__ == '__main__':
    main()