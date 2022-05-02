import utils
from kurs_2.Player import Player

path = "https://jsonkeeper.com/b/CRV0"

print('Ввведите имя игрока ')
user_name = input()
player = Player(user_name)
print()
print(f'Привет {user_name}.')
print()

basic_word = utils.load_random_word(path)

print(f'Составьте {basic_word.count_subwords()} слов из слова "{basic_word.word.upper()}"')
print('Слова должны быть не короче 3 букв.')
print('Поехали, ваше первое слово?')

while player.count_word_user() < basic_word.count_subwords():
    user_input = input().lower()
    if user_input in ["stop", "стоп"]:
        break

    if not basic_word.is_correct(user_input):
        print('Такого слова нет.')
        continue

    if player.chek_user_word(user_input):
        print('Такое слово уже было.')
        continue

    player.append_inuser_word(user_input)
    print('Верно.')

# Статистика
print('Слова закончились, игра завершена!')
print(f'вы угадали {player.count_word_user()} слов!')
