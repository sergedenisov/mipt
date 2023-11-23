import math
import random
import time

from random import choice

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
shots = 0


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.time = 0



    def move(self):
        self.time += 1
        if self.time == 120:
            balls.pop(0)
        if self.x>=780:
            self.vx *= -0.6
            self.x = 780


        if self.y>=560:
            if abs(self.vy) < 3:
                self.vy = 0

            else:
                self.vy *= -0.6
                self.vx *= 0.6
                self.y =560
        else:
            self.vy += -1.5

        if abs(self.vx) <= 1:
            self.vx = 0
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        xt = obj.x
        yt = obj.y
        rt = obj.r
        if (xt - self.x)**2 + (yt - self.y)**2 <= (rt + self.r)**2:
            return True

        else:
            return False
class BallShotgun:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x1 = x - random.uniform(0, 20)
        self.y1 = y - random.uniform(0, 20)
        self.x2 = x
        self.y2 = y
        self.x3 = x + random.uniform(0, 20)
        self.y3 = y + random.uniform(0, 20)
        self.r = 1
        self.vx1 = 0
        self.vy1 = 0
        self.vx2 = 0
        self.vy2 = 0
        self.vx3 = 0
        self.vy3 = 0
        self.color = GREY
        self.live = 30
        self.time = 0



    def move(self):
        self.time += 1
        if self.time == 120:
            balls.pop(0)
        if self.x1>=780:
            self.vx1 *= -0.6
            self.x1 = 780


        if self.y1>=560:
            if abs(self.vy1) < 3:
                self.vy1 = 0

            else:
                self.vy1 *= -0.6
                self.vx1 *= 0.6
                self.y1 =560
        else:
            self.vy1 += -1.5

        if abs(self.vx1) <= 1:
            self.vx1 = 0
        self.x1 += self.vx1
        self.y1 -= self.vy1

        if self.x2>=780:
            self.vx2 *= -0.6
            self.x2 = 780


        if self.y2>=560:
            if abs(self.vy2) < 3:
                self.vy2 = 0

            else:
                self.vy2 *= -0.6
                self.vx2 *= 0.6
                self.y2 =560
        else:
            self.vy2 += -1.5

        if abs(self.vx2) <= 1:
            self.vx2 = 0
        self.x2 += self.vx2
        self.y2 -= self.vy2

        if self.x3>=780:
            self.vx3 *= -0.6
            self.x3 = 780


        if self.y3>=560:
            if abs(self.vy3) < 3:
                self.vy3 = 0

            else:
                self.vy3 *= -0.6
                self.vx3 *= 0.6
                self.y3 =560
        else:
            self.vy3+= -1.5

        if abs(self.vx3) <= 1:
            self.vx3 = 0
        self.x3 += self.vx3
        self.y3 -= self.vy3


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x1, self.y1),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x2, self.y2),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x3, self.y3),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        xt = obj.x
        yt = obj.y
        rt = obj.r
        if (xt - self.x1)**2 + (yt - self.y1)**2 <= (rt + self.r)**2 or (xt - self.x2)**2 + (yt - self.y2)**2 <= (rt + self.r)**2 or (xt - self.x3)**2 + (yt - self.y3)**2 <= (rt + self.r)**2:
            return True

        else:
            return False
