from renderer import Renderer
from data import Data
from strategy import Strategy


class LinearComb(Strategy):
    renderer = Renderer
    subset = Data

    def execute(self, params, inputData):
        super().execute(params, inputData)

    def genSubset(self, params, inputData):
        dim = params.chosenDimensions
        sum = [[] for x in range(len(inputData.values[0]))]

        for row in inputData.values:
            for idx, val in enumerate(row):
                if idx == params.chosenDimensions[0]:
                    self.subset.values[0].append(val)
                elif idx == params.chosenDimensions[1]:
                    self.subset.values[1].append(val)
                else:
                    val *= inputData.values[idx][-2]
                    sum[int(inputData.values[idx][-1])].append(val)

        self.subset.categories.append(inputData.categories[dim[0]])
        self.subset.categories.append(inputData.categories[dim[1]])

        self.subset.values[0] += sum[0]
        self.subset.values[1] += sum[1]

    def render(self):
        pass

    def export(self):
        pass
