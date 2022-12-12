from abc import ABC, abstractmethod

from renderer import Renderer
from data import Data
from parameters import Parameters, ExportMethod, GraphType


class Strategy(ABC):

    renderer = Renderer
    subset = Data

    def execute(self, params, inputData):
        self.genSubset(params, inputData)

        if params.export_method.value == ExportMethod.bitmap.value:
            self.render()
        elif params.export_method == ExportMethod.data_series:
            self.export()

    @abstractmethod
    def genSubset(self, params, inputData):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def export(self):
        pass
