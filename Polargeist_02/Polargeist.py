import platform
import os
if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import pico2d
import game_framework
import main_game
import start_screen
import title_screen

pico2d.open_canvas(1100, 600)
game_framework.run(start_screen)
pico2d.close_canvas()