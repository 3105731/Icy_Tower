from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import pygame
man_path_array=['images/icyman1.jpg',]
man_path=man_path_array[0]

INTERVAL = 10

# frastom
frastom_top = 800
frastom_bottom = 0
g = 9.8

# ball
factor = 1
dtime = .1
ball_y_velocity = 0
ball_x_velocity = 0
ball_dir_y = -1
ball_dir_x = 1
moving_up = 16
moving_down = 0
on_plate = False
jumping = False
increaseF = True
score = 0 
hight_score = 0 
game_over = False 
# keyboard
keystates = [False, False, False, False]
gamestart=False
gameover=False
# plates
plates = []
stair_step_x = 2
names=[0,1,2,3,4,5,6,7]
def texture_setup(texture_image_string, texture_name, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_name)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGBA, 
                GL_UNSIGNED_BYTE, texture_image_string)
    

def load_textures():

    global names,man_path
    glEnable(GL_TEXTURE_2D)
    images=[]
    textures=[]
    paths=["images/bp.jpg","images/exitGame.png",
            "images/gameover.png","images/plate.png",man_path
	,'images/startPlay.png','images/icytower.png','images/icyT.png']

    for path in paths:
        images.append(pygame.image.load(path))
    
    for image in images:
        textures.append(pygame.image.tostring(image, "RGBA", True))
    
    glGenTextures(len(images),names)
    
    for i in range(len(images)):
        texture_setup(textures[i], names[i], images[i].get_width(), images[i].get_height())
# frastom


def change_man_path():
    global man_path
    manimg=pygame.image.load(man_path)
    stringimg=pygame.image.tostring(manimg,'RGBA',True)
    texture_setup(stringimg,names[4], manimg.get_width(),manimg.get_height())

class Rec:
    def __init__(self, t, b, r, l):
        self.top = t
        self.bottom = b
        self.right = r
        self.left = l
        self.direction = 1
        self.landed = 0

    def drawrec(self):
        glLoadIdentity()
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

wall=Rec(frastom_top + frastom_bottom,frastom_bottom,800,0)
gameo = Rec(600,200,550,200)
startplay = Rec(500,400,500,250)
exitgame = Rec(350,250,500,250)
pic_choose = 0
ball = Rec(20, 0, 510, 490)

def player_mover_x(player : Rec):  # x_movemet
    global factor, ball_x_velocity, ball_dir_x, increaseF, keystates , pic_choose

    ball_x_velocity = 0  # need to be تتفهم
    if increaseF:  # if the kay being pressed
        factor += 1
    else:
        factor = 1
    if keystates[0] == True and ball.left > 10:  # LEFT OR right
        ball_x_velocity += factor * 0.1 * ball_dir_x

    if keystates[1] == True and ball.right < 790:  # LEFT OR right
        ball_x_velocity += factor * 0.1 * ball_dir_x

    player.left += ball_x_velocity
    player.right += ball_x_velocity


def player_mover_y(player : Rec):  # y_movemet
    global frastom_top, frastom_bottom, dtime , score , game_over , hight_score
    global ball_y_velocity, on_plate, jumping, moving_up, moving_down, plates, stair_step_x
    global gameover,gamestart
    if jumping:
        ball_y_velocity = moving_up
        moving_up -= 10 * dtime
        if moving_up <= 0:
            jumping = False
        player.bottom += ball_y_velocity
        player.top = player.bottom + 20

    if jumping is False:
        for plate in plates:
            plate : Rec
            if (player.left + 10 >= plate.left and player.right - 10 <= plate.right
                    and plate.top >= player.bottom >= plate.bottom):
                ball_y_velocity = 0
                player.bottom = plate.top
                player.top = player.bottom + 20
                # player.left += stair_step_x * plate.direction
                # player.right += stair_step_x * plate.direction
                moving_up = 16
                on_plate = True
                moving_down = 0
                if plate.landed == False :
                    plate.landed = True 
                    score +=1
                    if score > hight_score :
                        hight_score = score  
                    print(score)
                break
            # elif (((plate.left <= player.right < plate.right) or
            #        (plate.right >= player.left > plate.left)) and
            #       plate.top <= player.top and plate.bottom >= player.bottom):
            #     plate.direction = -1 * plate.direction
            else:
                on_plate = False
        if player.bottom > frastom_bottom and on_plate is False:
            ball_y_velocity = moving_down
            moving_down += 1.85 * dtime
            player.bottom -= ball_y_velocity
            player.top = player.bottom + 20
            if player.bottom <=0:
                gameover=True
                gamestart=False

    if frastom_bottom > 0 and ( ball.bottom < frastom_bottom  ) :
        game_over = True
        print(game_over)

    if ball.bottom <= frastom_bottom:
        ball.bottom = frastom_bottom
        ball.top = frastom_bottom + 20
        moving_up = 16
        moving_down = 0


