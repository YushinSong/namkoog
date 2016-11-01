import random
from pico2d import *

back = None
ground = None
sliding = True
running = True
Go = False
air = False

#게임 오브젝트 클래스의 정의
class BackGround:
    def __init__(self):
        self.x = 550
        self.image = load_image('Ground\\background.png')
        self.blue = load_image('Ground\\background_blue.png')
    def update(self):
        global Go
        if Go == True:
            self.x -= 2
            if self.x < -550:
                self.x = 550
    def draw(self):
        self.blue.clip_draw(0, 0, 512, 512, 550, 500, 1100, 1100)
        self.image.clip_draw(0, 0, 1536, 512, self.x, 500, 3300, 1100)

class Ground:
    def __init__(self):
        self.x = 900
        self.image = load_image('Ground\\ground.png')
        self.line = load_image('Ground\\line.png')
        self.blue = load_image('Ground\\ground_blue.png')
    def update(self):
        global Go
        if Go == True:
            self.x -= 10
            if self.x < 400:
                self.x = 900
    def draw(self):
        self.blue.clip_draw(0, 0, 896, 127, 900, 70, 1800, 200)
        self.image.clip_draw(0, 0, 896, 127, self.x, 70, 1800, 200)
        self.line.clip_draw(0, 0, 896, 127, 560, 168, 900, 4)

class Change:
    def __init__(self):
         self.x, self.y = 2000, 390
         self.frame, self.count, self.round_count = 0, 0, 0
         self.image = load_image('Item\\change.png')
    def update(self):
         global Go
         if Go == True:
            self.x -= 10
            if self.x < 0:
                self.x = 2000

    def back_draw(self):
         self.image.clip_draw(300, 0, 150, 300, self.x - 20, self.y, 75, 150)
    def draw(self):
         self.image.clip_draw(0, 0, 150, 300, self.x, self.y, 75, 150)

class Obstacle:
    SQUARE, TRIANGLE, HALF_SQUARE, SPIKE = 0, 1, 2, 3

    def __init__(self):
        self.number = random.randint(0, 2)
        self.image = load_image('Ground\\obstacle.png')

    def square(self):
        self.frame, self.state = 0, 405
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 70, 70

    def triangle(self):
        self.frame, self.state = 94, 405
        self.wid, self.hei, self.rwid, self.rhei  = 95, 95, 70, 70

    def half_square(self):
        self.frame, self.state = 100, 300
        self.wid, self.hei, self.rwid, self.rhei  = 95, 95, 70, 70

    def spike(self):
        if self.number == 0:
            self.frame, self.state = 400, 330
        elif self.number == 1:
            self.frame, self.state = 400, 250
        else:
            self.frame, self.state = 400, 162
        self.wid, self.hei, self.rwid, self.rhei  = 110, 70, 72, 45

    handle_state = {
        SQUARE: square,
        TRIANGLE: triangle,
        HALF_SQUARE: half_square,
        SPIKE: spike
    }
    def update(self):
        global Go
        #if Go == True:
        #    self.x -= 10
        self.handle_state[self.shape](self)
    def draw(self):
        self.image.clip_draw(self.frame, self.state, self.wid, self.hei, self.x, self.y, self.rwid, self.rhei)


class Airplane:
    def __init__(self):
        self.x, self.y = 200, 215
        self.frame, self.round_count_up, self.round_count_down = 2, 0, 0
        self.a = 0
        self.image = load_image('Character\\airplane.png')
        self.up = False
    def update(self):
        global Go
        Go = True
        if self.up == False:
            if (self.round_count_up < 3):
                if (self.round_count_up == 2):
                    self.frame = min(24, self.frame + 1)
                    self.round_count_up = 0
                self.round_count_up += 1
            self.y = min(600, self.y - self.a)
            self.a = min(5, self.a + 0.5)
        else:
            if (self.round_count_down < 2):
                if (self.round_count_down == 1):
                    self.frame = max(0, self.frame - 1)
                    self.round_count_down = 0
                self.round_count_down += 1
            self.y = max(0, self.y + 4)
    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            self.up = True
        elif event.type == SDL_MOUSEBUTTONUP:
            self.up = False
            self.a = 0
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 90, 90)

class Soldier:
    global sliding
    def __init__(self):
        self.x, self.y = 0, 215
        self.frame, self.count, self.round_count = 0, 0, 0
        self.jumping = False
        self.image = load_image('Character\\soldier76.png')
    def jump(self):
        if self.jumping == True:
            if (self.round_count < 2):
                if (self.round_count == 1):
                    self.frame = (self.frame + 1) % 46
                    self.round_count = 0
                self.round_count += 1
            if (self.count < 15):
                self.y += 12
                self.count += 1
            elif (self.count < 31):
                self.y -= 12
                self.count += 1
                if (self.count == 30):
                    self.count = 0
                    self.jumping = False
        else:
            if (0 <= self.frame <= 5 or 41 <= self.frame <= 45):
                self.frame = 0
            elif (6 <= self.frame <= 15):
                self.frame = 10
            elif (16 <= self.frame <= 28):
                self.frame = 22
            elif (29 <= self.frame <= 40):
                self.frame = 34
    def update(self):
        global Go
        if Go == False:
            self.x += 10
            if self.x > 370:
                Go = True
        self.jump()
    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            self.jumping = True
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y, 90, 90)

# 초기화 코드
def enter():
    global ground, soldier, back, airplane, change_in
    open_canvas(1100, 600)
    back = BackGround()
    ground = Ground()
    soldier = Soldier()
    change_in = Change()
    airplane = Airplane()

#입력 핸들
def handle_events():
    global running, soldier, air
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            if air == False:
                soldier.handle_event(event)
            else:
                airplane.handle_event(event)

def create_obstacles():
    obstacle_state_table = {
        "SQUARE": Obstacle.SQUARE,
        "TRIANGLE": Obstacle.TRIANGLE,
        "HALF_SQUARE": Obstacle.HALF_SQUARE,
        "SPIKE": Obstacle.SPIKE
    }
    obstacle_data_file = open('obstacle_data.txt', 'r')
    obstacle_data = json.load(obstacle_data_file)
    obstacle_data_file.close()

    obstacle = []
    for name in obstacle_data:
        ob = Obstacle()
        ob.name = name
        ob.x = obstacle_data[name]['x']
        ob.y = obstacle_data[name]['y']
        ob.shape = obstacle_state_table[obstacle_data[name]['StartState']]
        obstacle.append(ob)

    return obstacle


#게임 루프 코드
enter()
obstacle = create_obstacles()
while running:
    handle_events()

    clear_canvas()

    for ob in obstacle:
        ob.update()

    if air == False:
        soldier.update()
    else:
        airplane.update()
    ground.update()
    back.update()
    change_in.update()

    back.draw()
    #change_in.back_draw()
    for ob in obstacle:
        ob.draw()
    ground.draw()
    if air == False:
        soldier.draw()
    else:
        airplane.draw()
    #change_in.draw()
    update_canvas()

    delay(0.013)
exit()

#종료 코드
