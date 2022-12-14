from renderer import Renderer
from data import Data
from strategy import Strategy
from parameters import Parameters


class ChosenCords(Strategy):

    renderer = Renderer
    subset = Data
    categories = []

    def execute(self, params, inputData):
        super().execute(params, inputData)

    def genSubset(self, params, inputData: Data):
        dim = params.chosenDimensions
        self.subset = inputData.values[dim[0]: dim[1]]
        self.categories = inputData.categories

    def render(self):
        self.renderer.render(self, self.categories, self.subset)

    def export(self):
        pass
