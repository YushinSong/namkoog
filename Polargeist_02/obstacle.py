from pico2d import*
import random

# 25초, 40초

class Obstacle:
    PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 3.4  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)
    #  스피드 인듯

    SQUARE, TRIANGLE, HALF_SQUARE, SPIKE = 0, 1, 2, 3
    NONE_WALL, UP_LEFT_RIGHT, UP_LEFT, LEFT_RIGHT = 4, 5, 6, 7
    UP_RIGHT, UP, LEFT, RIGHT, DOWN, DOWN_TRIANGLE = 8, 9, 10, 11, 12, 13
    image = None

    def __init__(self):
        self.number = random.randint(0, 2)
        self.x, self.y = 0, 0
        self.over_y, self.jumping, self.fall, self.y_stop = False, False, False, False
        self.total_frame, self.count, self.count_over = 0.0, 0, 0
        self.soldierX, self.soldierY = 0, 0
        self.nearby, self.collinearby = False, False
        self.y_distance = 0.0
        self.shape = 0
        self.total_frame = 0.0
        if Obstacle.image == None:
            Obstacle.image = load_image('Ground\\obstacle.png')

    def square(self):
        self.frame, self.state = 1, 405
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65
    def triangle(self):
        self.frame, self.state = 94, 405
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65
    def half_square(self):
        self.frame, self.state = 100, 300
        self.wid, self.hei, self.rwid, self.rhei = 102, 95, 65, 65
    def spike(self):
        if self.number == 0:
            self.frame, self.state = 400, 330
        elif self.number == 1:
            self.frame, self.state = 400, 250
        else:
            self.frame, self.state = 400, 162
        self.wid, self.hei, self.rwid, self.rhei = 110, 70, 68, 45
    def none_wall(self):
        self.frame, self.state = 191, 403
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65
    def up_left_right(self):
        self.frame, self.state = 284, 404
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65
    def up_left(self):
        self.frame, self.state = 383, 399
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 62, 62
    def left_right(self):
        self.frame, self.state = 0, 305
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65
    def up_right(self):
        self.frame, self.state = 202, 305
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65
    def up(self):
        self.frame, self.state = 297, 301
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65
    def left(self):
        self.frame, self.state = 6, 195
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 64, 64
    def right(self):
        self.frame, self.state = 103, 198
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65
    def down(self):
        self.frame, self.state = 398, 62
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65
    def down_triangle(self):
        self.frame, self.state = 300, 205
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65



    handle_state = {
        SQUARE: square,
        TRIANGLE: triangle,
        HALF_SQUARE: half_square,
        SPIKE: spike,
        NONE_WALL: none_wall,
        UP_LEFT_RIGHT: up_left_right,
        UP_LEFT: up_left,
        LEFT_RIGHT: left_right,
        UP_RIGHT: up_right,
        UP: up,
        LEFT: left,
        RIGHT: right,
        DOWN: down,
        DOWN_TRIANGLE: down_triangle
    }

    def update(self, frame_time):
        self.total_frame += frame_time
        distance = Obstacle.RUN_SPEED_PPS * frame_time
        if 85 > self.total_frame >= 1.1:
            self.x -= distance
        self.handle_state[self.shape](self)


        tempX, tempY = self.x - self.soldierX, self.y - self.soldierY
        self.tempdistance = math.sqrt((tempX * tempX) + (tempY * tempY))
        if self.tempdistance < 1100:
            self.nearby = True
        else:
            self.nearby = False
        if self.tempdistance < 150:
            self.collinearby = True
        else:
            self.collinearby = False

        if self.over_y == True:
            if self.jumping == True:
                self.y -= self.y_distance
            if self.fall == True:
                if self.y_stop == False:
                    self.y += self.y_distance

    def get_bb(self):
        if self.shape in (0, 5, 6, 7, 8, 9, 10, 11, 12):
            return self.x - 42, self.y - 28, self.x + 42, self.y + 31
        elif self.shape in (1, 13):
            return self.x - 10, self.y - 28, self.x + 10, self.y + 25
        elif self.shape == 2:
            return self.x - 42, self.y, self.x + 42, self.y + 31
        elif self.shape == 3:
            return self.x - 30, self.y - 28, self.x + 30, self.y + 10
        else:
            return 0, 0, 0, 0

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.image.clip_draw(self.frame, self.state, self.wid, self.hei, self.x, self.y, self.rwid, self.rhei)

def create_obstacles_01():
    obstacle_state_table = {
        "SQUARE": Obstacle.SQUARE,
        "TRIANGLE": Obstacle.TRIANGLE,
        "HALF_SQUARE": Obstacle.HALF_SQUARE,
        "SPIKE": Obstacle.SPIKE,
        "NONE_WALL": Obstacle.NONE_WALL,
        "UP_LEFT_RIGHT": Obstacle.UP_LEFT_RIGHT,
        "UP_LEFT": Obstacle.UP_LEFT,
        "LEFT_RIGHT": Obstacle.LEFT_RIGHT,
        "UP_RIGHT": Obstacle.UP_RIGHT,
        "UP": Obstacle.UP,
        "LEFT": Obstacle.LEFT,
        "RIGHT": Obstacle.RIGHT,
        "DOWN": Obstacle.DOWN,
        "DOWN_TRIANGLE": Obstacle.DOWN_TRIANGLE
    }
    obstacle_data_file = open('ob_data\\obstacle_data_01.txt', 'r')
    obstacle_data = json.load(obstacle_data_file)
    obstacle_data_file.close()

    obstacle = []
    for name in obstacle_data:
        ob = Obstacle()
        ob.name = name
        ob.x = obstacle_data[name]['x'] - 00
        ob.y = obstacle_data[name]['y']
        ob.shape = obstacle_state_table[obstacle_data[name]['StartState']]
        obstacle.append(ob)

    return obstacle

