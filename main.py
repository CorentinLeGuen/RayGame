import os

from sprites import FileSprite

os.environ["RAYLIB_BIN_PATH"] = "raylib-2.0.0-Win64-mingw/lib/"

from raylibpy import *

sizeScreenWidth = 1600
sizeScreenHeight = 900

targetFPS = 60


def main():
    init_window(sizeScreenWidth, sizeScreenHeight, "RayGame ! - v1.0.0")

    set_target_fps(targetFPS)
    # ======================================================================
    #   Start definition
    # ======================================================================

    frame_counter = 0

    # Import the texture pack
    sprite_file = FileSprite('resources/sprites/map.png')

    # Define sprites from the texture pack
    sprite_file.add_sprite(Rectangle(16, 0, 16, 16), 'grass')
    sprite_file.add_sprite(Rectangle(32, 0, 16, 16), 'ground')

    # ======================================================================
    #   End definition
    # ======================================================================

    while not window_should_close():
        mouse_position: Vector2 = get_mouse_position()

        if frame_counter >= targetFPS:
            frame_counter = 0
        else:
            frame_counter += 1

        begin_drawing()
        clear_background(RAYWHITE)

        # ======================================================================
        #   Start drawing
        # ======================================================================

        draw_text("Frame : " + str(frame_counter), 10, 10, 12, BLACK)
        draw_text("FPS : " + str(get_fps()), 10, 30, 12, BLACK)
        draw_text("Mouse X : " + str(int(mouse_position.x)), 10, 50, 12, BLACK)
        draw_text("Mouse Y : " + str(int(mouse_position.y)), 10, 70, 12, BLACK)

        # ======================================================================
        #   End drawing
        # ======================================================================

        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
