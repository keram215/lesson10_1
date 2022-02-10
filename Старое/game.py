from functions import get_words, shuffle_word,write_history, get_stattistics


def game():
    user_name = input('Ведите ваше имя')
    user_score = 0
    words = get_words()

    for word in words:
        word_shafllle = ''.join(shuffle_word(word))
        user_answer = input(f'Угадай слово: {word_shafllle}')
        if user_answer == word:
            print('Верно! Вы получаете 10 очков')
            user_score += 10
        else:
            print(f'Неверно! Верный отыет - {word}.')

    write_history(user_name,user_score)
    total_games, high_score = get_stattistics()
    print(f'Всего игр сыграно: {total_games}\nМаксимальный рекорд: {high_score}')


game()

