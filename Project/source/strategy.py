from renderer import *
from data import *
from parameters import *
from dataSource import *


class Strategy:
    fileName = ''
    renderer = Renderer()
    data = Data()


    def __init__(self, fileName) :
        self.fileName = fileName
        self.data = DataSource().getData(fileName)


    def execute(self, params) :
        processedData = self.__calculate()

        if params.outMethod == render:
            self.__render(processedData)
        elif params.outMethod == export:
            self.__export(processedData)


    def __calculate() :
        pass


    def __render() :
        pass


    def __export() :
        pass
