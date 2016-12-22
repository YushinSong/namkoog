from pico2d import*


class Airplane:
    Y_PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    Y_RUN_SPEED_KMPH = 2.0 # Km / Hour
    Y_RUN_SPEED_MPM = (Y_RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    Y_RUN_SPEED_MPS = (Y_RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    Y_RUN_SPEED_PPS = (Y_RUN_SPEED_MPS * Y_PIXEL_PER_METER)  # PPS = pulse per second(?)

    X_PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    X_RUN_SPEED_KMPH = 2.1  # Km / Hour
    X_RUN_SPEED_MPM = (X_RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    X_RUN_SPEED_MPS = (X_RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    X_RUN_SPEED_PPS = (X_RUN_SPEED_MPS * X_PIXEL_PER_METER)  # PPS = pulse per second(?)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    UP_TIME_PER_ACTION = 1.0
    UP_ACTION_PER_TIME = 0.1 / UP_TIME_PER_ACTION
    UP_FRAMES_PER_ACTION = 8
    image = None

    def __init__(self):
        self.x, self.y = 450, 350
        self.frame, self.round_count_up, self.round_count_down = 2, 0, 0
        self.total_action, self.total_frame = 0.0, 0
        self.a, self.dead, self.dead_time = 0, False, 0
        self.birth, self.rebirth = None, False
        self.up, self.stop, self.upstop, self.dead = False, False, False, False
        if Airplane.image == None:
            Airplane.image = load_image('Character\\airplane.png')

    def update(self, frame_time):
        self.total_frame = self.birth.total_frame
        X_distance = Airplane.X_RUN_SPEED_PPS * frame_time
        Y_distance = (Airplane.Y_RUN_SPEED_PPS + self.a) * frame_time
        if self.dead == False:
            if self.total_frame > 85:
                self.x = min(1130, self.x + X_distance)
                if self.y > 350:
                    self.y = max(350, self.y - Y_distance)
                elif self.y < 350:
                    self.y = min(350, self.y + Y_distance)
            else:
                if self.stop == False and self.upstop == False:
                    if self.up == False:
                        if self.frame < 15:
                            self.total_action += Airplane.FRAMES_PER_ACTION * Airplane.ACTION_PER_TIME * frame_time
                            self.frame = int(self.total_action) % 25
                        self.y -= Y_distance
                    else:
                        if self.frame > 0:
                            self.total_action -= Airplane.UP_FRAMES_PER_ACTION * Airplane.ACTION_PER_TIME * frame_time
                            self.frame = int(self.total_action) % 25
                        self.y += Y_distance
                elif self.stop == True:
                    self.frame = 2
                elif self.upstop == True:
                    self.frame = 2
                    if self.up == False:
                        self.y -= Y_distance

    def reb(self, re):
        self.birth = re

    def death(self):
        if self.dead == False:
            self.birth.bgm.stop()
            self.birth.dead_bgm.play(1)
            self.dead_time = self.total_frame
        self.dead = True
        if (self.total_frame - self.dead_time) > 2.5:
            self.birth.rebirth = True
            self.birth.total_frame = 0.0
            self.birth.x, self.birth.y = -300, 215
            self.birth.bgm.play(1)
            self.dead = False
            self.rebirth = True

    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            self.stop = False
            self.up = True
        elif event.type == SDL_MOUSEBUTTONUP:
            self.up = False

    def get_bb(self):
        return self.x - 28, self.y - 20, self.x + 27, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        if self.dead == False:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 90, 90)
