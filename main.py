
from basicword import BasicWord
from player import Player
from utils import load_random_word


def main():

    is_game_on = True
    print("Введите имя")
    user_input = input()
    player = Player(user_input)
    print(f"Привет {user_input}")

    randow_word = load_random_word()
    full_word = randow_word.get('word')
    sub_words = randow_word.get('subwords')
    basic_word = BasicWord(full_word,sub_words)
    subword_max_count = basic_word.get_subwords_count()

    print(f'Составте {subword_max_count} слов из слова {basic_word.full_word.upper()}')
    print(f'Слова должны быть не коросе 3 букв')
    print(f"Чтобы закончить игру, угадай все слова или нажми stop")

    while is_game_on:
        user_input = input()

        if user_input == 'stop':
            break
        used_count = player.count()

        if used_count == subword_max_count:
            break
        #print(basic_word.sub_words)
        is_subword = basic_word.has_subwords(user_input)
        was_used = player.is_word_used(user_input)

        if is_subword and not was_used:
            print('Правильный ответ')
            player.add_word(user_input)
        else:
            print('Неверно')

    print('Программа: слова закончились, игра завершена!')
    print(f'Программа: вы угадали {player.count()} слова"')

main()