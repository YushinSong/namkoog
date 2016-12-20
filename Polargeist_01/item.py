from pico2d import*

class Change:
    PIXEL_PER_METER = (70.0 / 0.1)  # 70 pixel 10cm
    RUN_SPEED_KMPH = 3.4  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # mpm = 1분에 몇미터
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # MPS = 1초당 몇미터
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # PPS = pulse per second(?)
    #  스피드 인듯

    CHANGE_IN, CHANGE_OUT = 0, 1
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.over_y, self.jumping, self.fall, self.y_stop = False, False, False, False
        self.total_frame, self.count, self.count_over = 0.0, 0, 0
        self.y_distance = 0.0
        self.total_frame = 0.0
        self.frame, self.count, self.round_count = 0, 0, 0
        self.state, self.shape = 0, 0
        self.wid, self.hei, self.rwid, self.rhei = 0, 0, 0, 0
        if Change.image == None:
            Change.image = load_image('Item\\change.png')

    def update(self, frame_time):
        distance = Change.RUN_SPEED_PPS * frame_time
        self.total_frame += frame_time
        self.handle_state[self.shape](self)
        if self.total_frame >= 1.1:
            self.x -= distance

        if self.over_y == True:
            if self.jumping == True:
                self.y -= self.y_distance
            if self.fall == True:
                if self.y_stop == False:
                    self.y += self.y_distance

    def change_in(self):
        self.frame, self.state = 0, 0
        self.wid, self.hei, self.rwid, self.rhei = 150, 300, 75, 150

    def change_out(self):
        self.frame, self.state = 150, 0
        self.wid, self.hei, self.rwid, self.rhei = 150, 300, 75, 150

    handle_state = {
        CHANGE_IN: change_in,
        CHANGE_OUT: change_out
    }

    def back_draw(self):
        if self.shape == 0:
            self.image.clip_draw(300, 0, self.wid, self.hei, self.x - 20, self.y, self.rwid, self.rhei)
        elif self.shape == 1:
            self.image.clip_draw(450, 0, self.wid, self.hei, self.x - 20, self.y, self.rwid, self.rhei)

    def draw(self):
        self.image.clip_draw(self.frame, self.state, self.wid, self.hei, self.x, self.y, self.rwid, self.rhei)

    def get_bb(self):
         return self.x - 20, self.y - 60, self.x + 20, self.y + 60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



def create_changes():
    change_state_table = {
        "CHANGE_IN": Change.CHANGE_IN,
        "CHANGE_OUT": Change.CHANGE_OUT
    }
    change_data_file = open('change_data.txt', 'r')
    change_data = json.load(change_data_file)
    change_data_file.close()

    change = []
    for name in change_data:
        portal = Change()
        portal.name = name
        portal.x = change_data[name]['x'] - 000
        portal.y = change_data[name]['y']
        portal.shape = change_state_table[change_data[name]['StartState']]
        change.append(portal)

    return change