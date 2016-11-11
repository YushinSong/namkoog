from pico2d import*

class Soldier:
    # 기여운 솔져의 이동속도는 1초에 1미터
    PIXEL_PER_METER = (70.0 / 0.1)  # 70 pixel 10cm
    RUN_SPEED_KMPH = 2.8  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)
    #  스피드 인듯

    JUMP_SPEED_KMPH = 3.5  # Km / Hour
    JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?).

    def __init__(self):
        self.x, self.y = -500, 215
        self.frame, self.count, self.round_count, self.count_over = 0, 0, 0, 0
        self.total_frame = 0.0
        self.jumping = False
        self.fall = False
        self.image = load_image('Character\\soldier76.png')

    def jump(self, frame_time):
        y_distance = Soldier.JUMP_SPEED_PPS * frame_time
        #print("%lf" % self.total_frame)
        if self.jumping == True or self.fall == True:
            if (self.round_count < 4):
                if (self.round_count == 3):
                    self.frame = (self.frame + 1) % 46
                    self.round_count = 0
                self.round_count += 1

            if self.fall == True:
                self.y -= y_distance

            if self.jumping == True:
                if self.count == 0:
                    self.count = self.total_frame
                    self.count_over = self.count + 0.25
                else:
                    if self.total_frame < self.count_over:
                        self.y += y_distance
                    else:
                        self.count = 0
                        self.fall = True
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
        self.total_frame += frame_time

        if self.total_frame < 1.5:
            self.x += distance
        self.jump(frame_time)

    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN and self.fall == False:
            self.jumping = True

    def get_bb(self):
        return self.x - 28, self.y - 45, self.x + 27, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 90, 90)
        self.draw_bb()

