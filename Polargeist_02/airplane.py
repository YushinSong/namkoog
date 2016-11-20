from pico2d import*


class Airplane:
    PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 2.0 # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    UP_ACTION_PER_TIME = 0.1 / TIME_PER_ACTION
    UP_FRAMES_PER_ACTION = 8

    def __init__(self):
        self.x, self.y = 450, 450
        self.frame, self.round_count_up, self.round_count_down = 2, 0, 0
        self.total_action = 0.0
        self.a = 0
        self.image = load_image('Character\\airplane.png')
        self.up = False

    def update(self, frame_time):
        distance = (Airplane.RUN_SPEED_PPS + self.a) * frame_time
        if self.up == False:
            if self.frame < 15:
                self.total_action += Airplane.FRAMES_PER_ACTION * Airplane.ACTION_PER_TIME * frame_time
                self.frame = int(self.total_action) % 25
            self.y -= distance
        else:
            if self.frame > 0:
                self.total_action -= Airplane.UP_FRAMES_PER_ACTION * Airplane.ACTION_PER_TIME * frame_time
                self.frame = int(self.total_action) % 25
            self.y += distance
    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            self.up = True
        elif event.type == SDL_MOUSEBUTTONUP:
            self.up = False

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 90, 90)
