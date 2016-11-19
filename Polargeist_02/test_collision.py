from pico2d import*
import game_framework
import json
import random
from obstacle import Obstacle

# 1미터면 부딫힐 일 없음
# 7칸에 10센치
# 가로 총 110칸 1미터57센치 한번에 15개
# 세로 총 60칸 85센치

balls = None

class Ball:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(100, 500), random.randint(100, 500)
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

    def update(self, frame_time):
        print("아")

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


def create_world():
    global balls
    balls = [Ball() for i in range(5)]

def destroy_world():
    global balls
    del(balls)

def enter():
    open_canvas(500, 500)
    game_framework.reset_time()
    create_world()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def handle_events(frame_time):
    pass

def update(frame_time):
    for ball in balls:
        ball.update(frame_time)

def draw(frame_time):
    clear_canvas()
    update_canvas()

def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass
