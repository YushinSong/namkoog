from pico2d import*


class Airplane:
    PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 3.2  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)

    #  스피드 인듯
    def __init__(self):
        self.x, self.y = 200, 215
        self.frame, self.round_count_up, self.round_count_down = 2, 0, 0
        self.a = 0
        self.image = load_image('Character\\airplane.png')
        self.up = False

    def update(self, frame_time):
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
