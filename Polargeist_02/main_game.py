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
    global air
    for ob in obstacles:
        ob.soldierX, ob.soldierY = soldier.x, soldier.y
        ob.update(frame_time)
    if air == False:
        soldier.update(frame_time)
    else:
        soldier.jumping = False
        if ground.notice_for_soldier == False:
            soldier.over_y = True
        airplane.update(frame_time)
    ground.update(frame_time)
    back.update(frame_time)
    for obstacle in obstacles:
        if soldier.jumping == True:  # 솔져가 뛸 때
            ground.notice_for_soldier = False # 무조건 땅이 경계선에 없다고..?????
        if ground.notice_for_soldier == False: # 땅이 경계선에 없을 때(작동)
            if soldier.over_y == True:   # 솔져가 시야에 없을 때
                obstacle.y_stop, change_in.y_stop = False, False  # 장애물이 움직인다
                ground.over_y, obstacle.over_y, change_in.over_y = True, True, True # 장애물과 땅이 움직인다
                ground.y_distance, obstacle.y_distance, change_in.y_distance = soldier.y_distance, soldier.y_distance, soldier.y_distance
                ground.jumping, ground.fall = soldier.jumping, soldier.fall
                obstacle.jumping, obstacle.fall = soldier.jumping, soldier.fall
                change_in.jumping, change_in.fall = soldier.jumping, soldier.fall
        else: # 땅이 경계선에 왔따(작동)
            if soldier.over_y == True:  # 솔져가 시야에 없다
                soldier.y -= soldier.y_distance
                laydown(frame_time)
            soldier.over_y = False  #솔져 시야에 있는걸로 바꿔줌
            ground.over_y, obstacle.over_y, change_in.over_y= False, False, False # 땅과 장애물이 멈춘다
            obstacle.y_stop, change_in.y_stop = True, True  # 장애물 멈춘다
    change_in.update(frame_time)

    if collide(soldier, change_in):
        soldier.over_y = False
        ground.y_stop = False
        air = True
    if collide(soldier, ground):
        soldier.fall = False
    else:
        for obstacle in obstacles:
            if obstacle.collinearby == True:
                if collide(soldier, obstacle) == False and soldier.jumping == False:
                    soldier.fall = True
    for obstacle in obstacles:
        if obstacle.collinearby == True:
            if collide(soldier, obstacle):
                if obstacle.shape in (0, 2, 5, 6, 7, 8, 9, 10, 11):
                    soldier.fall = False


def draw(frame_time):
    clear_canvas()
    back.draw()
    change_in.back_draw()
    for ob in obstacles:
        if ob.nearby == True:
            ob.draw()
    ground.draw()
    ground.draw_bb()
    if air == False:
        soldier.draw()
    else:
        airplane.draw()
    change_in.draw()


    update_canvas()

def laydown(frame_time):
    for obstacle in obstacles:
        obstacle.y -= ( soldier.y_distance * 0.98 )