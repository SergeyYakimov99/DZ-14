class BasicWord:

    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

        self.answer_user = None

    def is_correct(self, answer_user):
        """ проверка введенного слова в списке допустимых подслов (вернет bool)"""
        if answer_user.lower() in self.sub_words:
            return True
        return False

    def count_subwords(self):
        """ подсчет количества подслов, которые можно составить из исходного слова"""
        return len(self.sub_words)
