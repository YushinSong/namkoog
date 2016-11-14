from pico2d import*

import game_framework

from soldier import Soldier
from obstacle import Obstacle, create_obstacles
from ground import BackGround, Ground
from item import Change
from airplane import Airplane


back, ground = None, None
soldier, airplane = None, None
change_in, obstacles, obstacle = None, None, None
air = False

def create_world():
    global ground, soldier, back, airplane, change_in, obstacles, obstacle
    obstacles = create_obstacles()
    obstacle = Obstacle()
    back = BackGround()
    ground = Ground()
    soldier = Soldier()
    change_in = Change()
    airplane = Airplane()

def destroy_world():
    global ground, soldier, back, airplane, change_in

    del(ground)
    del(soldier)
    del(back)
    del(airplane)
    del(change_in)

def enter():
    open_canvas(1100, 600)
    game_framework.reset_time()
    create_world()

def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if (left_b - right_a) < 100:
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True


def handle_events(frame_time):
    global soldier, air
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            if air == False:
                soldier.handle_event(event)
            else:
                airplane.handle_event(event)

def update(frame_time):
    for ob in obstacles:
        ob.update(frame_time)
    if air == False:
        soldier.update(frame_time)
    else:
        airplane.update(frame_time)
    ground.update(frame_time)
    back.update(frame_time)
    change_in.update(frame_time)

    if collide(soldier, ground):
        soldier.fall = False
    else:
        for obstacle in obstacles:
            if collide(soldier, obstacle) == False and soldier.jumping == False:
                soldier.fall = True
    for obstacle in obstacles:
        if collide(soldier, obstacle):
            if obstacle.shape in (0, 2, 4, 5, 6, 7, 8, 9, 10, 11):
                soldier.fall = False
                #soldier.count = 0

def draw(frame_time):
    clear_canvas()
    back.draw()
    #change_in.back_draw()
    for ob in obstacles:
        ob.draw()
    ground.draw()
    if air == False:
        soldier.draw()
    else:
        airplane.draw()
    #change_in.draw()
    update_canvas()
    #delay(0.013)
