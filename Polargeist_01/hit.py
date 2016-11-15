from pico2d import*
import random


class Hit:
    PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 2.8  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)
    #  스피드 인듯

    SQUARE, TRIANGLE = 0, 1

    def __init__(self):
        self.x, self.y = 0, 0
        self.over_y, self.jumping, self.fall, self.y_stop = False, False, False, False
        self.total_frame, self.count, self.count_over = 0.0, 0, 0
        self.y_distance = 0.0
        self.shape = 0
        self.total_frame = 0.0

    def square(self):
        self.frame, self.state = 0, 405
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65
    def triangle(self):
        self.frame, self.state = 94, 405
        self.wid, self.hei, self.rwid, self.rhei = 95, 95, 65, 65

    handle_state = {
        SQUARE: square,
        TRIANGLE: triangle
    }

    def update(self, frame_time):
        self.total_frame += frame_time
        distance = Hit.RUN_SPEED_PPS * frame_time

        if self.total_frame >= 1.5:
            self.x -= distance
        self.handle_state[self.shape](self)

        if self.over_y == True:
            if self.jumping == True:
                self.y -= self.y_distance
            if self.fall == True:
                if self.y_stop == False:
                    self.y += self.y_distance

    def get_bb(self):
        if self.shape == 0:
            return self.x - 30, self.y - 28, self.x + 30, self.y + 31
        elif self.shape == 1:
            return self.x - 10, self.y - 28, self.x + 10, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.draw_bb()

def create_hit_obstacles():
    obstacle_hit_state_table = {
        "SQUARE": Hit.SQUARE,
        "TRIANGLE": Hit.TRIANGLE
    }
    obstacle_hit_data_file = open('obstacle_hit_data.txt', 'r')
    obstacle_hit_data = json.load(obstacle_hit_data_file)
    obstacle_hit_data_file.close()

    obstacle_hit = []
    for name in obstacle_hit_data:
        h = Hit()
        h.name = name
        h.x = obstacle_hit_data[name]['x'] - 00
        h.y = obstacle_hit_data[name]['y']
        h.shape = obstacle_hit_state_table[obstacle_hit_data[name]['StartState']]
        obstacle_hit.append(obstacle_hit)

    return obstacle_hit