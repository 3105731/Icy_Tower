from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
import Global as G

man_fall=['images/fall_left.png','images/fall_right.png']
man_stand=['images/stand_left.png','images/stand_r.png']
man_jump=['images/jump_left.png','images/jump_right.png']
man_path_right=['images/run_right_1.png','images/run_right_2.png','images/run_right_3.png',
                'images/run_right_4.png']
man_path_left=['images/run_left_1.png','images/run_left_2.png',
                'images/run_left_3.png','images/run_left_4.png']

man_path = man_stand[0]
names=[0,1,2,3,4,5,6,7,8]

def texture_setup(texture_image_string, texture_name, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_name)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, 
                GL_UNSIGNED_BYTE, texture_image_string)
    

def load_textures():
    global names,man_path
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
    images=[]
    textures=[]
    paths=["images/bg.jpg","images/exitGame.png",
            "images/gameover.png",
            "images/plate_22.png",man_path
	,'images/startPlay.png','images/Image AM.jpg','images/23357.jpg','images/nuts.png']

    for path in paths:
        images.append(pygame.image.load(path))
    for image in images:
        textures.append(pygame.image.tostring(image, "RGBA", True))
    glGenTextures(len(images),names)
    for i in range(len(images)):
        texture_setup(textures[i], names[i], images[i].get_width(), images[i].get_height())



def change_man_path(path):
    global man_path
    man_path=path
    manimg=pygame.image.load(man_path)
    stringimg=pygame.image.tostring(manimg,'RGBA',True)
    texture_setup(stringimg,names[4], manimg.get_width(),manimg.get_height())

def choose_photo(array):
    global man_path
    f = (G.factor // 5) % 4
    man_path = array[f]
    change_man_path(man_path)
