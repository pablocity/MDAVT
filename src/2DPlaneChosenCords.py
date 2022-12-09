from renderer import Renderer
from data import Data
from strategy import Strategy
from parameters import Parameters


class ChosenCoords(Strategy):

    renderer = Renderer
    subset = Data

    def execute(self, params, inputData):
        Strategy.execute(params, inputData)

    def __genSubset(self, params, inputData):
        dim = params.chosenDimensions
        self.subset = inputData.slice(dim[0], dim[1])

    def __render(self):
        pass

    def __export(self):
        pass
