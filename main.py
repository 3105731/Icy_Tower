from Ball import*
from Plates import*
from arrow import*
from text import *
def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	if G.frastom_top - G.ball.top <= 200 and G.score > 3:
		G.frastom_bottom = G.frastom_bottom - G.ball_dir_y + 10
		G.frastom_top = G.frastom_top - G.ball_dir_y + 10
	else:
		if G.score > 3 and G.score <= 50:
			G.frastom_bottom += 1
			G.frastom_top += 1
		elif G.score > 50 and G.score <= 100:
			G.frastom_bottom+=1.5
			G.frastom_top+=1.5
		elif G.score > 100 : 
			G.frastom_bottom+=2
			G.frastom_top+=2
	glOrtho(0, 800,G.frastom_bottom ,G.frastom_top, -1.0, 1.0) # left, right, bottom, top, near, far
	glMatrixMode(GL_MODELVIEW)
def game_over():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
def draw():
	init()
	if G.gamestart is True and G.gameover is not True:
		glColor3f(1.0, 1.0, 1.0)
		stairs()
		glColor(1,0,0)
		player()
		glLoadIdentity()
		normal_score = "Score"
		Text(normal_score,20,G.frastom_top-160)
		scoreNum = str(G.score)
		Text(scoreNum,50,G.frastom_top-200)

		High_Score = "High Score"
		Text(High_Score,20,G.frastom_top-90)
		HighScoreNum = str(G.hight_score)
		Text(HighScoreNum,50,G.frastom_top-130)
	else :
		game_over()
	glutSwapBuffers()

def game_timer(v):
	draw()
	glutTimerFunc(G.INTERVAL, game_timer, 1)

def main():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(800, 800)
	glutInitWindowPosition(100, 100)
	glutCreateWindow (b"OpenGL - First window demo")
	glutTimerFunc(G.INTERVAL, game_timer, 1)
	glutKeyboardFunc(keypress)
	glutSpecialFunc(keypress)
	glutSpecialUpFunc(reset_keys)
	glutDisplayFunc(draw)
	glutMainLoop()

main()