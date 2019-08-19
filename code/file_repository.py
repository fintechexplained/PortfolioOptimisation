import pandas as pd

class file_repository:

    def __init__(self, directory):
        self.__writer = pd.ExcelWriter(directory, engine='xlsxwriter')

    def save_to_file(self, data, sheet_name=None):        
        data.to_excel (self.__writer, sheet_name=sheet_name, header=True)

    def close(self):
        self.__writer.save()
