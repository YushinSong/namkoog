import random
from pico2d import *

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 600
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 2
        if self.y >= 95:
            self.y -= random.randint(10, 20)
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

team = [Boy() for i in range(20)]

grass = Grass()
running = True

while running:
    handle_events()

    for boy in team:
        boy.update()
    clear_canvas()
    for boy in team:
        boy.draw()

    grass.draw()
    update_canvas()

    delay(0.05)

close_canvas()