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

    def __init__(self):
        self.x = 56500
        self.total_frame = 0.0
        if EndLine.image == None:
            EndLine.image = load_image('Ground\\end.png')

    def update(self, frame_time):
        distance = EndLine.RUN_SPEED_PPS * frame_time
        self.total_frame += frame_time

        if self.total_frame >= 1.5:
            if self.x > 1040:
                self.x -= distance

    def stop(self):
        self.dead = True

    def draw(self):
        self.image.clip_draw(0, 0, 200, 1000, self.x, 495, 130, 650)