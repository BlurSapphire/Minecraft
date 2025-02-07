from src.engine.settings import *
from src.engine.scene import Scene

class Window:
    def __init__(self):
        self.win = pg.display.set_mode(RES)
        pg.display.set_caption(TITLE)
        self.running = True
        self.clock = pg.time.Clock()
        self.dt = None
        self.scene = Scene()

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def render(self):
        self.win.fill(BG_COLOUR)
        pg.display.flip()
        self.scene.render()

    def update(self):
        self.dt = self.clock.tick(FPS) / 1000

    def run(self):
        while self.running:
            self.event_handler()
            self.render()
            self.update()
        pg.quit()
        sys.exit()