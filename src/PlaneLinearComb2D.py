from renderer import Renderer
from data import Data
from strategy import Strategy
class LinearComb(Strategy):
    renderer = Renderer
    subset = Data

    def execute(self):
        pass

    def __genSubset(self, params, inputData):
        dim = params.chosenDimensions
        sum = [[], []]
        self.subset.values = [[], []]
        for i, vec in inputData.values:
            for idx, val in vec:
                if idx == params.chosenDimensions[0]:
                    self.subset.values[0].append(val)
                elif idx == params.chosenDimensions[1]:
                    self.subset.values[1].append(val)
                else:
                    val *= inputData.values[-1][idx]
                    sum[inputData.values[-2][idx]].append(val)

        self.subset.categories.append(inputData.categories[dim[0]])
        self.subset.categories.append(inputData.categories[dim[1]])

        self.subset.values += sum[0]
        self.subset.values += sum[1]

    def __render(self):
        pass

    def __export(self):
        pass