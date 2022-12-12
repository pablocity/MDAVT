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
        for idx, vec in inputData.values:
            if (idx == params.chosenDimensions[0]
                or idx == params.chosenDimensions[1]):
                continue

            vec.nums *= vec.mult
            sum[vec.dim] += vec

        subset = inputData.slice(dim[0], dim[1])
        subset[0] += sum[0]
        subset[1] += sum[1]

    def __render(self):
        pass

    def __export(self):
        pass