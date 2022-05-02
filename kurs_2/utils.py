import random
import requests

from kurs_2.BasicWord import BasicWord


def load_random_word(path):
    """
    - получает список слов с внешнего ресурса,
    - выберает случайное слово,
    - создает экземпляр класса `BasicWord` и возвращает его.
    """

    words = requests.get(path)
    word_json = words.json()
    word_data = random.choice(word_json)
    word = BasicWord(word_data['word'], word_data['subwords'])
    return word