def create_obstacles_02():
    obstacle_state_table = {
        "SQUARE": Obstacle.SQUARE,
        "TRIANGLE": Obstacle.TRIANGLE,
        "HALF_SQUARE": Obstacle.HALF_SQUARE,
        "SPIKE": Obstacle.SPIKE,
        "NONE_WALL": Obstacle.NONE_WALL,
        "UP_LEFT_RIGHT": Obstacle.UP_LEFT_RIGHT,
        "UP_LEFT": Obstacle.UP_LEFT,
        "LEFT_RIGHT": Obstacle.LEFT_RIGHT,
        "UP_RIGHT": Obstacle.UP_RIGHT,
        "UP": Obstacle.UP,
        "LEFT": Obstacle.LEFT,
        "RIGHT": Obstacle.RIGHT,
        "DOWN": Obstacle.DOWN,
        "DOWN_TRIANGLE": Obstacle.DOWN_TRIANGLE
    }
    obstacle_data_file = open('ob_data\\obstacle_data_02.txt', 'r')
    obstacle_data = json.load(obstacle_data_file)
    obstacle_data_file.close()

    obstacle = []
    for name in obstacle_data:
        ob = Obstacle()
        ob.name = name
        ob.x = obstacle_data[name]['x'] - 16000
        ob.y = obstacle_data[name]['y'] + 3
        ob.shape = obstacle_state_table[obstacle_data[name]['StartState']]
        obstacle.append(ob)

    return obstacle

def create_obstacles_03():
    obstacle_state_table = {
        "SQUARE": Obstacle.SQUARE,
        "TRIANGLE": Obstacle.TRIANGLE,
        "HALF_SQUARE": Obstacle.HALF_SQUARE,
        "SPIKE": Obstacle.SPIKE,
        "NONE_WALL": Obstacle.NONE_WALL,
        "UP_LEFT_RIGHT": Obstacle.UP_LEFT_RIGHT,
        "UP_LEFT": Obstacle.UP_LEFT,
        "LEFT_RIGHT": Obstacle.LEFT_RIGHT,
        "UP_RIGHT": Obstacle.UP_RIGHT,
        "UP": Obstacle.UP,
        "LEFT": Obstacle.LEFT,
        "RIGHT": Obstacle.RIGHT,
        "DOWN": Obstacle.DOWN,
        "DOWN_TRIANGLE": Obstacle.DOWN_TRIANGLE
    }
    obstacle_data_file = open('ob_data\\obstacle_data_03.txt', 'r')
    obstacle_data = json.load(obstacle_data_file)
    obstacle_data_file.close()

    obstacle = []
    for name in obstacle_data:
        ob = Obstacle()
        ob.name = name
        ob.x = obstacle_data[name]['x'] - 24120 #24120
        ob.y = obstacle_data[name]['y'] + 3
        ob.shape = obstacle_state_table[obstacle_data[name]['StartState']]
        obstacle.append(ob)

    return obstacle

def create_obstacles_04():
    obstacle_state_table = {
        "SQUARE": Obstacle.SQUARE,
        "TRIANGLE": Obstacle.TRIANGLE,
        "HALF_SQUARE": Obstacle.HALF_SQUARE,
        "SPIKE": Obstacle.SPIKE,
        "NONE_WALL": Obstacle.NONE_WALL,
        "UP_LEFT_RIGHT": Obstacle.UP_LEFT_RIGHT,
        "UP_LEFT": Obstacle.UP_LEFT,
        "LEFT_RIGHT": Obstacle.LEFT_RIGHT,
        "UP_RIGHT": Obstacle.UP_RIGHT,
        "UP": Obstacle.UP,
        "LEFT": Obstacle.LEFT,
        "RIGHT": Obstacle.RIGHT,
        "DOWN": Obstacle.DOWN,
        "DOWN_TRIANGLE": Obstacle.DOWN_TRIANGLE
    }
    obstacle_data_file = open('ob_data\\obstacle_data_04.txt', 'r')
    obstacle_data = json.load(obstacle_data_file)
    obstacle_data_file.close()

    obstacle = []
    for name in obstacle_data:
        ob = Obstacle()
        ob.name = name
        ob.x = obstacle_data[name]['x'] - 47720 #47720
        ob.y = obstacle_data[name]['y'] + 2
        ob.shape = obstacle_state_table[obstacle_data[name]['StartState']]
        obstacle.append(ob)

    return obstacle
