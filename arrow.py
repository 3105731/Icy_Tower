from Rectangle import *
from texture import man_path
from texture import man_jump,man_stand,change_man_path,man_fall

#texture fix TODO:
def keypress(key, x, y):
	global man_path,left_key,right_key

	""" moving ball to the left"""
	if G.ball.left > 0 and key == GLUT_KEY_LEFT:
		G.ball_dir_x = -1
		G.keystates[0] = True
		G.increaseF = True

	""" moving ball to the right"""
	if G.ball.right < 800 and key == GLUT_KEY_RIGHT:
		G.ball_dir_x = 1
		G.keystates[1] = True
		G.increaseF = True

	""" jumping """
	if key == GLUT_KEY_UP:
		G.keystates[2] = True
		G.jumping = True

	""" BEGIN"""
	if key == b' ' and G.gamestart is False:
		G.gamestart = True
		G.gameover = False

	glutPostRedisplay()

def reset_keys(key,x,y):
	if G.keystates[0]==True:
		change_man_path(man_jump[0])
		change_man_path(man_stand[0])

	if G.keystates[1]==True:
		change_man_path(man_jump[1])
		change_man_path(man_stand[1])

	G.keystates = [False, False, False, False]
	G.increaseF = False
	glutPostRedisplay() # to redraw the scene

