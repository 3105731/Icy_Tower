from Rectangle import *
def Text(score,x,y):
    glLineWidth(3)
    glColor(1,1,1)
    glLoadIdentity()
    glTranslate(x,y,0)
    glScale(0.19,0.19,1)
    string = score.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN,c)
    glBindTexture(GL_TEXTURE_2D,-1)
