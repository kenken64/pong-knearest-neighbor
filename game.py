import pygame

WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 15
FRAMERATE = 30

class Ball:
    RADIUS = 20

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def show(self, color):
        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), Ball.RADIUS)

    def update(self):
        global bgColor, fgColor

        newX  = self.x + self.vx
        newY  = self.y + self.vy

        if newX < BORDER + self.RADIUS:
            self.vx = - self.vx
        elif newY < BORDER + self.RADIUS or newY > HEIGHT-BORDER-self.RADIUS:
            self.vy = - self.vy
        elif newX+Ball.RADIUS > WIDTH-Paddle.WIDTH and abs(newY-paddle.y) < Paddle.HEIGHT//2:
            self.vx = - self.vx
        else:
            self.show(bgColor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(fgColor)

class Paddle:
    WIDTH =20
    HEIGHT = 80

    def __init__(self,y):
        self.y = y
    
    def show(self, color):
        global screen
        pygame.draw.rect(screen, color, 
                pygame.Rect(WIDTH-self.WIDTH, 
                            self.y-self.HEIGHT//2, 
                            self.WIDTH, self.HEIGHT))
    
    def update(self):
        global bgColor, fgColor
        newY = pygame.mouse.get_pos()[1]
        if newY-self.HEIGHT//2 > BORDER \
          and newY+self.HEIGHT//2 < HEIGHT-BORDER :
            self.show(bgColor)
            self.y = newY
            self.show(fgColor)

ballplay = Ball(WIDTH-Ball.RADIUS, HEIGHT//2, -VELOCITY,-VELOCITY)
paddle = Paddle(HEIGHT//2)
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

bgColor = pygame.Color("black")
fgColor = pygame.Color("white")
borderColor = pygame.Color("yellow")

pygame.draw.rect(screen, borderColor, pygame.Rect((0,0), (WIDTH, BORDER)))
pygame.draw.rect(screen, borderColor, pygame.Rect(0,0, BORDER, HEIGHT))
pygame.draw.rect(screen, borderColor, pygame.Rect(0,HEIGHT-BORDER, WIDTH, BORDER))

ballplay.show(fgColor)
paddle.show(fgColor)

clock = pygame.time.Clock()
sample = open("game.csv", "w")

print("x,y,vx,vy,Paddle.y", file=sample)


while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    clock.tick(FRAMERATE)
    pygame.display.flip()
    paddle.update()
    ballplay.update()
    print("{}, {}, {}, {}, {}".format(ball.x, ball.y, ball.vx, ball, vy, paddle.y), file=sample)
    
pygame.quit()
