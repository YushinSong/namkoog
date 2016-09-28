from pico2d import *

def handle_events():
    global running
    global wx, wy
    global r
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
             if event.key == SDLK_RIGHT:
                  wx = wx + 10
             elif event.key == SDLK_LEFT:
                  wx = wx - 10
             elif event.key == SDLK_UP:
                  wy = wy + 10
             elif event.key == SDLK_UP:
                  wy = wy - 10
             elif event.key == SDLK_a and r > 20:
                  r = r - 10
             elif event.key == SDLK_d and r < 300:
                  r = r + 10
             elif event.key == SDLK_ESCAPE:
                 running = False



open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
wx, wy = 300, 300
r = 100
x, y = 0, 0
frame = 0
set = 4.7
while (running):
    clear_canvas()
    grass.draw(400, 30)
    x = wx + r * math.sin(set);
    y = wy + r * math.cos(set);
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    set = set + 0.2

    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    handle_events()

close_canvas()

