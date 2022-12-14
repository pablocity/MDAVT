from data import Data
import pathlib
import pandas


class DataSource:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_extension = pathlib.Path(file_name).suffix

    def __parse_csv(self):
        with open(self.file_name, mode='r') as file:
            csvFile = pandas.read_csv(file)

            data = Data

            data.categories = csvFile.columns.tolist()
            data.values = csvFile.values.tolist()

        file.close()

        return data

    def __parse_xlsx(self):
        xlsxFile = pandas.read_excel(self.file_name)

        data = Data

        data.categories = xlsxFile.columns.tolist()
        data.values = xlsxFile.values.tolist()

        return data

    def __parse_txt(self):
        with open(self.file_name, mode='r') as file:
            txtFile = pandas.read_csv(file, sep=' ')

            data = Data

            data.categories = txtFile.columns.tolist()
            data.values = txtFile.values.tolist()

        file.close()

        return data

    def parse_data(self):
        if self.file_extension == '.csv':
            return self.__parse_csv()
        elif self.file_extension == '.xlsx':
            return self.__parse_xlsx()
        elif self.file_extension == '.txt':
            return self.__parse_txt()
        else:
            return 'Unsupported file extension'
