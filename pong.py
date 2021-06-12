#Create your own shooter

from pygame import *
from random import *
clock = time.Clock()
FPS = 60
#create game window
window_width = 1200
window_height = 900
window = display.set_mode((window_width,window_height))
#set scene background
background = transform.scale(image.load("C:/Users/AAL/Documents/Python/Test images/background.jpg"),(window_width,window_height))
#create 2 sprites and place them on the scene
sprite1 = transform.scale(image.load("C:/Users/AAL/pongpygame/Pong_in_Pygame-master/Paddle.png"),(10,100))
font.init()
#handle "click on the "Close the window"" event 
mixer.init()
mixer.music.load("C:/Users/AAL/Documents/musiccc.mp3")
mixer.music.play()
#money = mixer.Sound("money.ogg")
#kick = mixer.Sound("kick.ogg")
font.init()
font1 = font.SysFont('Arial',36)
game = True

class GameSprite(sprite.Sprite):
    def __init__(self,size_x,size_y,player_image,player_x,player_y,x_speed,y_speed):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.y >= 0:
            self.rect.y -= 10
        if key_pressed[K_RIGHT] and self.rect.y <= 800:
            self.rect.y += 10

class Player2(GameSprite):
    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.y >= 0:
            self.rect.y -= 10
        if key_pressed[K_d] and self.rect.y <= 800:
            self.rect.y += 10


class Ball(GameSprite):
    def update(self):
        self.rect.y -= self.y_speed
        self.rect.x -= self.x_speed
        if self.rect.x <= 0:
            self.kill()
            text_win = font1.render("P2 WINS",1,(255,255,255))
            window.blit(text_win,(250,350))
        if self.rect.x >= 1200:
            self.kill()
            text_win = font1.render("P1 WINS",1,(255,255,255))
            window.blit(text_win,(250,350))
        if ball.rect.y >= 900 or ball.rect.y <= 0:
            self.y_speed *= -1
        if sprite.collide_rect(p1,ball) or sprite.collide_rect(p2,ball):
            self.x_speed *= -1



        

            



p1 = Player1(10,100,"C:/Users/AAL/pongpygame/Pong_in_Pygame-master/Paddle.png",1150,400,4,5)
p2 = Player2(10,100,"C:/Users/AAL/pongpygame/Pong_in_Pygame-master/Paddle.png",50,100,4,5)
ball = Ball(30,30,"C:/Users/AAL/pongpygame/Pong_in_Pygame-master/Ball.png",600,450,7,10)


finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    
    if finish != True:
        p1.reset()
        p1.update()
        p2.reset()
        p2.update2()
        ball.reset()
        ball.update()
        

        display.update()
        window.blit(background,(0,0))
    clock.tick(FPS)
    