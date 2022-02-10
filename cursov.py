import requests
import json
import random

from class_word import Word
from class_player import Player


def get_data():
    r = requests.get("https://jsonkeeper.com/b/LVVW")
    return json.loads(r.text)


def get_word(data):
    random.shuffle(data)
    return data[0]


word_data = get_word(get_data())
word = Word(word=word_data['word'], subwords=word_data['subwords'])

def main():
    print('Введите имя')
    user_input = input()
    player = Player(user_input)

while True:
    print(word.word)
    answer = input("Введите свой ответ")

    if answer == 'stop':
        break
    elif not word.check_word(answer):
        print("Нельзя составить")
    elif word.check_word(answer) and player.is_answer(answer):
        print("Правильно")
        player.add(answer)

print(player.point())
