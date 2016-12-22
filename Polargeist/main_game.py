from pico2d import*

import game_framework

import collision
from soldier import Soldier
from obstacle import Obstacle, create_obstacles_01, create_obstacles_02, create_obstacles_03, create_obstacles_04
from ground import BackGround, Ground
from item import Change, create_changes
from end_line import EndLine
from airplane import Airplane


back, ground, end = None, None, None
soldier, airplane, changes = None, None, None
change, obstacles, obstacle = None, None, None
FirstStage, SecondStage, ThirdStage = True, False, False
total_frame = 0.0
air = False

def create_world():
    global ground, soldier, back, airplane, change, obstacles, obstacle, changes, end
    end = EndLine()
    changes = create_changes()
    obstacles = create_obstacles_01()
    obstacle = Obstacle()
    back = BackGround()
    ground = Ground()
    soldier = Soldier()
    change = Change()
    airplane = Airplane()

def destroy_world():
    global ground, soldier, back, airplane, change

    del(ground)
    del(soldier)
    del(back)
    del(airplane)
    del(change)

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
    ground.update(frame_time)
    back.update(frame_time)
    end.update(frame_time)
    stage(frame_time)

    for ob in obstacles:
        if air == False:
            ob.soldierX, ob.soldierY = soldier.x, soldier.y
        else:
            ob.soldierX, ob.soldierY = airplane.x, airplane.y
        ob.update(frame_time)
    if air == False:
        soldier.update(frame_time)
        collision_soldier(frame_time)
    else:
        soldier.jumping = False
        if ground.notice_for_soldier == False:
            soldier.over_y = True
        airplane.update(frame_time)
        collision_airplane(frame_time)

    for change in changes:
        change.update(frame_time)



def draw(frame_time):
    clear_canvas()
    back.draw()
    end.draw()
    for change in changes:
        change.back_draw()
    for ob in obstacles:
        if ob.nearby == True:
            ob.draw()
            #ob.draw_bb()
    ground.draw()
    #ground.draw_bb()
    if air == False:
        soldier.draw()
    else:
        airplane.draw()
    #soldier.draw_bb()
    #airplane.draw_bb()
    for change in changes:
        change.draw()

    update_canvas()

def collision_airplane(frame_time):
    global air
    for change in changes:
        if collision.Collide(airplane, change):
            if change.shape == 1:
                air = False
                soldier.x, soldier.y = airplane.x, airplane.y + 5
    if collision.Collide(airplane, ground):
        airplane.stop = True
    else:
        for obstacle in obstacles:
            if obstacle.collinearby == True:
                if collision.Collide(airplane, obstacle) == False:
                    airplane.stop = False
                    airplane.upstop = False
    for obstacle in obstacles:
        if obstacle.collinearby == True:
            if collision.TableCollide(airplane, obstacle):
                if obstacle.shape in (0, 2, 5, 6, 7, 8, 9, 10, 11, 12):
                    airplane.stop = True
            if collision.DownCollide(airplane, obstacle):
                if obstacle.shape in (0, 2, 5, 6, 7, 8, 9, 10, 11, 12):
                    airplane.upstop = True


def collision_soldier(frame_time):
    global air
    for obstacle in obstacles:
        if soldier.jumping == True:  # 솔져가 뛸 때
            ground.notice_for_soldier = False # 무조건 땅이 경계선에 없다고..?????
        for change in changes:
            if ground.notice_for_soldier == False: # 땅이 경계선에 없을 때(작동)
                if soldier.over_y == True:   # 솔져가 시야에 없을 때
                    obstacle.y_stop, change.y_stop = False, False  # 장애물이 움직인다
                    ground.over_y, obstacle.over_y, change.over_y = True, True, True # 장애물과 땅이 움직인다
                    ground.y_distance, obstacle.y_distance, change.y_distance = soldier.y_distance, soldier.y_distance, soldier.y_distance
                    ground.jumping, ground.fall = soldier.jumping, soldier.fall
                    obstacle.jumping, obstacle.fall = soldier.jumping, soldier.fall
                    change.jumping, change.fall = soldier.jumping, soldier.fall
            else: # 땅이 경계선에 왔따(작동)
                if soldier.over_y == True:  # 솔져가 시야에 없다
                    soldier.y -= soldier.y_distance
                    laydown(frame_time)
                soldier.over_y = False  #솔져 시야에 있는걸로 바꿔줌
                ground.over_y, obstacle.over_y, change.over_y= False, False, False # 땅과 장애물이 멈춘다
                obstacle.y_stop, change.y_stop = True, True  # 장애물 멈춘다
    for change in changes:
        if collision.Collide(soldier, change):
            if change.shape == 0:
                airplane.x, airplane.y = soldier.x, soldier.y
                soldier.over_y = False
                ground.y_stop = False
                air = True


    if collision.Collide(soldier, ground):
        if soldier.keep == True:
            soldier.jumping = True
        soldier.fall = False
    else:
        for obstacle in obstacles:
            if obstacle.collinearby == True:
                if collision.Collide(soldier, obstacle) == False and soldier.jumping == False:
                    soldier.fall = True
    for obstacle in obstacles:
        if obstacle.collinearby == True:
            if collision.TableCollide(soldier, obstacle):
                if obstacle.shape in (0, 2, 5, 6, 7, 8, 9, 10, 11):
                    soldier.fall = False
                    if soldier.keep == True:
                        soldier.jumping = True
            if collision.Collide(soldier, obstacle):
                if obstacle.shape in (1, 13):
                    soldier.death()
                    soldier.fall = False
                    if soldier.keep == True:
                        soldier.jumping = True

def stage(frame_time):
    global air, obstacles, FirstStage, SecondStage, ThirdStage, total_frame
    total_frame += frame_time

    soldier.total_frame = total_frame
    if total_frame > 25.3:
        if FirstStage == True:
            obstacles = create_obstacles_02()
            for obstacle in obstacles:
                obstacle.total_frame = 25.3
            FirstStage = False
            SecondStage = True
    if total_frame > 38.3:
        if SecondStage == True:
            obstacles = create_obstacles_03()
            for obstacle in obstacles:
                obstacle.total_frame = 38.3
            SecondStage = False
            ThirdStage = True
    if total_frame > 74:
        if ThirdStage == True:
            obstacles = create_obstacles_04()
            for obstacle in obstacles:
                obstacle.total_frame = 74
            ThirdStage = False

def laydown(frame_time):
    for obstacle in obstacles:
        obstacle.y -= ( soldier.y_distance * 0.999 )
    for change in changes:
        change.y -= ( soldier.y_distance * 0.999 )