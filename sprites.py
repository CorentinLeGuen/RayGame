import os

os.environ["RAYLIB_BIN_PATH"] = "raylib-2.0.0-Win64-mingw/lib/"

from raylibpy import Rectangle, load_texture


class Sprite:
    def __init__(self, rectangle: Rectangle, name: str):
        self.__name = name
        self.__rect = rectangle

    def get_name(self):
        return self.__name

    def get_source(self):
        return self.__rect


class FileSprite:
    def __init__(self, file: str):
        try:
            self.__texture = load_texture(file)
        except OSError:
            print('something went wrong')
        self.__source: str = file
        self.__sprites = {}

    def get_file_source(self):
        return self.__source

    def get_file_texture(self):
        return self.__texture

    def add_sprite(self, source: Rectangle, name: str):
        sprite = Sprite(source, name)
        self.__sprites[name] = sprite

    def get_sprite(self, name: str):
        return self.__sprites[name]

    def get_number_of_sprites(self):
        return len(self.__sprites)

    def remove_sprite(self, name: str):
        self.__sprites.pop(name)
