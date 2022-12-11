from renderer import Renderer
from data import Data
from strategy import Strategy


class ParallelCoords(Strategy):

    renderer = Renderer
    subset = Data

    def execute(self, params, inputData):
        Strategy.execute(params, inputData)

    def __genSubset(self, params, inputData):
        self.subset = inputData

    def __render(self):
        pass

    def __export(self):
        pass
