import os
os.environ["RAYLIB_BIN_PATH"] = "raylib-2.0.0-Win64-mingw/lib/"

from raylibpy import *


def main():

    init_window(800, 450, "raylib [core] example - basic window")

    set_target_fps(60)

    while not window_should_close():

        begin_drawing()
        clear_background(RAYWHITE)
        draw_text("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY)
        end_drawing()

    close_window()


if __name__ == '__main__':
    main()