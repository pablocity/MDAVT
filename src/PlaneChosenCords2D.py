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
            for idx, val in enumerate(row):
                if idx == params.chosenDimensions[0]:
                    self.subset.values[0].append(val)
                elif idx == params.chosenDimensions[1]:
                    self.subset.values[1].append(val)

        self.subset.categories.append(inputData.categories[dim[0]])
        self.subset.categories.append(inputData.categories[dim[1]])

    def render(self):
        self.renderer.render(self, self.subset.values[0], self.subset.values[1])

    def export(self):
        pass
