from renderer import Renderer
from data import Data


class Strategy:

    renderer = Renderer
    subset = Data

    def execute(self):
        pass

    def __render(self):
        pass

    def __export(self):
        pass
