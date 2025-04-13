from pygame import*

window = display.set_mode((700,500))
back = (120, 56, 206)
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, plaer_image, x, y, w, h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(plaer_image),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updata_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    
    def updata_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

player_l = Player('cat 2.png', 20, 200, 50, 100, 8)
player_r = Player('cat 2.png', 600, 200, 50, 100, 8)
ball = GameSprite('ball png.png', 200, 200, 40, 40, 888)

game = True
finish = False

speed_x = 3
speed_y = 3

font.init()
font1 = font.SysFont('Arial', 40)
lose1 = font1.render('Левый проиграл!', True, (102, 23, 204))
lose2 = font1.render('Правый протграл!', True, (102, 23, 204))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        player_l.reset()
        player_r.reset()
        ball.reset()
        

        player_l.updata_l()
        player_r.updata_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1

        if ball.rect.y > 440 or ball.rect.y < 5:
            speed_y *= -1

        if ball.rect.x < 5:
            finish = True
            window.blit(lose1, (200,200))
           
        if ball.rect.x > 640:
            finish = True
            window.blit(lose1, (200,200))
            
    display.update()
    time.delay(60)
