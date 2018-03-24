from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import numpy as np
import sys

x=0
angle = 0
k = 0.1
y = 0.01

def myinit():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    #glOrtho(-10,10,-10,10,-10,10)##2d##
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)

def Draw():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global angle
    global y
    global k
    glMatrixMode(GL_MODELVIEW)
######### ROAD###############
    glLoadIdentity()
    glColor3f(.3, .3, .3)
    glTranslate(0, -1.80, 0)
    glScale(100, .5, 10)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(0, -1.80, 0)
    glScale(5, 0, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(7, -1.80,0)
    glScale(5, 0, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-10, -1.80, 0)
    glScale(5, 0, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-22, -1.80, 0)
    glScale(5, 0, .5)
    glutSolidCube(1)
############## TREE##############
    glLoadIdentity()
    glColor3f(.3, 0, 0)
    glTranslate(0, -1, -5)
    glRotate(90, 1, 0, 0)
    glScale(0.5, 1, -5)
    glutSolidCylinder(1, 2, 10, 10)
    glColor3f(0, 1, 0)
    glRotate(90, 1, 0, 0)
    glTranslate(0, 1.5, 0)
    glScale(4, 10, 5)
    glutSolidSphere(1, 2, 20)

    glLoadIdentity()
    glColor3f(.3, 0, 0)
    glTranslate(4,-1,-5)
    glRotate(90, 1, 0, 0)
    glScale(0.5, 1, -5)
    glutSolidCylinder(1, 2, 10, 10)
    glColor3f(0, 1, 0)
    glRotate(90, 1, 0, 0)
    glTranslate(0, 1.5, 0)
    glScale(4, 10, 5)
    glutSolidSphere(1, 2, 20)

    glLoadIdentity()
    glColor3f(.3, 0, 0)
    glTranslate(-12, -1, -5)
    glRotate(90, 1, 0, 0)
    glScale(0.5, 1, -5)
    glutSolidCylinder(1, 2, 10, 10)
    glColor3f(0, 1, 0)
    glRotate(90, 1, 0, 0)
    glTranslate(0, 1.5, 0)
    glScale(4, 10, 5)
    glutSolidSphere(1, 2, 20)

    glLoadIdentity()
    glColor3f(.3, 0, 0)
    glTranslate(-8, -1, -5)
    glRotate(90, 1, 0, 0)
    glScale(0.5, 1, -5)
    glutSolidCylinder(1, 2, 10, 10)
    glColor3f(0, 1, 0)
    glRotate(90, 1, 0, 0)
    glTranslate(0, 1.5, 0)
    glScale(4, 10, 5)
    glutSolidSphere(1, 2, 20)

    glLoadIdentity()
    glColor3f(.3, 0, 0)
    glTranslate(-20, -1, -5)
    glRotate(90, 1, 0, 0)
    glScale(0.5, 1, -5)
    glutSolidCylinder(1, 2, 10, 10)
    glColor3f(0, 1, 0)
    glRotate(90, 1, 0, 0)
    glTranslate(0, 1.5, 0)
    glScale(4, 10, 5)
    glutSolidSphere(1, 2, 20)

    glLoadIdentity()
    glColor3f(.3, 0, 0)
    glTranslate(-16, -1, -5)
    glRotate(90, 1, 0, 0)
    glScale(0.5, 1, -5)
    glutSolidCylinder(1, 2, 10, 10)
    glColor3f(0, 1, 0)
    glRotate(90, 1, 0, 0)
    glTranslate(0, 1.5, 0)
    glScale(4, 10, 5)
    glutSolidSphere(1, 2, 20)

    glLoadIdentity()
    glColor3f(.3, 0, 0)
    glTranslate(-6, -1, -5)
    glRotate(90, 1, 0, 0)
    glScale(0.5, 1, -5)
    glutSolidCylinder(1, 2, 10, 10)
    glColor3f(0, 1, 0)
    glRotate(90, 1, 0, 0)
    glTranslate(0, 1.5, 0)
    glScale(4, 10, 5)
    glutSolidSphere(1, 2, 20)

    ###CAR#############
    glLoadIdentity()
    glColor3f(1,0,0)
    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)
    ####
    glLoadIdentity()
    glColor3f(0, 1, 0)
    glTranslate(x+0,.25*5,0)
    glScale(.5,.25,.5)
    glutWireCube(5)
    #####Torus1##########
    glColor3f(0,0,0)
    glLoadIdentity()
    glTranslate(x+2.5,-2.5*.25,2.5*.5)
    glRotate(angle,0,0,1)
    glutWireTorus(.125,.5,12,8)
    ######Torus2########
    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x+2.5,-2.5*.25,-2.5*.5)
    glRotate(angle,0,0,1)
    glutWireTorus(.125, .5, 12, 8)
    ######Torus3########
    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x+-2.5,-2.5*.25,2.5*.5)
    glRotate(angle,0,0,1)
    glutWireTorus(.125, .5, 12, 8)
    ######Torus4########
    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x+-2.5,-2.5*.25,-2.5*.5)
    glRotate(angle,0,0,1)
    glutWireTorus(.125, .5, 12, 8)
    #####lamp1#######
    glColor(0, 1, 0)
    glLoadIdentity()
    glTranslate(x, 0, 0)
    glTranslate(2.2, -.3, .4)
    glScale(.25, 1, 1)
    glutSolidSphere(.3, 20, 20)
    #####lamp2#######
    glLoadIdentity()
    glTranslate(x, 0, 0)
    glTranslate(2.2, -.3, -.4)
    glScale(.25, 1, 1)
    glutSolidSphere(.3, 20, 20)
    ######forward&backward moving car########
    if x >6.9:
        y = -0.01
        k = -0.1
    elif x < -15.9:
        y = 0.01
        k = 0.1
    x += y
    angle -= k
    #########################################












    glFlush()












glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)   # Set the window's initial width & height
glutCreateWindow(b"moving car")
glutDisplayFunc(Draw)
glutIdleFunc(Draw)
#glutIdleFunc(draw)
#glutKeyboardFunc(KeyPressed)
glutPostRedisplay()
myinit()
glutMainLoop()


