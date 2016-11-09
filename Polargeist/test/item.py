from pico2d import*
from soldier import Soldier

soldier = Soldier()

class Change:
    PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 3.2  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)
    #  스피드 인듯

    def __init__(self):
        self.x, self.y = 2000, 390
        self.frame, self.count, self.round_count = 0, 0, 0
        self.image = load_image('Item\\change.png')

    def update(self, frame_time):
        global soldier
        distance = Change.RUN_SPEED_PPS * frame_time
        if soldier.x >= 370:
            self.x -= distance
            if self.x < 0:
                self.x = 2000

    def back_draw(self):
        self.image.clip_draw(300, 0, 150, 300, self.x - 20, self.y, 75, 150)

    def draw(self):
        self.image.clip_draw(0, 0, 150, 300, self.x, self.y, 75, 150)