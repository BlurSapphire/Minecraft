from src.engine.settings import *


class Scene:
    def __init__(self):
        self.square = pg.Rect(0, 0, 100, 100)


    def render(self):
        pg.draw.rect(self.square, )

    def update(self):
        ...
