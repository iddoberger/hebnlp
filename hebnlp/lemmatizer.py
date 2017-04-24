import pathlib
from typing import Union
import os
import csv
from collections import defaultdict

data_path = pathlib.Path(__file__).parent.parent / 'data'


class Lemmatizer:
    def __init__(self):
        self.lemma_dict = Lemmatizer._create_lemma_dict()

    def get_lemma(self, word) -> Union[list, str, None]:
        lemma_list= self.lemma_dict.get(word, None)
        if lemma_list:
            if len(lemma_list) > 1:
                return lemma_list
            else:
                return lemma_list[0]
    @staticmethod
    def _create_lemma_dict():
        lemma_dict = defaultdict(list)
        for file_name in os.listdir(str(data_path)):
            file_path = data_path / file_name
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    form = row[0]
                    lemma = row[1]
                    lemma_dict[form].append(lemma)
        lemma_dict = dict(lemma_dict)
        for form, lemma_list in list(lemma_dict.items()):
            lemma_dict[form] = list(set(lemma_list))
        return dict(lemma_dict)


