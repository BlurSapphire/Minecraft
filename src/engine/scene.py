from src.engine.settings import *


class Scene:
    def __init__(self):
        self.win = pg.display.get_surface()

    def render(self):
        ...

    def update(self):
        ...
