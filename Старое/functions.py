from os.path import isfile
import random

WORDS_FILE_PATH = 'words.txt'
HISTORY_FILE_PATH = 'history.txt'


def get_words():
    if isfile(WORDS_FILE_PATH):
        words_list = []
        with open(WORDS_FILE_PATH) as f:
            for word in f:
                words_list.append(word.strip())
        return words_list
    return []


def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return word_list


def write_history(user_name, user_score):
    formatted_record = f'{user_name} {user_score}\n'
    with open(HISTORY_FILE_PATH, 'a') as f:
        f.write(formatted_record)


def get_stattistics():
    if isfile(HISTORY_FILE_PATH):
        with open(HISTORY_FILE_PATH) as f:
            lines = f. readlines()

        high_score = 0
        total_games = len(lines)
        for line in lines:
            score = int(line.strip().split(' ')[-1])

            if score > high_score:
                high_score = score

        return total_games, high_score
    return '', ''
