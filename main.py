import os

from sprites import FileSprite

os.environ["RAYLIB_BIN_PATH"] = "raylib-2.0.0-Win64-mingw/lib/"

from raylibpy import *
from grid.matrix import Matrix

SIZE_SCREEN_WIDTH = 1600
SIZE_SCREEN_HEIGHT = 900

SIZE_SMALL_TEXT = 11
SIZE_MEDIUM_TEXT = 13
SIZE_BIG_TEXT = 15

SIZE_RENDER_SPRITE: int = 21

TARGET_FPS = 60


def main():
    init_window(SIZE_SCREEN_WIDTH, SIZE_SCREEN_HEIGHT, "RayGame ! - v1.0.0")

    set_target_fps(TARGET_FPS)
    # ======================================================================
    #   Start definition
    # ======================================================================

    frame_counter = 0
    originGrisPosition: Vector2 = Vector2(0, 0)

    # Import the texture pack
    sprite_file = FileSprite('resources/sprites/map.png')

    # Define sprites from the texture pack
    sprite_file.add_sprite(Rectangle(16, 0, 16, 16), 'grass')
    sprite_file.add_sprite(Rectangle(32, 0, 16, 16), 'ground')
    sprite_file.add_sprite(Rectangle(0, 16, 48, 64), 'house')

    # The map
    grid = Matrix(20, 20)

    # ======================================================================
    #   End definition
    # ======================================================================

    while not window_should_close():
        mouse_position: Vector2 = get_mouse_position()

        if frame_counter >= TARGET_FPS:
            frame_counter = 0
        else:
            frame_counter += 1

        begin_drawing()
        clear_background(RAYWHITE)

        # ======================================================================
        #   Start drawing
        # ======================================================================

        # Write some infos
        draw_text("Frame : " + str(frame_counter), 10, 10, SIZE_SMALL_TEXT, BLACK)
        draw_text("FPS : " + str(get_fps()), 10, 30, SIZE_SMALL_TEXT, BLACK)
        draw_text("Mouse X : " + str(int(mouse_position.x)), 10, 50, SIZE_SMALL_TEXT, BLACK)
        draw_text("Mouse Y : " + str(int(mouse_position.y)), 10, 70, SIZE_SMALL_TEXT, BLACK)

        # Draw the grid
        for x in range(grid.get_row_number() + 1):
            for y in range(grid.get_col_number() + 1):
                # Vertical lines
                draw_line(0 + originGrisPosition.x,
                          y * SIZE_RENDER_SPRITE + originGrisPosition.y,
                          grid.get_col_number() * SIZE_RENDER_SPRITE + originGrisPosition.x,
                          y * SIZE_RENDER_SPRITE + originGrisPosition.y,
                          BLACK)
                # Horizontal lines
                draw_line(x * SIZE_RENDER_SPRITE + originGrisPosition.x,
                          0 + originGrisPosition.y,
                          x * SIZE_RENDER_SPRITE + originGrisPosition.x,
                          grid.get_row_number() * SIZE_RENDER_SPRITE + originGrisPosition.y,
                          BLACK)

        # ===== Key events =====================================================
        # === Move the origin
        if is_key_pressed(KEY_RIGHT) or is_key_down(KEY_RIGHT):
            originGrisPosition.x += 1
        if is_key_pressed(KEY_LEFT) or is_key_down(KEY_LEFT):
            originGrisPosition.x -= 1
        if is_key_pressed(KEY_UP) or is_key_down(KEY_UP):
            originGrisPosition.y -= 1
        if is_key_pressed(KEY_DOWN) or is_key_down(KEY_DOWN):
            originGrisPosition.y += 1

        # ======================================================================
        #   End drawing
        # ======================================================================

        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
