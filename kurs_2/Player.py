class Player:

    def __init__(self, user_name):
        self.user_name = user_name
        self.user_subwords = []

    def count_word_user(self):
        """ получение количества отвеченных слов (возвращает int)"""
        return len(self.user_subwords)

    def append_inuser_word(self, word):
        """ добавление слова в использованные слова (ничего не возвращает) """
        self.user_subwords.append(word)

    def chek_user_word(self, word):
        """ проверка использования данного слова до этого (возвращает bool)"""
        return word.lower() in self.user_subwords
