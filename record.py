import pygame
#import pandas as pd
#from sklearn.neighbors import KNeighborsRegressor

WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 15
FRAMERATE = 25
success = 0

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
        global bgColor, fgColor, success

        newX  = self.x + self.vx
        newY  = self.y + self.vy

        if newX < BORDER + self.RADIUS:
            self.vx = - self.vx
        elif newY < BORDER + self.RADIUS or newY > HEIGHT-BORDER-self.RADIUS:
            self.vy = - self.vy
        elif newX+Ball.RADIUS > WIDTH-Paddle.WIDTH and abs(newY-paddle.y) < Paddle.HEIGHT//2:
            self.vx = - self.vx
            success = success + 1
        else:
            self.show(bgColor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(fgColor)

class Paddle:
    WIDTH =20
    HEIGHT = 100

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

ballplay = Ball(WIDTH//2-Ball.RADIUS, HEIGHT//2, -VELOCITY,-VELOCITY)
paddle = Paddle(HEIGHT//2)
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pong by kenken64')
font = pygame.font.Font('freesansbold.ttf', 32)

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

#pong = pd.read_csv('game.csv')
#pong = pong.drop_duplicates()

#X = pong.drop(columns="Paddle.y")
#Y = pong['Paddle.y']

#clf = KNeighborsRegressor(n_neighbors=3)
#clf.fit(X, Y)

#df = pd.DataFrame(columns=['x', 'y', 'vx', 'vy'])

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    clock.tick(FRAMERATE)
    pygame.display.flip()
    text = font.render(str(success), True, pygame.Color("green"), pygame.Color("blue"))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, textRect)
    #toPredict = df.append({'x' : ballplay.x, 'y' : ballplay.y,'vx': ballplay.vx, 'vy': ballplay.vy}, ignore_index=True)
    #print(toPredict)
    #shouldGoThere = clf.predict(toPredict)
    paddle.update()
    ballplay.update()
    print("{}, {}, {}, {}, {}".format(ballplay.x, ballplay.y, ballplay.vx, ballplay.vy, paddle.y), file=sample)

pygame.quit()
