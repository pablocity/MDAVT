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

        for row in inputData.values:
            self.subset.values[dim[0]].append(row[dim[0]])
            self.subset.values[dim[1]].append(row[dim[1]])

        self.subset.categories.append(inputData.categories[dim[0]])
        self.subset.categories.append(inputData.categories[dim[1]])

    def render(self):
        self.renderer.render(self, self.subset.values[0], self.subset.values[1])

    def export(self):
        pass
