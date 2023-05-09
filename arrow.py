from Rectangle import *

def keypress(key, x, y):
	if G.ball.left > 0: #to detect the windo
		if key == GLUT_KEY_LEFT:
			G.ball_dir_x = -1
			G.keystates[0] = True
			G.increaseF = True

	if G.ball.right < 800: #to detect the windo
		if key == GLUT_KEY_RIGHT:
			G.ball_dir_x = 1
			G.keystates[1] = True
			G.increaseF = True

	if key == GLUT_KEY_UP:
		G.keystates[2] = True
		G.jumping = True

	if key == b's' and (G.start == False and G.gameover == True) :
		G.gamestart=True
		G.gameover=False
		G.score = 0
		G.frastom_bottom = 0 
		G.frastom_top = 800 
		G.ball.bottom = 0 
		G.ball.top = 20
		G.plates = []
		for plate in G.plates:
			plate : Rec 
			if plate.landed == True :
				plate.landed = False 
			else :
				break 
	if key == GLUT_KEY_DOWN:			 #TODO:remove 
		G.ball.top -= 30
		G.ball.bottom -= 30
	glutPostRedisplay()

def reset_keys(key,x,y):
	G.keystates = [False, False, False, False]
	G.increaseF = False
	glutPostRedisplay() # to redraw the scene
