from Rectangle import *
# import G as G

G.ball = Rec(20, 0 ,510, 490)

def player_mover_x(player):
	# x movemet
	G.ball_x_velocity = 0 # need to be تتفهم 
	if G.increaseF == True: # if the kay being pressed 
		G.factor += 1
	else:
		G.factor = 1

	if G.keystates[0] == True and  player.left > 10: # LEFT OR right 
			G.ball_x_velocity += G.factor * 0.1 * G.ball_dir_x

	if G.keystates[1] == True and player.right < 790:# LEFT OR right 
			G.ball_x_velocity += G.factor * 0.1 * G.ball_dir_x
	
	player.left +=G.ball_x_velocity
	player.right += G.ball_x_velocity


def player_mover_y(player):
	
	if G.jumping == True:
		G.ball_y_velocity = G.moving_up 
		G.moving_up -= 10 * G.dtime
		if G.moving_up <= 0:
			G.jumping = False
		player.bottom += G.ball_y_velocity
		player.top = player.bottom + 20

	if G.jumping is False :	#and G.land == False
		for plate in G.plates:
			if (player.left + 10 >= plate.left and player.right - 10 <= plate.right 
			and plate.top >= player.bottom >= plate.bottom):
				player.bottom = plate.top
				player.top = player.bottom + 20
				player.left += G.stair_step_x * plate.direction
				player.right += G.stair_step_x * plate.direction
				if plate.landed is not True:
					G.score += 1
				plate.landed = True
				G.moving_up = 16
				G.moving_down = 0
				G.ball_y_velocity = 0
				if G.hight_score < G.score:
					G.hight_score = G.score
				G.on_plate = True 	#لو مش مهمه اسمح
				break
			elif (((plate.left <= player.right < plate.right) or
		   (plate.right >= player.left > plate.left)) and
		  plate.top <= player.top and plate.bottom >= player.bottom):
				plate.direction = -1 * plate.direction
			else:
				G.on_plate = False
		if player.bottom > G.frastom_bottom and G.on_plate == False:
			G.ball_y_velocity = G.moving_down
			G.moving_down += 1.85 * G.dtime 
			player.bottom -= G.ball_y_velocity
			player.top = player.bottom + 20

	if G.frastom_bottom > 0 and (player.bottom < G.frastom_bottom):
		game_over = True
		print(game_over)
	if G.ball.bottom <= G.frastom_bottom:
		G.ball.bottom = G.frastom_bottom
		G.ball.top = G.frastom_bottom + 20
		G.moving_up = 16
		G.moving_down = 0

#TODO: المفروض لما يطلع من برا الطبق يقع 

def player():
	# global ball
	player_mover_x(G.ball)
	player_mover_y(G.ball)
	G.ball.drawrec()

