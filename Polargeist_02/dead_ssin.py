from pico2d import*
import json


class Dead:
    image = None
    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    def __init__(self):
        self.x, self.y = 0, 0
        self.total_frames, self.frame = 0, 0
        self.who = None
        self.start = False
        if Dead.image == None:
            Dead.image = load_image('Character\\dead.png')


    def set_who_dead(self, who):
        self.who = who

    def update(self, frame_time):
        if self.start == True:
            if self.who != None:
                self.x, self.y = self.who.x, self.who.y
            self.total_frames += Dead.FRAMES_PER_ACTION * Dead.ACTION_PER_TIME * frame_time
            self.frame = int(self.total_frames)

    def draw(self):
        if self.start == True:
            self.image.clip_draw(self.frame * 500, 0, 500, 500, self.x, self.y, 300, 300)

class Attempt:
    PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 3.4  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)
    font = None

    def __init__(self):
        self.x, self.y = 250, 470
        self.dead_count = None
        f = open('font\\dead.txt','r')
        [self.dead_count] = json.load(f)
        f.close()
        self.total_frame, self.dead = 0.0, False
        if Attempt.font == None:
            Attempt.font = load_font('font\\PUSAB___.otf', 80)

    def update(self, frame_time):
        distance = Attempt.RUN_SPEED_PPS * frame_time
        self.total_frame += frame_time
        if self.dead == False:
            if 85 > self.total_frame >= 1.1:
                self.x -= distance

    def death(self):
        f = open('font\\dead.txt', 'w')
        json.dump([self.dead_count], f)
        f.close()
        self.dead = True

    def draw(self):
        Attempt.font.draw(self.x, self.y, 'Attempt %d' % (self.dead_count), (235, 235, 235))
