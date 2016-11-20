from pico2d import*

class Change:
    PIXEL_PER_METER = (70.0 / 0.1)  # 70 pixel 10cm
    RUN_SPEED_KMPH = 3.4  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)
    #  스피드 인듯

    def __init__(self):
        self.x, self.y = 16160, 420
        self.over_y, self.jumping, self.fall, self.y_stop = False, False, False, False
        self.total_frame, self.count, self.count_over = 0.0, 0, 0
        self.y_distance = 0.0
        self.total_frame = 0.0
        self.frame, self.count, self.round_count = 0, 0, 0
        self.image = load_image('Item\\change.png')

    def update(self, frame_time):
        distance = Change.RUN_SPEED_PPS * frame_time
        self.total_frame += frame_time

        if self.total_frame >= 1.1:
            self.x -= distance

        if self.over_y == True:
            if self.jumping == True:
                self.y -= self.y_distance
            if self.fall == True:
                if self.y_stop == False:
                    self.y += self.y_distance

    def back_draw(self):
        self.image.clip_draw(300, 0, 150, 300, self.x - 20, self.y, 75, 150)

    def draw(self):
        self.image.clip_draw(0, 0, 150, 300, self.x, self.y, 75, 150)
        #self.draw_bb()

    def get_bb(self):
         return self.x - 20, self.y - 60, self.x + 20, self.y + 60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())