import game_framework
from pico2d import *
import main_game

back = None
soldier = None
rhythm = None
loop_bgm = None
logo_time = 0.0

def enter():
    global back, soldier, rhythm, loop_bgm
    back = load_image('title\\bb.png')
    soldier = load_image('title\\polargeist.png')
    rhythm = load_image('title\\rhythm.png')
    loop_bgm = load_music('song\\menuLoop.mp3')
    loop_bgm.set_volume(64)
    loop_bgm.repeat_play()


def exit():
    global back, soldier, rhythm, loop_bgm
    del(back)
    del(soldier)
    del(rhythm)
    del(loop_bgm)

def update(frame_time):
    pass

def draw(frame_time):
    global back, soldier, rhythm
    clear_canvas()
    rhythm.draw(550, 300)
    soldier.draw(550, 300)
    back.draw(550, 300)
    update_canvas()

def handle_events(frame_time):
    global loop_bgm
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                loop_bgm.stop()
                game_framework.push_state(main_game)



def pause(): pass
def resume(): pass




