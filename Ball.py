from Rectangle import *
import Global as G
from texture import names
from texture import man_path_left,man_path_right,choose_photo,man_path,man_stand,change_man_path
from texture import man_path, man_fall , man_jump

""" land from right and left""" #TODO:
""" GAME OVER AND game start""" #TODO:

G.ball = Rec(80, 0 ,530, 470)

"""move player in x direction"""
def player_mover_x(player):
	#TODO: TEXTURE NEED TO BE REWRITTEN
	global man_path
	G.ball_x_velocity = 0  # reset x velocity
	if G.increaseF == True:
		G.factor += 1
	else:
		G.factor=1
	if G.keystates[0] == True and  player.left > 0: # LEFT OR right 
			G.ball_x_velocity += G.factor * 0.25 * G.ball_dir_x
			choose_photo(man_path_left)

	if G.keystates[1] == True and player.right < 790:
			choose_photo(man_path_right)
			G.ball_x_velocity += G.factor * 0.25 * G.ball_dir_x
	
	player.left +=G.ball_x_velocity
	player.right += G.ball_x_velocity

def player_mover_y(player):
	"""jump in y direction"""
	if G.jumping == True:
		if G.moving_up <= 0:
			G.jumping = False
		else:
			if G.keystates[1]:
				change_man_path(man_jump[1])
			else:
				change_man_path(man_jump[0])

			if G.ball_x_velocity < 0:
				G.ball_x_velocity *= -1
			G.ball_y_velocity = 0.5 * G.ball_x_velocity + G.moving_up
			G.moving_up -= 10 * G.dtime
		player.bottom += G.ball_y_velocity
		player.top = player.bottom + 80

	"""fall"""
	if G.jumping is False :	#and G.land == False
		for plate in G.plates:

			# collison detection
			if (player.left >= plate.left - 25 and player.right <= plate.right + 25
			and plate.top>= player.bottom+10  >= plate.bottom):
				player.bottom = plate.top - 15
				player.top = player.bottom + 80
				player.left += G.stair_step_x * plate.direction
				player.right += G.stair_step_x * plate.direction
	
				"""check score"""
				if plate.landed == False:
					G.score += 1
					plate.landed = True
				if G.hight_score < G.score:
					G.hight_score = G.score

				""" collison detection with plate nuts"""
				if plate.coin:
					if player.right > plate.coin.left and player.left < plate.coin.right :
						plate.coin=None
						G.score += 5

				"""reset values"""
				G.moving_up = 16
				G.moving_down = 0
				G.ball_y_velocity = 0
				G.on_plate = True

				if G.keystates[0]== False and G.keystates[1] == False: 
					change_man_path(man_stand[0])
				break
			else:
				G.on_plate = False ##used for movinf ball down

		if player.bottom > G.frastom_bottom and G.on_plate == False:
			change_man_path(man_fall[0])
			G.ball_y_velocity = G.moving_down
			G.moving_down += 1.85 * G.dtime
			player.bottom -= G.ball_y_velocity
			player.top = player.bottom + 80

	if player.bottom < G.frastom_bottom:
		G.gamestart = False
		G.gameover = True
		G.score = 0
		G.frastom_y = 0
		G.frastom_bottom = 0
		G.frastom_top = 800
		G.plates = []
		player.bottom = 0
		player.top = player.bottom + 80
		G.moving_down = 0
		G.moving_up = 16
		G.stair_step_x = 0
		change_man_path(man_stand[0])

def player():
	player_mover_x(G.ball)
	player_mover_y(G.ball)
	glBindTexture(GL_TEXTURE_2D,names[4])
	G.ball.draw_palyer()