class BallExplode:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = BLACK
        self.explode =0
        self.live = 30
        self.time = 0



    def move(self):
        self.time += 1
        if self.time == 30 and self.explode == 0:
            self.explode = 1
            self.time = 0

        if self.time == 10 and self.explode == 1:
            balls.pop(0)
        if self.x>=780:
            self.vx *= -0.6
            self.x = 780


        if self.y>=560:
            if abs(self.vy) < 3:
                self.vy = 0

            else:
                self.vy *= -0.6
                self.vx *= 0.6
                self.y =560
        else:
            self.vy += -1.5

        if abs(self.vx) <= 1:
            self.vx = 0

        if self.explode == 1:
            self.vx = 0
            self.vy = 0
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        if self.explode == 0:
            pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r
            )
        elif self.explode == 1:
            if self.r<60:
                self.r += 7
            pygame.draw.circle(
                self.screen,
                YELLOW,
                (self.x, self.y),
                self.r
            )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        xt = obj.x
        yt = obj.y
        rt = obj.r
        if (xt - self.x)**2 + (yt - self.y)**2 <= (rt + self.r)**2:
            return True

        else:
            return False

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.x = 20
        self.y = 450
        self.v = 5
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        global Balltype, tankX, tankY
        tankX = self.x
        tankY = self.y

    def move(self, keys):
        if keys[pygame.K_d]:
            self.x += self.v
        if keys[pygame.K_a]:
            self.x -= self.v


    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """

        if (event.pos[0]-self.x)<0:
            self.an = math.pi - math.atan2((event.pos[1]-self.y), (-1*(event.pos[0]-self.x)))
        else:
            self.an = math.atan2((event.pos[1] - self.y), (event.pos[0] - self.x))

        global shots
        shots +=1
        global balls, bullet
        bullet += 1
        if Balltype == 1:
            new_ball = Ball(self.screen)
            new_ball.r += 5
            new_ball.x = self.x
            new_ball.y = self.y
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            balls.append(new_ball)
        if Balltype == 2:
            new_ball = BallShotgun(self.screen, self.x, self.y)
            new_ball.r += 5

            new_ball.vx1 = self.f2_power * math.cos(self.an) * random.uniform(0.5, 1)
            new_ball.vy1 = - self.f2_power * math.sin(self.an) * random.uniform(0.5, 1)
            new_ball.vx2 = self.f2_power * math.cos(self.an) * random.uniform(0.5, 1)
            new_ball.vy2 = - self.f2_power * math.sin(self.an) * random.uniform(0.5, 1)
            new_ball.vx3 = self.f2_power * math.cos(self.an) * random.uniform(0.5, 1)
            new_ball.vy3 = - self.f2_power * math.sin(self.an) * random.uniform(0.5, 1)
            balls.append(new_ball)
        if Balltype == 3:
            new_ball = BallExplode(self.screen)
            new_ball.r += 5
            new_ball.x = self.x
            new_ball.y = self.y
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, ko):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.pos[0] - self.x) < 0:
                self.an = math.pi - math.atan((event.pos[1] - self.y) / (-1*(event.pos[0] - self.x)))
            else:
                self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(screen, self.color, [self.x, self.y], [self.x  +math.cos(self.an) *1.3* (self.f2_power + 15), self.y + math.sin(self.an) *1.3* (self.f2_power + 15)], 10)
        pygame.draw.rect(screen, GREY,(self.x-25, self.y-3, 50, 30))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class TargetBall:
    def __init__(self, screen: pygame.Surface, x, y):

        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.time = 0
        global tballs



    def move(self):
        self.time += 1
        if self.time == 120:
            tballs.pop(0)
        if self.x>=780:
            self.vx *= -0.6
            self.x = 780


        if self.y>=560:
            if abs(self.vy) < 3:
                self.vy = 0

            else:
                self.vy *= -0.6
                self.vx *= 0.6
                self.y =560
        else:
            self.vy += -1.5

        if abs(self.vx) <= 1:
            self.vx = 0
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


    def hittest(self, obj):

        # FIXME
        xt = obj.x
        yt = obj.y
        rt = 20
        if (xt - self.x)**2 + (yt - self.y)**2 <= (rt + self.r)**2:
            return True

        else:
            return False

class TargetY:
    def __init__(self, screen, color):
        self.screen =screen
        self.live = 1
        self.x = random.uniform(600, 780)
        self.y = random.uniform(300, 550)
        self.y0 = self.y
        self.r = random.uniform(10, 50)
        self.diff = random.uniform(30, 70)
        self.vy = random.uniform(1, 10)
        self.color = color
        self.time = 0
        self.h=0
        global clock, shots, points


    # FIXME: don't work!!! How to call this functions when object is created?
        self.new_target()
    def move(self):
        if self.y <= self.y0 - self.diff or self.y >= self.y0 + self.diff:
            self.vy *= -1
        self.y += self.vy
    def disapear(self):
        self.x = 10000
        self.y = 10000
    def new_target(self):

        self.live = 1
        self.x = random.uniform(600, 780)
        self.y = random.uniform(300, 550)
        self.y0 = self.y

        self.r = random.uniform(10, 50)
        self.diff = random.uniform(30, 70)
        self.vy = random.uniform(1, 10)


        #self.color = RED





    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
class TargetX:
    def __init__(self, screen, color):
        self.screen =screen
        self.live = 1
        self.x = random.uniform(600, 780)
        self.y = random.uniform(300, 550)
        self.x0 = self.x
        self.r = random.uniform(10, 50)
        self.diff = random.uniform(30, 70)
        self.vx = random.uniform(1, 10)
        self.color = color
        self.time = 0
        self.h=0
        global clock, shots, points


    # FIXME: don't work!!! How to call this functions when object is created?
        self.new_target()
    def move(self):
        if self.x <= self.x0 - self.diff or self.x >= self.x0 + self.diff:
            self.vx *= -1
        self.x += self.vx
    def disapear(self):
        self.x = 10000
        self.y = 10000
    def new_target(self):

        self.live = 1
        self.x = random.uniform(600, 780)
        self.y = random.uniform(300, 550)
        self.x0 = self.x

        self.r = random.uniform(10, 50)
        self.diff = random.uniform(30, 70)
        self.vx = random.uniform(1, 10)


        #self.color = RED





    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
class TargetEllipse:
    def __init__(self, screen, color):
        self.screen = screen
        self.live = 1
        self.x = random.uniform(600, 780)
        self.y = random.uniform(50, 300)
        self.x0 = self.x
        self.y0 = self.y
        self.t = 0

        self.w = random.uniform(5, 10)

        self.r1 = random.uniform(20, 100)
        self.r2 = random.uniform(20, 100)

        self.r = random.uniform(10, 50)
        self.color = color
        self.time = 0
        self.h=0
        global clock, shots, points

        self.v = 20
        global tankX, tankY, tballs





    # FIXME: don't work!!! How to call this functions when object is created?
        self.new_target()
    def move(self):
        self.time+=1
        if self.time == 60:
            self.a = random.uniform(0, 2*math.pi)
            new_ball = TargetBall(self.screen, self.x, self.y)
            new_ball.r += 5
            new_ball.vx = -self.v * math.cos(self.a)
            new_ball.vy = -self.v * math.sin(self.a)
            tballs.append(new_ball)
            self.time = 0
        self.t += 0.01
        self.x = self.x0 + self.r1*math.sin(self.w * self.t)
        self.y = self.y0 + self.r2*math.cos(self.w * self.t)
    def disapear(self):
        self.x0 = 10000
        self.y0 = 10000
    def new_target(self):

        self.live = 1
        self.x = random.uniform(500, 680)
        self.y = random.uniform(50, 300)
        self.x0 = self.x
        self.y0 = self.y
        self.t = 0
        self.w = random.uniform(5, 10)

        self.r1 = random.uniform(20, 100)
        self.r2 = random.uniform(20, 100)

        self.r = random.uniform(10, 50)


        #self.color = RED





    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

        


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
tballs = []

h1 =0
h2 =0
h3 =0
points = 0
clock = pygame.time.Clock()
gun = Gun(screen)
target1 = TargetY(screen, RED)
target3 = TargetX(screen, YELLOW)

target2 = TargetEllipse(screen, BLUE)

finished = False
message_end_time = 0
time = 0
time0 = 0
k1=0
k2=0
k3=0
l=0

Balltype = 1
gameover = 0

tankX = 0
tankY = 0

while not finished:

    screen.fill(WHITE)
    font1 = pygame.font.SysFont(None, 40)
    img1 = font1.render('%d' % points, True, BLUE)
    screen.blit(img1, (20, 20))
    gun.draw()

    target1.move()
    target2.move()
    target3.move()

    target1.draw()
    target2.draw()
    target3.draw()


    for b in balls:
        b.draw()
    for tb in tballs:
        tb.draw()
    keys = pygame.key.get_pressed()  # Checking pressed keys
    gun.move(keys)

    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                Balltype = 1
            if event.key == pygame.K_2:
                Balltype = 2
            if event.key == pygame.K_3:
                Balltype = 3

        elif event.type == pygame.MOUSEBUTTONDOWN and h1==0 and h2==0:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and h1==0 and h2==0:
            gun.fire2_end(event)

        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    for b in balls:
        b.move()
        if b.hittest(target1) and target1.live and h1==0 and h2==0 and h3==0:
            time0 = time
            h1 = 1
            k1 = 1
        if b.hittest(target2) and target2.live and h1==0 and h2==0 and h3==0:
            time0 = time
            h2 = 1
            k2 = 1
        if b.hittest(target3) and target3.live and h1==0 and h2==0 and h3==0:
            time0 = time
            h3 = 1
            k3 = 1
    for tb in tballs:
        tb.move()
        if tb.hittest(gun):
            gameover = 1

    if h1==1:
        if k1== 1:
            points +=1
            k1=0
        font1 = pygame.font.SysFont(None, 40)
        img1 = font1.render('Вы уничтожили цель за %d выстрелов' % shots, True, BLUE)
        screen.blit(img1, (200, 200))
        target1.disapear()

        if time - time0>90:
            h1=0
            time0=0
            time=0
            target1.live = 0
            target1.new_target()
            shots = 0
    if h2==1:
        if k2== 1:
            points +=1
            k2=0
        font1 = pygame.font.SysFont(None, 40)
        img1 = font1.render('Вы уничтожили цель за %d выстрелов' % shots, True, BLUE)
        screen.blit(img1, (200, 200))
        target2.disapear()

        if time - time0>90:
            h2=0
            time0=0
            time=0
            target2.live = 0
            target2.new_target()
            shots = 0
    if h3==1:
        if k3== 1:
            points +=1
            k3=0
        font1 = pygame.font.SysFont(None, 40)
        img1 = font1.render('Вы уничтожили цель за %d выстрелов' % shots, True, BLUE)
        screen.blit(img1, (200, 200))
        target3.disapear()

        if time - time0>90:
            h3=0
            time0=0
            time=0
            target3.live = 0
            target3.new_target()
            shots = 0

    if gameover == 1 and l == 0:
        l = 1
        time = 0
    if gameover == 1:
        font1 = pygame.font.SysFont(None, 40)
        img1 = font1.render('Вы проиграли, вы вас попали', True, BLUE)
        screen.blit(img1, (200, 200))
    if gameover == 1 and time > 120:
        pygame.quit()
    time+=1

    pygame.display.update()


    gun.power_up()



pygame.quit()
