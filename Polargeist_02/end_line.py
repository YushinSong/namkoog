from pico2d import*

#85초

class EndLine:
    PIXEL_PER_METER = (70.0 / 0.1)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 3.4  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)
    #  스피드 인듯

    image = None
    effect_image = None
    com_image = None


    def __init__(self):
        self.x = 56500
        self.total_frame, self.increase, self.com_increase= 0.0, 0, 0
        self.dead, self.play = False, False
        if EndLine.image == None:
            EndLine.image = load_image('Ground\\end.png')
            EndLine.effect_image = load_image('Ground\\end_effect.png')
            EndLine.com_image = load_image('Ground\\complete.png')
            self.end_bgm = load_music('song\\complete.mp3')
            self.end_bgm.set_volume(64)
            self.end_bgm.play(1)

    def sol(self, sol):
        self.sol =  sol

    def update(self, frame_time):
        distance = EndLine.RUN_SPEED_PPS * frame_time
        self.total_frame = self.sol.total_frame
        if self.dead == False:
            if 85 > self.total_frame >= 1.1:
                    self.x -= distance
            if 86.5 < self.total_frame:
                if self.play == False:
                    self.sol.bgm.stop()
                    self.end_bgm.play(1)
                    self.play = True
                self.increase = min(1, self.increase + 0.002)
                if 88 < self.total_frame:
                    self.com_increase = min(1, self.increase + 0.05)

    def death(self):
        self.dead = True

    def draw(self):
        self.image.clip_draw(0, 0, 200, 1000, self.x, 300, 130, 650)
        self.effect_image.opacify(self.increase) #480
        self.effect_image.clip_draw(0, 0, 1500, 1000, self.x - 480, 300, 1100, 600)
        self.com_image.opacify(self.com_increase)
        self.com_image.clip_draw(0, 0, 1500, 500, 560, 320, 1000, 350)