def createPlate():
    if not plates:
        x = random.randint(0, 600)
        left = x
        right = x + (random.randint(180, 250)) 
        top = 100
        bottom = 90
        rec = Rec(top, bottom, right, left)
        plates.append(rec)

    if plates[-1].top <= frastom_top - 100:
        x = random.randint(100, 450)
        left = x
        right = x + (random.randint(100, 200))
        top = plates[-1].top + 100
        bottom = plates[-1].bottom + 100
        rec = Rec(top, bottom, right, left)
        plates.append(rec)


def stairs():
    global plates, stair_step_x
    createPlate()
    for i in range(0, len(plates), 1):
        # plates[i].right += stair_step_x * plates[i].direction
        # plates[i].left += stair_step_x * plates[i].direction
        # if plates[i].right >= 800:
        #     plates[i].direction = -1
        # elif plates[i].left <= 0:
        #     plates[i].direction = 1
        glBindTexture(GL_TEXTURE_2D,names[3])
        plates[i].drawrec()


def player():
    global ball
    player_mover_x(ball)
    player_mover_y(ball)
    glBindTexture(GL_TEXTURE_2D,names[4])
    ball.drawrec()


def keypress(key, x, y):
    global gamestart , gameover
    global ball_dir_x, jumping, increaseF, keystates

    if ball.left > 0:  # to detect the windo
        if key == GLUT_KEY_LEFT:
            ball_dir_x = -1
            keystates[0] = True
            increaseF = True

    if ball.right < 800:  # to detect the windo
        if key == GLUT_KEY_RIGHT:
            ball_dir_x = 1
            keystates[1] = True
            increaseF = True

    if key == GLUT_KEY_UP:
        keystates[2] = True
        jumping = True
    if key == b"s":
        gamestart=True
        gameover=False

    if key == GLUT_KEY_DOWN:  # TODO:remove
        ball.top -= 30
        ball.bottom -= 30
    glutPostRedisplay()


def reset_keys(key, x, y):
    global increaseF, keystates
    keystates = [False, False, False, False]
    increaseF = False
    glutPostRedisplay()  # to redraw the scene


def init():
    global frastom_top , ball , frastom_bottom , frastom_top , ball_dir_x , ball_y_velocity  
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if frastom_top - ball.top <= 200 and score > 3:
        frastom_bottom = frastom_bottom - ball_dir_y + 10
        frastom_top = frastom_top - ball_dir_y + 10
    else:
        if score > 3:
            frastom_bottom += 1
            frastom_top += 1
    glOrtho(0, 800, frastom_bottom, frastom_top, -1.0, 1.0)  # left, right, bottom, top, near, far
    
    glMatrixMode(GL_MODELVIEW)


def draw():
    global game_over , score , hight_score , frastom_top
    init()
    if not game_over :
        glLoadIdentity()
        glBindTexture(GL_TEXTURE_2D,names[0])
    wall.drawrec()
    if gamestart==False and gameover==False:
        glBindTexture(GL_TEXTURE_2D,names[6])
        wall.drawrec()
        glBindTexture(GL_TEXTURE_2D,names[5])
        startplay.drawrec()
        glBindTexture(GL_TEXTURE_2D,names[1])
        exitgame.drawrec()
    if gamestart:
        glBindTexture(GL_TEXTURE_2D,names[0])
        wall.drawrec()
        stairs()
        player()
    if gameover==True:
        glBindTexture(GL_TEXTURE_2D,names[7])
        wall.drawrec()
        glBindTexture(GL_TEXTURE_2D,names[2])
        gameo.drawrec()
        normal_score = "Score"
        Text(normal_score,20,frastom_top-160)
        scoreNum = str(score)
        Text(scoreNum,50,frastom_top-200)

        High_Score = "High Score"
        Text(High_Score,20,frastom_top-90)
        HighScoreNum = str(hight_score)
        Text(HighScoreNum,50,frastom_top-130)
    glutSwapBuffers()

def Text(score,x,y):
    glLineWidth(3)
    glColor(1,1,1)
    glLoadIdentity()
    glTranslate(x,y,0)
    glScale(0.19,0.19,1)
    string = score.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN,c)

def game_timer(v):
    draw()
    glutTimerFunc(INTERVAL, game_timer, 1)





def main():
    global frastom_top, frastom_bottom, dtime , score , game_over , hight_score
    global ball_y_velocity, on_plate, jumping, moving_up, moving_down, plates, stair_step_x
    global gameover,gamestart
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(100, 10)
    glutCreateWindow(b"OpenGL - Working Ice Tower")
    glutDisplayFunc(draw)
    load_textures()
    glutTimerFunc(INTERVAL, game_timer, 1)
    glutKeyboardFunc(keypress)
    glutSpecialFunc(keypress)
    glutSpecialUpFunc(reset_keys)
    glutMainLoop()


main()