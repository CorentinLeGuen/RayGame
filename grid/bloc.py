from sprites import Sprite


class Bloc:
    def __init__(self):
        self.__sprite = None

    def set_sprite(self, sprite: Sprite):
        self.__sprite = sprite

    def is_empty(self):
        return self.__sprite is None
