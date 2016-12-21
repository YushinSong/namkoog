import game_framework
import main_game
from pico2d import *


name = "rest"
image = None

def enter():
    pass

def exit():
    close_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def draw(frame_time):
    clear_canvas()
    update_canvas()


def update(frame_time):
    game_framework.change_state(main_game)

def pause():
    pass


def resume():
    pass






