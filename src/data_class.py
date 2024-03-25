import csv
from collections import defaultdict

from src.config import PATH_FOR_SAVE
import pandas as pd


class DataSaver:

    def open_data_file(self, data_path) -> list:
        list_info = []
        with open(data_path, encoding='windows-1251') as data_file:
            for row in csv.DictReader(data_file):
                list_info.append(row)
        return list_info

    def save_to_file(self, data_file: list):
        dict_for_save = defaultdict(list)
        with open(PATH_FOR_SAVE, 'w', encoding='windows-1251') as file:
            for data in data_file:
                for key, val in data.items():
                    dict_for_save[key].append(str(val))
            formatted_data = pd.DataFrame(dict_for_save)
            formatted_data.to_csv(file, sep='\t', index= False)
