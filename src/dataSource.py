from data import Data
import pathlib
import csv
import pandas


class DataSource:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_extension = pathlib.Path(file_name).suffix

    def __parse_csv(self):
        with open(self.file_name, mode='r') as file:
            csvFile = csv.reader(file)

            categories = csvFile.__next__()

            values = []

            for lines in csvFile:
                row = []

                for entry in lines:
                    row.append(entry)

                values.append(row)

        file.close()

    def __parse_xlsx(self):
        print('xlsx')

    def __parse_txt(self):
        with open(self.file_name, mode='r') as file:
            txtFile = pandas.read_csv(file, sep=' ')

            categories = txtFile.columns.tolist()
            values = txtFile.values.tolist()

        file.close()

    def parse_data(self):
        if self.file_extension == '.csv':
            self.__parse_csv()
        elif self.file_extension == '.xlsx':
            self.__parse_xlsx()
        elif self.file_extension == '.txt':
            self.__parse_txt()
        else:
            print('Unsupported file extension')
