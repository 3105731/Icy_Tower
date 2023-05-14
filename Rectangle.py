from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import Global as G

class Rec:
    def __init__(self, t, b, r, l):
        self.top = t
        self.bottom = b
        self.right = r
        self.left = l
        self.direction = 1
        self.landed = False
        self.coin=None

    def drawrec(self):
        glPushMatrix()
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex2f(self.left, self.bottom)
        glTexCoord2f(1, 0)
        glVertex2f(self.right, self.bottom)
        glTexCoord2f(1, 1)
        glVertex2f(self.right, self.top)
        glTexCoord2f(0, 1)
        glVertex2f(self.left, self.top)
        glEnd()
        glPopMatrix()

    def draw_palyer(self):
        glPushMatrix()
        glBegin(GL_QUADS)
        glTexCoord2f(0.22, 0.22)
        glVertex2f(self.left, self.bottom)
        glTexCoord2f(1, 0.2)
        glVertex2f(self.right, self.bottom)
        glTexCoord2f(1, 1)
        glVertex2f(self.right, self.top)
        glTexCoord2f(0, 1)
        glVertex2f(self.left, self.top)
        glEnd()
        glPopMatrix()




