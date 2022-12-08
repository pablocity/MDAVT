from data import Data
import pathlib


class DataSource:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_extension = pathlib.Path(file_name).suffix

    def __parse_csv(self):
        print('.csv')

    def __parse_xlsx(self):
        print('.xlsx')

    def __parse_txt(self):
        print('.txt')

    def parse_data(self):
        if self.file_extension == '.csv':
            self.__parse_csv()
        elif self.file_extension == '.xlsx':
            self.__parse_xlsx()
        elif self.file_extension == '.txt':
            self.__parse_txt()
        else:
            print('Unsupported file extension')
