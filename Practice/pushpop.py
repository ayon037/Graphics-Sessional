import pygame
from math import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the points for the brown stand (rectangle)
stand_vertices = (
    (-1.1, -1.3),
    (-1, -1.3),
    (-1, 0.5),
    (-1.1, 0.5)
)

rectangle_vertices =vertices = [(-1, -0.5),
                                (1, -0.5), 
                                (1, 0.5), 
                                (-1, 0.5)]

def rectangle():
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0.3)  # Green color for the rectangle
    
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()

def circle():
    posx, posy = 0, 0    
    sides = 32 
    radius = 0.25  # Adjust the circle's radius as needed
    glBegin(GL_POLYGON)    
    glColor3f(1, 0, 0)  # Red color for the circle
    for i in range(100):    
        cosine = radius * cos(i * 2 * pi / sides) + posx    
        sine = radius * sin(i * 2 * pi / sides) + posy    
        glVertex2f(cosine, sine)
    glEnd()

def brown_stand():
    glBegin(GL_QUADS)
    glColor3f(0.36, 0.25, 0.20)  # Brown color for the stand
    for vertex in stand_vertices:
        glVertex2f(*vertex)
    glEnd()

    # Draw a small brown circle on top of the stand
    posx, posy = -1.05, 0.58  # Adjust the position of the circle
    sides = 32
    radius = 0.09  # Adjust the circle's radius as needed
    glBegin(GL_POLYGON)
    glColor3f(0.36, 0.25, 0.20)  # Brown color for the circle
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()


# =============================================================================
# def main():
#     pygame.init()
#     display = (800, 600)
#     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
# 
#     gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
# 
#     glTranslatef(0.0, 0.0, -5)
# 
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         
#         # Rotate the entire scene
#         #glRotatef(1, 1, 1, 1)    
#         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#         rectangle()
#         circle()
#         brown_stand()
#         pygame.display.flip()
#         pygame.time.wait(10)
# =============================================================================

# ...

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    # Define the initial rotation angle for the circle
    circle_angle = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Render the static rectangle and stand
        # circle()
        rectangle()
        brown_stand()

        # Rotate only the circle
        glPushMatrix()
        glRotatef(circle_angle, 1, 0, 1)  # Rotate the circle around the z-axis
        circle()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

        # Adjust the rotation speed of the circle
        circle_angle += 1  # Increase the rotation angle
        if circle_angle >= 360:
            circle_angle -= 360

if __name__ == "__main__":
    main()


