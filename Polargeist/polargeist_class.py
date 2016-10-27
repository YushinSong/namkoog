from pico2d import *

jump = False

#게임 오브젝트 클래스의 정의
class Ground:
    def __init__(self):
        self.image = load_image('Ground\\ground.png')
    def draw(self):
        self.image.clip_draw(0, 0, 896, 127, 900, 70, 1800, 200)
class Soldier:
    global jump, sliding, move
    def __init__(self):
        self.x, self.y = 0, 215
        self.frame = 0
        # frame = 0, 6, 12, 18
        self.image = load_image('Character\\soldier76.png')
    def update(self):
        if jump == True:
            self.frame = (self.frame + 1) % 24
            for i in range(0, 4):
                if i == 4:
                #    jump = False
                    for j in range(0, 4):
                        self.y -= 2
                else:
                    self.y += 2
        else:
            self.frame = 0
        self.x += 2
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y, 90, 90)
