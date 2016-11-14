from pico2d import*


class BackGround:
    PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 0.3  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)
    #  스피드 인듯

    def __init__(self):
        self.x = 550
        # self.bgm = load_music('StereoMadness.mp3')
        # self.bgm.set_volume(64)
        # self.bgm.play(1)
        self.total_frame = 0.0
        self.image = load_image('Ground\\background.png')
        self.blue = load_image('Ground\\background_blue.png')

    def update(self, frame_time):
        # 배경은 1초에 0.1미터
        distance = BackGround.RUN_SPEED_PPS * frame_time
        self.total_frame += frame_time

        if self.total_frame >= 1.5:
            self.x -= distance
            if self.x < -550:
                self.x = 550

    def draw(self):
        self.blue.clip_draw(0, 0, 512, 512, 550, 500, 1100, 1100)
        self.image.clip_draw(0, 0, 1536, 512, self.x, 500, 3300, 1100)


class Ground:
    PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 2.8  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)
    #  스피드 인듯

    def __init__(self):
        self.x, self.y = 900, 70
        self.total_frame = 0.0
        self.over_y, self.jumping, self.fall = False, False, False
        self.notice_for_soldier = True
        self.y_distance = 0.0
        self.image = load_image('Ground\\ground.png')
        self.line = load_image('Ground\\line.png')
        self.blue = load_image('Ground\\ground_blue.png')

    def update(self, frame_time):
        distance = Ground.RUN_SPEED_PPS * frame_time
        self.total_frame += frame_time

        if self.total_frame >= 1.5:
            self.x -= distance
            if self.x < 300:
                self.x = 815
        if self.over_y == True:
            if self.jumping == True:
                self.y -= self.y_distance
            elif self.fall == True:
                if self.y <= 70:
                    self.y += self.y_distance
                    self.notice_for_soldier = False
                else:
                    self.notice_for_soldier = True


    def draw(self):
        self.blue.clip_draw(0, 0, 896, 127, self.x, self.y, 1800, 200)
        self.image.clip_draw(0, 0, 896, 127, self.x, self.y, 1800, 200)
        self.line.clip_draw(0, 0, 896, 127, 560, self.y + 98, 900, 4)

    def get_bb(self):
        return -1000, 0, 1100, 170

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


