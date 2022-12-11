from renderer import Renderer
from data import Data
from parameters import Parameters


class Strategy:

    renderer = Renderer
    subset = Data

    def execute(self, params, inputData):
        self.__genSubset(params, inputData)

        if params.exportMethod == Parameters.export_method.bitmap:
            self.__render()
        elif params.exportMethod == Parameters.export_method.data_series:
            self.__export

    def __genSubset(self, params, inputData):
        pass

    def __render(self):
        pass

    def __export(self):
        pass