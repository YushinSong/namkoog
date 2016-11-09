from pico2d import*

class Soldier:
    # 기여운 솔져의 이동속도는 1초에 1미터
    PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 3.2  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)
    #  스피드 인듯

    def __init__(self):
        self.x, self.y = -900, 215
        self.frame, self.count, self.round_count = 0, 0, 0
        self.total_frame = 0.0
        self.jumping = False
        self.image = load_image('Character\\soldier76.png')

    def jump(self):
        if self.jumping == True:
            if (self.round_count < 2):
                if (self.round_count == 1):
                    self.frame = (self.frame + 1) % 46
                    self.round_count = 0
                self.round_count += 1
            if (self.count < 13):
                self.y += 13
                self.count += 1
            elif (self.count < 27):
                self.y -= 13
                self.count += 1
                if (self.count == 26):
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

    def update(self, frame_time):
        distance = Soldier.RUN_SPEED_PPS * frame_time

        if self.x < 370:
            self.x += distance
        self.jump()

    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            self.jumping = True

    def get_bb(self):
        return self.x - 28, self.y - 45, self.x + 27, self.y + 15

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 90, 90)

